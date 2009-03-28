# File:   navigate.py
# Author: Nathan Tarr

import extensions
import runnable
import guidedcam
from pyepl.locals import *

class NavigationTask(runnable.Runnable):
	"""
	Wraps task attributes and operations involved
	in presenting the motion through a virtual town and
	in allowing observer to move through that virtual town
	"""

	def __init__(self, config, town):
		"""
		Save task details into this task instance
		"""
		self.config = config

		self.townname = town.name

	def setupTracks(self):
		"""
		Get references to video VideoTrack and VRTrack
		Any extra logging tracks are introduced here
		"""
		# get the already loaded video track
		self.video = VideoTrack.lastInstance()

		# get the already loaded VR track
		self.vr = extensions.VRCamTrack.lastInstance()

		# get the already loaded text logging track
		self.tasklog = extensions.TaskTrack(self.town.logname)

	def setupTown(self):
		"""
		Set up virtual town landmarks
		"""
		pass

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
		#pos = self.layout.getStart()
		
		# set up avatar...
		self.av = self.vr.newAvatar(
			"subject_avatar", 
			eyeheight = self.config.eyeHeight,
			radius = self.config.avatarRadius,
			#posorient = (pos[0], pos[1], pos[2], 0.0, 0.0, 0.0)
			)
		
		# set avatar controls...
		self.av.setControls(
			forward_speed = self.forward, 
			yaw_speed = self.turning
			)
		
		# set up avatar view...
		self.eye = self.av.newEye("subject_view")
		self.eye.setFOV(self.config.FOV)
		self.video.clear() # no need to clear between frames
		self.video.show(self.eye, 0, 0)

	def setupCamera(self):
		"""
		Set up initial view
		"""
		self.cam = guidedcam.GuidedCam()
		self.cam.setHeight(self.config.camHeight)

		camOrient = self.cam.getPosition()

		self.eye = self.vr.newEye("subject_cam")
		self.eye.reposition(camOrient[0], camOrient[1], camOrient[2], camOrient[3], camOrient[4], camOrient[5])
		self.eye.setFOV(self.config.camFOV)
		
		self.video.clear() # no need to clear between frames
		self.video.show(self.eye, 0, 0)

	def updateCamera(self):
		"""
		Get new position of camera and update view
		"""
		done = self.cam.updateCamera()

		camOrient = self.cam.getPosition()

		self.eye.reposition(camOrient[0], camOrient[1], camOrient[2], camOrient[3], camOrient[4], camOrient[5])

		return done

	def guidedLoop(self, f):
		"""
		Update Loop
		"""
		# detect when task ends

		self.video.updateScreen()

		return not self.taskdone

	def navigateLoop(self, f):
		"""
		Update Loop
		"""
		# detect when task ends

		self.video.updateScreen()

		return not self.taskdone

	def landmarkTouched(self, name):
		"""
		Empty function
		"""
		pass	

	def run(self, clock):
		"""
		Sets up the task and starts running it.
		"""
		self.video = VideoTrack.lastInstance()
		self.video.clear("black")
		flashStimulus(Text("Task 2: Welcome to %s" % self.townname), 1000, 0.5, 0.5, None, clock)
		self.video.clear("black")
		flashStimulus(Text("Task 2 is still under development..."), 5000, 0.5, 0.5, None, clock)
		
		#self.taskdone = False

		#self.setupTracks()
		#self.setupTown()

		#self.tasklog.logMessage("Subject #\t%s" % self.town.subject)
		#self.tasklog.logMessage("Date and Time\t%s" % time.asctime(time.localtime(now()/1000)) )
		#self.tasklog.logMessage("Task and Route\t%s\t%s" % (self.town.logname, self.town.name) )
		#if self.town.order == True:
		#	self.tasklog.logMessage("Order\tSwapped")
		#else:
		#	self.tasklog.logMessage("Order\tNot swapped")
		#self.tasklog.logMessage("Tested By\t%s" % self.town.supervisor )
		#self.tasklog.logMessage("")
		#self.tasklog.logMessage("")

		#self.setupControls()
		#self.setupPlayer()

		#self.video.renderLoop(self.mainLoop)

		#self.taskdone = False

