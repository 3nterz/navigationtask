# Extend or override functionality in PyEPL classes

# File:   extensions.py
# Author: Nathan Tarr

from pyepl.vr import VEye, VRTrack
import pyepl.hardware.vr
from pyepl.textlog import LogTrack

class VCam(VEye):
	"""
	Override functionality found in VEye class
	This is required until new versions of PyEPL are released and circulated
	"""
	def reposition(self, x, y, z, yaw, pitch, roll):
		"""
		Position the camera.
		"""
		self.eye.reposition(x, y, z, yaw, pitch, roll)
		self.lookat = (self.name, x, y, z, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

class VRCamTrack(VRTrack):
	"""
	Override functionality found in VRTrack class
	This is required until new versions of PyEPL are released and circulated
	"""
	def newEye(self, name, xsize = None, ysize = None):
		"""
		Create a VEye for the loaded environment.
		"""
		if xsize == None or ysize == None:
			xsize, ysize = self.videotrack.getResolution()
		return VCam(pyepl.hardware.vr.LowVEye(self.env, xsize, ysize), name, self)

class TaskTrack(LogTrack):
	"""
	Represents a task trail log
	Override functionality found in LogTrack class
	This is for convenience
	"""
	def startLogging(self):
		"""
		Begin logging.
		"""
		if not self.logall:
			self.logall = True
	def stopLogging(self):
		"""
		Stop logging.
		"""
		if self.logall:
			self.logall = False
			self.dataFile.flush()
	def logMessage(self, message, timestamp = None):
		"""
		Add message to log.
		
		INPUT ARGS:
        message- String to add to log.
        timestamp- This value is ignored.
		"""
		if self.logall:
			self.dataFile.seek(0, 2) # seek to end of file
			self.dataFile.write("%s\n" % message)

