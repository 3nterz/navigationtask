
# File:   guidedcam.py
# Author: Nathan Tarr

import math

class GuidedCam:
	"""
	A GuidedCam can be set up to follow linear or curved segments in its path
	"""

	def __init__(self):
		"""
		Build a new guided camera with initial settings
		"""
		self.speed = 0.03
		#self.speed = 0.5

		self.t = 0.0
		self.seqnum = 0

		self.currHeight = 0.0
		self.currPoint = (0.0, 0.0)
		self.currYaw = 0.0

		self.routeSegments = []

	def addLinearSegment(self, pointAX, pointAY, pointBX, pointBY, yawA=0.0, yawB=0.0):
		"""
		Add a straight segment to camera path
		"""
		self.routeSegments.append( ("linear", (pointAX, pointAY), (pointBX, pointBY), yawA, yawB) )

	def addCurvedSegment(self, pointAX, pointAY, pointBX, pointBY, pointCX, pointCY, yawA, yawB):
		"""
		Add a curved segment to camera path
		"""
		self.routeSegments.append( ("parabola", (pointAX, pointAY), (pointBX, pointBY), (pointCX, pointCY), yawA, yawB) )

	def lerp(self, a, b, t):
		"""
		Linear interpolation between two values
		"""
		return a + (b - a) * t

	def linearTween(self, pointA, pointB, t):
		"""
		Tweening a path between two 2D points
		"""
		return (self.lerp(pointA[0], pointB[0], t), self.lerp(pointA[1], pointB[1], t))

	def parabolaTween(self, pointA, pointB, pointC, t):
		"""
		Tweening three 2D points to create a parabolic path
		"""
		return self.linearTween(self.linearTween(pointA, pointB, t), self.linearTween(pointB, pointC, t), t)

	def getPosition(self):
		"""
		return (xpos, ypos, zpos, yaw, 0.0, 0.0)
		"""
		return (self.currPoint[0], self.currHeight, self.currPoint[1], self.currYaw, 0.0, 0.0)

	def setHeight(self, newHeight):
		"""
		set the camera height
		"""
		self.currHeight = newHeight

	def getHeight(self):
		"""
		get the camera height
		"""
		return self.currHeight

	def setSpeed(self, newSpeed):
		"""
		set the camera speed over each segment per update invocation
		"""
		self.speed = max(0.0, newSpeed)
		self.speed = min(1.0, newSpeed)

	def getSpeed(self):
		"""
		get the camera speed over each segment per update invocation
		"""
		return self.speed

	def resetCamera(self):
		"""
		prepare camera to start back at starting position
		"""
		self.t = 0.0
		self.seqnum = 0

	def updateCamera(self):
		"""
		update camera position
		"""
		if len(self.routeSegments) > 0:

			if self.seqnum < len(self.routeSegments):		
			
				currSeg = self.routeSegments[self.seqnum]
		
				if currSeg[0] == "linear":
					self.currPoint = self.linearTween(currSeg[1], currSeg[2], self.t)
					self.currYaw = self.lerp(currSeg[3], currSeg[4], self.t)
				elif currSeg[0] == "parabola":
					self.currPoint = self.parabolaTween(currSeg[1], currSeg[2], currSeg[3], self.t)
					self.currYaw = self.lerp(currSeg[4], currSeg[5], self.t)

				self.t += self.speed
				self.t = max(0.0, self.t)

				if self.t >= 1.0:
					self.t = math.fmod(self.t, 1.0)
					self.seqnum = self.seqnum + 1

				return False # Have not traversed all segments yet

			else:
				currSeg = self.routeSegments[len(self.routeSegments) - 1]

				if currSeg[0] == "linear":
					self.currPoint = self.linearTween(currSeg[1], currSeg[2], 1.0)
					self.currYaw = self.lerp(currSeg[3], currSeg[4], 1.0)
				elif currSeg[0] == "parabola":
					self.currPoint = self.parabolaTween(currSeg[1], currSeg[2], currSeg[3], 1.0)
					self.currYaw = self.lerp(currSeg[4], currSeg[5], 1.0)

		return True # Entire route has been traversed

