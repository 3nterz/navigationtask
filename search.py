
# File:   search.py
# Author: Nathan Tarr

import extensions
import runnable
import generate
import time
from pyepl.locals import *

class SearchTask(runnable.Runnable):
	"""
	Wraps task attributes and operations involved
	in allowing observer to move through a virtual town
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
		Set up virtual town landmarks
		"""
		avail_lmarks = self.town.labelledA
		avail_dmarks = self.town.distinctA
		avail_ndmarks = self.town.nondistinctA

		self.layout = generate.buildLayout(self.town.layout, avail_lmarks, avail_dmarks, avail_ndmarks)

		self.layout.addMeasurements(self.config.unitScale)

		self.layout.buildVTown(self.vr, self.config, self.landmarkTouched)

		self.layout.printEnvironment()

		all_landmarks = Pool()
		all_landmarks.extend(avail_lmarks)
		all_landmarks.extend(avail_dmarks)
		all_landmarks.extend(avail_ndmarks)
		
		if len(all_landmarks) > 0:
			self.target = all_landmarks.sample(1)[0]
			self.targetPoolDict = self.target
			self.target = self.target.name
			return True
		
		self.target = "unknown"
		return False

	def setupControls(self):
		"""
		Bind keys to controls
		"""
		# keep track of whether or not we use any left/right and forward/backward buttons...
		leftandright = False
		forwardandbackward = False
		
		# create forward button...
		if hasattr(self.config, "forwardButton"):
			forward_button = self.config.forwardButton
			forwardandbackward = True
		else:
			forward_button = Button() # dummy button
			
		# create backward button...
		if hasattr(self.config, "backwardButton"):
			backward_button = self.config.backwardButton
			forwardandbackward = True
		else:
			backward_button = Button() # dummy button
			
		# create left turn button...
		if hasattr(self.config, "leftButton"):
			left_button = self.config.leftButton
			leftandright = True
		else:
			left_button = Button() # dummy button
		
		# create right turn button
		if hasattr(self.config, "rightButton"):
			right_button = self.config.rightButton
			leftandright = True
		else:
			right_button = Button() # dummy button
			
		# set up navigation control...
		forward_axes = []
		turn_axes = []
		if forwardandbackward:
			forward_axes.append(ButtonAxis(forward_button,
										   backward_button,
										   self.config.fullForwardSpeed,
										   self.config.fullBackwardSpeed))
										   
		if leftandright:
			turn_axes.append(ButtonAxis(right_button,
										left_button,
										self.config.fullTurnSpeed))
										
		self.forward = ThrottledAxis(JointAxis(*forward_axes), maxVel = self.config.maximumLinearAcceleration)
		
		self.turning = JointAxis(*turn_axes)


	def setupPlayer(self):
		"""
		Sets initial orientation of avatar and appends
		controls that move avatar and a first person camera
		"""
		pos = self.layout.getStart()
		
		# set up avatar...
		self.av = self.vr.newAvatar(
			"subject_avatar", 
			eyeheight = self.config.eyeHeight,
			radius = self.config.avatarRadius,
			posorient = (pos[0], pos[1], pos[2], 0.0, 0.0, 0.0)
			)
		
		# set avatar controls...
		self.av.setControls(
			forward_speed = self.forward, 
			yaw_speed = self.turning
			)
		
		# set up avatar view...
		self.eye = self.av.newEye("subject_view")
		self.eye.setFOV(self.config.eyeFOV)
		self.video.clear() # no need to clear between frames
		self.video.show(self.eye, 0, 0)

	def landmarkTouched(self, name):
		"""
		Checks if correct landmark has been found
		"""
		if self.target == name and self.enableTarget == True:
			self.taskdone = True
			self.finishtime = now()
		elif self.target != name and self.enableTarget == True:
			self.incorrectTouches[name] = 1

	def mainLoop(self, f):
		"""
		Update Loop
		"""
		# detect when task ends
		if self.enableTarget == False:
			thistime = now()
			elapsed = thistime - self.lasttime
			if elapsed >= 300000:
				self.enableTarget = True
				buttonChooser = ButtonChooser(Key("RETURN"))
				self.video.clear("black")
				flashStimulus(Text("Please find the following landmark..."), 2500)
				self.video.clear("black")
				img = self.targetPoolDict.image.scale(0.8*self.targetPoolDict.width, 0.8*self.targetPoolDict.height)
				img.present(bc = buttonChooser, minDuration = 2500)
				self.setupPlayer()
				self.lasttime = now()
				self.tasklog.logMessage("SEARCH START TIME: %s" % time.asctime(time.localtime(self.lasttime/1000)))
				self.tasklog.flush()

		self.video.updateScreen()

		return not self.taskdone

	def run(self, clock):
		"""
		Sets up the task and starts running it.
		"""

		self.incorrectTouches = dict()
		self.taskdone = False
		self.enableTarget = False

		self.setupTracks()
		
		# if we fail to setup town we are done
		self.taskdone = not self.setupTown()

		instruct("You will explore a virtual town for at least 5 minutes.\n You will then be required to find a certain landmark.")

		self.setupControls()
		self.setupPlayer()

		self.lasttime = now()
		self.finishtime = None

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

		self.video.renderLoop(self.mainLoop)

		if self.finishtime == None:
			self.finishtime = now()
		searchTime = (self.finishtime - self.lasttime)

		self.tasklog.logMessage("FINISH TIME:\t%s" % time.asctime(time.localtime(self.finishtime/1000)))
		self.tasklog.logMessage("TOTAL SEARCH TIME (ms):\t%s" % searchTime)
		self.tasklog.logMessage("TARGET LANDMARK NAME:\t%s" % self.target)
		self.tasklog.logMessage("NUMBER OF OTHER LANDMARKS TOUCHED:\t%s" % len(self.incorrectTouches))
		self.tasklog.logMessage("")

		self.tasklog.flush()

