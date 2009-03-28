
# File:   testsquare.py
# Author: Nathan Tarr

import extensions
import runnable
from pyepl.locals import *

class TestTask(runnable.Runnable):
	"""
	Shows a unit test square that can be measured on screen
	"""
	
	def __init__(self, config, town):
		"""
		Save task details into this task instance
		"""
		self.config = config
	
	def setupTracks(self):
		"""
		Get reference to VideoTrack, VRTrack and KeyTrack
		"""
		# get the already loaded video track
		self.video = VideoTrack.lastInstance()

		# get the already loaded VR track
		self.vr = extensions.VRCamTrack.lastInstance()

		# get the already loaded input track
		self.keyboard = KeyTrack.lastInstance()
		
	def setupTown(self):
		"""
		Set up virtual environment
		"""
		# create a test square to determine participant distance
		self.vr.resetEnvironment()
		
		self.vr.addSkyBox(self.config.blackImage)
		self.vr.addFloorBox(0.0, -1.0, 0.0, self.config.unitScale, self.config.unitScale, self.config.unitScale,
						self.config.blackImage, None, self.config.blackImage, None)
		self.vr.setGravity(0.0, -0.1, 0.0)
		self.vr.addPlaneGeom(0.0, 1.0, 0.0, 0.0, mu = 0.0)
		self.vr.addBuildingBox(0.0, 0.95, -0.5, self.config.whiteImage, 0.1, 0.1)
		
	def setupCamera(self):
		"""
		Set up initial view
		"""
		self.eye = self.vr.newEye("test_cam")
		self.eye.reposition(0.0, 1.0, 0.5, 0.0, 0.0, 0.0)
		self.eye.setFOV(self.config.camFOV)
	
		self.video.clear("black")
		self.video.show(self.eye, 0, 0)
	
	def mainLoop(self, f):
		"""
		Test square loop
		"""
		if (self.callbackKey.isPressed() == True):
			self.taskdone = True
		
		self.video.updateScreen()
		
		return not self.taskdone
					
	def run(self, clock):
		"""
		Start this task
		"""
		self.setupTracks()
		self.setupTown()
		self.setupCamera()
		
		self.callbackKey = Key("RETURN")
		
		self.taskdone = False
		
		self.video.renderLoop(self.mainLoop)
