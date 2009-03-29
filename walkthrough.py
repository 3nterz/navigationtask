
# File:   walkthrough.py
# Author: Nathan Tarr

import extensions
import runnable
import guidedcam
import generate
import random
import time
from pyepl.locals import *

class GuidedTask(runnable.Runnable):
	"""
	Wraps task attributes and operations involved
	in presenting the motion through a virtual town
	"""
	
	def __init__(self, config, town):
		"""
		Save task details into this task instance
		"""
		self.config = config
		self.town = town

	def setupTracks(self):
		"""
		Get references to video VideoTrack and VRTrack
		Any extra logging tracks are introduced here
		"""
		# get the already loaded video track
		self.video = VideoTrack.lastInstance()
		# get the already loaded VR track
		self.vr = extensions.VRCamTrack.lastInstance()
		# get the already loaded input track
		self.keyboard = KeyTrack.lastInstance()
		# get the already loaded text logging track
		self.tasklog = extensions.TaskTrack(self.town.logname)

	def setupTown(self):
		"""
		Set up visible virtual town landmarks
		"""
		avail_lmarks = self.town.labelledA
		avail_dmarks = self.town.distinctA
		avail_ndmarks = self.town.nondistinctA
		
		self.layout = generate.buildLayout(self.town.layout, avail_lmarks, avail_dmarks, avail_ndmarks)

		self.layout.addMeasurements(self.config.unitScale)

		self.layout.buildVTown(self.vr, self.config, self.landmarkTouched)

		self.layout.printEnvironment()

	def landmarkTouched(self, name):
		"""
		Empty function
		"""
		pass

	def setupCamera(self):
		"""
		Set up initial view
		"""

		# set up the path camera will move on
		self.cam = guidedcam.GuidedCam()
		self.cam.setHeight(self.config.camHeight)

		# scale camera movements
		camRoute = self.town.route
		scale = self.config.unitScale

		# load motion data into camera
		if len(camRoute) > 0:
			for seg in camRoute:
				if seg[0] == 'linear' and len(seg) == 7:
					self.cam.addLinearSegment(	seg[1]*scale, seg[2]*scale, 
												seg[3]*scale, seg[4]*scale, 
												seg[5], seg[6])
				elif seg[0] == 'curved' and len(seg) == 9:
					self.cam.addCurvedSegment(	seg[1]*scale, seg[2]*scale,
												seg[3]*scale, seg[4]*scale,
												seg[5]*scale, seg[6]*scale,
												seg[7], seg[8])
		
		# get position of camera
		camOrient = self.cam.getPosition()

		# get starting position of camera
		pos = self.layout.getStart()

		# build a camera
		self.eye = self.vr.newEye("subject_cam")
		self.eye.setFOV(self.config.camFOV)

		# camera position is made relative to its starting position
		# camera rotation is absolute
		self.eye.reposition(pos[0] + camOrient[0], 
							camOrient[1], 
							pos[2] + camOrient[2], 
							camOrient[3], camOrient[4], camOrient[5])
		
		# present the view of the camera
		self.video.clear()
		self.video.show(self.eye, 0, 0)

	
	def updateCamera(self):
		"""
		Get new position of camera and update view
		"""
		# determine if camera has completed all its motions
		done = self.cam.updateCamera()

		# camera position is made relative to its starting position
		# camera rotation is absolute
		camOrient = self.cam.getPosition()
		pos = self.layout.getStart()
		self.eye.reposition(pos[0] + camOrient[0], 
							camOrient[1], 
							pos[2] + camOrient[2], 
							camOrient[3], camOrient[4], camOrient[5])

		return done

	def mainLoop(self, f):
		"""
		Update Loop
		"""
		# update at a fixed rate
		thistime = now()
		remaining = thistime - self.lasttime
		if remaining >= 40:
			self.lasttime = self.lasttime + 40
			self.taskdone = self.updateCamera()
		
		# update screen at fastest rate
		self.video.updateScreen()

		return not self.taskdone

	def presentChoice(self, img1, img2, clk, bc):
		"""
		Present two images on the screen.
		Clears the stimulus once a button is pressed

		INPUT ARGS:
		  img1- left PoolDict containing Image object
		  img1- right PoolDict containing Image object
          clk- PresentationClock to update.
          
        OUTPUT ARGS:
          timestamp- time and latency of when the images came on the screen.
          button- Button pressed.
          bc_time- Time and latency of when the button was pressed (if provided)
		"""
		imgOne = img1.image.scale(0.45*img1.width, 0.45*img1.height)
		imgTwo = img2.image.scale(0.45*img2.width, 0.45*img2.height)

		# show images
		self.video.showProportional(imgOne, 0.2, 0.5)
		self.video.showProportional(imgTwo, 0.8, 0.5)

		# show text
		self.video.showProportional(Text("LEFT"), 0.2, 0.9)
		self.video.showProportional(Text("or"), 0.5, 0.9)
		self.video.showProportional(Text("RIGHT"), 0.8, 0.9)

		timestamp = self.video.updateScreen(clk)

		# wait for button press
		button, bc_time = bc.waitWithTime(None, None, clk)
		
		# unshow images
		self.video.unshow(imgOne)
		self.video.unshow(imgTwo)
		self.video.clear("black")
		self.video.updateScreen(clk)
		
		return timestamp, button, bc_time

	def collectLandmarkPairs(self):
		"""
		collect pairs of landmarks from each pool and shuffle the final collection 
		"""
		entryPool = []
		
		# iterate through pairs of landmarks
		for pool in [(self.town.labelledA, self.town.labelledB),
					(self.town.distinctA, self.town.distinctB),
					(self.town.nondistinctA, self.town.nondistinctB)]:
			for entry1, entry2 in zip(pool[0], pool[1]):
				entryPool.append(('L', entry1, entry2))

		# swap the entries for one half of the collection (step by 2)
		for i in xrange(0, len(entryPool), 2):
			entryPool[i] = ('R', entryPool[i][2], entryPool[i][1])

		# shuffle the collection of pairs
		randObj = random.Random()
		randObj.shuffle(entryPool)

		return entryPool

	def run(self, clock):
		"""
		Sets up the task and starts running it.
		"""

		self.setupTracks()

		self.setupTown()

		instruct("%s\n\nYou will be guided through a virtual town. Your task is to remember the landmarks that appear." % self.town.name)

		self.tasklog.logMessage("Subject #\t%s" % self.town.subject)
		self.tasklog.logMessage("Date and Time\t%s" % time.asctime(time.localtime(now()/1000)) )
		self.tasklog.logMessage("Task and Route\t%s\t%s" % (self.town.logname, self.town.name) )
		if self.town.order == True:
			self.tasklog.logMessage("Order\tSwapped")
		else:
			self.tasklog.logMessage("Order\tNot swapped")
		self.tasklog.logMessage("Tested By\t%s" % self.town.supervisor )
		self.tasklog.logMessage("")
		self.tasklog.logMessage("")

		self.tasklog.flush()
		
		self.setupCamera()

		# setup task render loop variables
		self.taskdone = False
		self.lasttime = now()

		self.video.renderLoop(self.mainLoop)

		self.video.clear("black")
		instruct("You will now be tested on which landmarks you remembered.")

		self.tasklog.logMessage("TRIAL #\tLANDMARK 1\tLANDMARK 2\tCATEGORY\tSUBJECT RESPONSE\tACCURACY\tREACTION TIME (ms)")
		self.tasklog.flush()

		# collect pairs of landmarks from each pool and shuffle them
		entryPool = self.collectLandmarkPairs()

		leftKey, rightKey = Key("LEFT"), Key("RIGHT")
		buttonChooser = ButtonChooser(leftKey, rightKey)

		for i, (correct, entry1, entry2) in enumerate(entryPool):
			entries = [entry1, entry2]
			result = self.presentChoice(entries[0], entries[1], clock, buttonChooser)
			reactionTime = result[2][0]-result[0][0]

			if result[1] == leftKey:
				formatStr = "%s\t%s\t%s\t%s\tLEFT\t%s\t%s"
				if correct == 'L':
					self.tasklog.logMessage(formatStr % (i, entries[0].name, entries[1].name, entries[0].category, 1, reactionTime))
				else:
					self.tasklog.logMessage(formatStr % (i, entries[0].name, entries[1].name, entries[0].category, 0, reactionTime))
			elif result[1] == rightKey:
				formatStr = "%s\t%s\t%s\t%s\tRIGHT\t%s\t%s"
				if correct == 'R':
					self.tasklog.logMessage(formatStr % (i, entries[0].name, entries[1].name, entries[0].category, 1, reactionTime))
				else:
					self.tasklog.logMessage(formatStr % (i, entries[0].name, entries[1].name, entries[0].category, 0, reactionTime))

			self.tasklog.flush()

		self.tasklog.logMessage("")
		self.tasklog.flush()

