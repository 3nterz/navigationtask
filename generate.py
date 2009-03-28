
# File:   generate.py
# Author: Nathan Tarr

from pyepl.locals import *
import walkthrough
import navigate
import search

def buildTask(task_type, config, town):
	"""
	Builds a runnable task based on type
	"""
	if task_type == "guided":
		return walkthrough.GuidedTask(config, town)

	if task_type == "navigate":
		return navigate.NavigationTask(config, town)

	if task_type == "search":
		return search.SearchTask(config, town)

	return None

def chooseAllLandmarks(task_type, config, townconfig, taskPool, swap = False):
	"""
	Returns 6-tuple (labelled landmarks pool, 
					redundant labelled landmarks pool,
					distinct landmarks pool,
					redundant distinct landmarks pool,
					non-distinct landmarks pool,
					redundant non-distinct landmarks pool)
	"""
	visible = None
	hidden = None
	if swap == True:
		visible = (config.labelledB, config.distinctB, config.nondistinctB)
		hidden = (config.labelledA, config.distinctA, config.nondistinctA)
	else:
		visible = (config.labelledA, config.distinctA, config.nondistinctA)
		hidden = (config.labelledB, config.distinctB, config.nondistinctB)

	labelled = chooseLabelled(townconfig, taskPool, visible[0])
	labelledRedun = Pool()
	if task_type == "guided": 
		labelledRedun = chooseLabelled(townconfig, taskPool, hidden[0], labelled)

	distinct = chooseDistinct(townconfig, taskPool, visible[1])
	distinctRedun = Pool()
	if task_type == "guided":
		distinctRedun = chooseDistinct(townconfig, taskPool, hidden[1], distinct)

	nondistinct = chooseNonDistinct(townconfig, taskPool, visible[2])
	nondistinctRedun = Pool()
	if task_type == "guided":
		nondistinctRedun = chooseNonDistinct(townconfig, taskPool, hidden[2], nondistinct)

	return labelled, labelledRedun, distinct, distinctRedun, nondistinct, nondistinctRedun

def buildLayout(grid, labelledpool, distpool, nondistpool):
	"""
	Create a town layout given a two-dimensional matrix
	"""
	# start with an empty list for the layout configuration
	layoutConfig = []

	# unpack layout into atomic elements
	for row in grid:
		for spot in row:
			if spot not in ("L", "D", "ND", "N", "S", "F"):
				spot = "N"
			layoutConfig.append(spot)

	# wrap layout
	layout = VTownLayout(len(grid[0]), len(grid), layoutConfig)
	layout.fillBlanks(labelledpool.sample(), distpool.sample(), nondistpool.sample())
	
	return layout

def chooseLabelled(townconfig, taskPool, includePool, excludePool = None):
	"""
	Obtain a Pool of labelled landmark definitions
	"""
	landmarkpool = includePool[:]

	# start a Pool of items to be excluded
	exclude = Pool()
	
	# if excludeLandmarksFrom is in the config...
	if hasattr(townconfig, "excludeLandmarksFrom"):
		# populate the exclude pool...
		for townname in townconfig.excludeLandmarksFrom:
			exclude.extend(taskPool.findBy(name = townname).labelledA)
			exclude.extend(taskPool.findBy(name = townname).labelledB)

	if excludePool != None:
		exclude.extend(excludePool)

	# find where items in the exclude Pool match items in the labelled pool...
	for x in exclude:
		# ...and remove them
		try:
			landmarkpool.remove(x)
		except ValueError:
			# if it's not already there, fine
			pass

	landmarkCount = 0
	if hasattr(townconfig, "townLayout"):
		townAreas = unpackLayout(townconfig.townLayout)

		for area in townAreas:
			if area == "L":
				landmarkCount += 1
		
		if landmarkCount > 0 and landmarkCount < len(landmarkpool):
			return landmarkpool.sample(landmarkCount)
		# return as many landmarks as possible
		elif len(landmarkpool) > 0 and landmarkCount >= len(landmarkpool):
			return landmarkpool.sample(len(landmarkpool))
			
	return Pool()

def chooseDistinct(townconfig, taskPool, includePool, excludePool = None):
	"""
	Obtain a Pool of labelled landmark definitions
	"""
	landmarkpool = includePool[:]
	
	# start a Pool of items to be excluded
	exclude = Pool()

	# if excludeLandmarksFrom is in the config...
	if hasattr(townconfig, "excludeLandmarksFrom"):
		# populate the exclude pool...
		for townname in townconfig.excludeLandmarksFrom:
			exclude.extend(taskPool.findBy(name = townname).distinctA)
			exclude.extend(taskPool.findBy(name = townname).distinctB)

	if excludePool != None:
		exclude.extend(excludePool)

	# find where items in the exclude Pool match items in the labelled pool...
	for x in exclude:
		# ...and remove them
		try:
			landmarkpool.remove(x)
		except ValueError:
			# if it's not already there, fine
			pass

	landmarkCount = 0
	if hasattr(townconfig, "townLayout"):
		townAreas = unpackLayout(townconfig.townLayout)

		for area in townAreas:
			if area == "D":
				landmarkCount += 1
		
		if landmarkCount > 0 and landmarkCount < len(landmarkpool):
			return landmarkpool.sample(landmarkCount)
		# return as many landmarks as possible
		elif len(landmarkpool) > 0 and landmarkCount >= len(landmarkpool):
			return landmarkpool.sample(len(landmarkpool))
			
	return Pool()

def chooseNonDistinct(townconfig, taskPool, includePool, excludePool = None):
	"""
	Obtain a Pool of labelled landmark definitions
	"""
	landmarkpool = includePool[:]
	
	# start a Pool of items to be excluded
	exclude = Pool()

	# if excludeLandmarksFrom is in the config...
	if hasattr(townconfig, "excludeLandmarksFrom"):
		
		# populate the exclude pool...
		for townname in townconfig.excludeLandmarksFrom:
			exclude.extend(taskPool.findBy(name = townname).nondistinctA)
			exclude.extend(taskPool.findBy(name = townname).nondistinctB)

	if excludePool != None:
		exclude.extend(excludePool)

	# find where items in the exclude Pool match items in the labelled pool...
	for x in exclude:
		# ...and remove them
		try:
			landmarkpool.remove(x)
		except ValueError:
			# if it's not already there, fine
			pass

	landmarkCount = 0
	if hasattr(townconfig, "townLayout"):
		townAreas = unpackLayout(townconfig.townLayout)

		for area in townAreas:
			if area == "ND":
				landmarkCount += 1
		
		if landmarkCount > 0 and landmarkCount < len(landmarkpool):
			return landmarkpool.sample(landmarkCount)
		# return as many landmarks as possible
		elif len(landmarkpool) > 0 and landmarkCount >= len(landmarkpool):
			return landmarkpool.sample(len(landmarkpool))
			
	return Pool()

def unpackLayout(grid):
	"""
	Unpack layout into atomic elements
	"""
	# start with an empty list for the layout configuration
	layoutConfig = []

	# unpack layout into atomic elements
	for row in grid:
		for spot in row:
			if spot not in ("L", "D", "ND", "N", "S", "F"):
				spot = "N"
			layoutConfig.append(spot)
	
	return layoutConfig

class VTownLayout:
	"""
	Defines placement of geometry and landmarks
	"""
	def __init__(self, xsize, ysize, layoutConfig):
		"""
		Packs given layout configuration (2 dimensional)
		Assume xsize is minimum column size
		Assume ysize is minimum row size
		"""
		configIter = iter(layoutConfig)
		
		self.rows = []
		for y in xrange(ysize):
			row = []
			self.rows.append(row)
			for x in xrange(xsize):
				row.append(configIter.next())

	def __getitem__(self, index):
		"""
		Obtain information about a virtual block
		"""
		if not isinstance(index, tuple) or len(index) != 2:
			raise IndexError, "YCLayout indices must be two-dimensional coordinates"
		return self.rows[index[0]][index[1]]

	def __iter__(self):
		"""
		Iterator of virtual blocks
		"""
		for row in self.rows:
			for value in row:
				yield value

	def getWidth(self):
		"""
		Number of cols in a row
		"""
		return len(self.rows[0])

	def getHeight(self):
		"""
		Number of rows
		"""
		return len(self.rows)

	def getStart(self):
		"""
		Returns a 3-tuple (x, y, z) where x, y and z refer the starting position
		"""
		result = (0.0, 0.0, 0.0)
		
		for x in self:
			if x == "S" or (hasattr(x, "type") and x.type == "start"):
				if hasattr(x, "realpos"):
					result = (x.realpos[0], 0.0, x.realpos[1])
					break
		
		return result

	def getFinish(self):
		"""
		Returns a 3-tuple (x, y, z) where x, y and z refer to the destination position
		"""
		result = (0.0, 0.0, 0.0)

		for x in self:
			if x == "F" or (hasattr(x, "type") and x.type == "finish"):
				if hasattr(x, "realpos"):
					result = (x.realpos[0], 0.0, x.realpos[1])
					break

		return result
	
	def iterLabelled(self):
		"""
		Iterator of virtual blocks that are labelled landmarks
		"""
		for x in self:
			if x == "L" or (hasattr(x, "type") and x.type == "labelled"):
				yield x

	def iterDistinct(self):
		"""
		Iterator of virtual blocks that are distinct landmarks
		"""
		for x in self:
			if x == "D" or (hasattr(x, "type") and x.type == "distinct"):
				yield x

	def iterNonDistinct(self):
		"""
		Iterator of virtual blocks that are non distinct landmarks
		"""
		for x in self:
			if x == "ND" or (hasattr(x, "type") and x.type == "nondistinct"):
				yield x

	def getLabelledPool(self):
		"""
		Obtain a Pool of labelled landmarks
		"""
		return Pool(*self.iterLabelled())

	def getDistinctPool(self):
		"""
		Obtain a Pool of distinct landmarks
		"""
		return Pool(*self.iterDistinct())

	def getNonDistinctPool(self):
		"""
		Obtain a Pool of non distinct landmarks
		"""
		return Pool(*self.iterNonDistinct())

	def fillBlanks(self, landmarkLabelled, landmarkDist, landmarkNonDist):
		"""
		Assign attributes to each block. Note this replaces the character
		"""
		# copy the pools...
		labelledCopy = landmarkLabelled[:]
		distCopy = landmarkDist[:]
		nonDistCopy = landmarkNonDist[:]

		labelledIter = iter(labelledCopy)
		distIter = iter(distCopy)
		nonDistIter = iter(nonDistCopy)

		for y, row in enumerate(self.rows):
			for x, value in enumerate(row):
				if value == "L":
					# TODO: error checking for this statement in general
					p = PoolDict()					
					try:
						p = labelledIter.next().copy()
					except StopIteration:
						labelledIter = iter(labelledCopy)
						try:
							p = labelledIter.next().copy()
						except StopIteration:
							pass
					p.type = "labelled"
					self.rows[y][x] = p
				elif value == "D":
					p = PoolDict()					
					try:
						p = distIter.next().copy()
					except StopIteration:
						distIter = iter(distCopy)
						try:
							p = distIter.next().copy()
						except StopIteration:
							pass
					p.type = "distinct"
					self.rows[y][x] = p
				elif value == "ND":
					p = PoolDict()					
					try:
						p = nonDistIter.next().copy()
					except StopIteration:
						nonDistIter = iter(nonDistCopy)
						try:
							p = nonDistIter.next().copy()
						except StopIteration:
							pass
					p.type = "nondistinct"
					self.rows[y][x] = p
				elif value == "N":
					p = PoolDict()
					p.type = "null"
					self.rows[y][x] = p
				elif value == "S":
					p = PoolDict()
					p.type = "start"
					self.rows[y][x] = p
				elif value == "F":
					p = PoolDict()
					p.type = "finish"
					self.rows[y][x] = p
                

	def addMeasurements(self, unitScale):
		"""
		Assign positional attributes to each virtual block
		"""
		townrows = self.getHeight()
		towncols = self.getWidth()

		# define the size of the virtual town
		self.realsize = ( unitScale*towncols, unitScale*townrows )

		lowx = 0.5*unitScale*(towncols-1)
		lowz = 0.5*unitScale*(townrows-1)

		self.unitScale = unitScale

		for rownum in xrange(townrows):
			for colnum in xrange(towncols):
				item = self[rownum, colnum]
				xpos = unitScale*colnum - lowx
				zpos = unitScale*rownum - lowz
				item.realpos = (xpos, zpos)
				item.negz = (xpos, 0.0, zpos - (unitScale/2.0))
				item.posz = (xpos, 0.0, zpos + (unitScale/2.0))
				item.negx = (xpos - (unitScale/2.0), 0.0, zpos)
				item.posx = (xpos + (unitScale/2.0), 0.0, zpos)
				if hasattr(item, "width") and hasattr(item, "height"):
					item.realsize = (	item.width * unitScale, 
										item.height * unitScale,
										item.width * unitScale )
				else:
					item.realsize = (unitScale, 0.0, unitScale)

	def buildVTown(self, vr, config, touchfunc):
		"""
		Build the layout currently set up
		"""
		# start with a blank environment
		vr.resetEnvironment()	

		# Sky...
		vr.addSkyBox(config.skyImage)

		# Ground & walls...
		vr.addFloorBox(0, 0, 0, self.realsize[0], config.wallHeight, self.realsize[1],
						config.groundImage, config.groundImageLen, config.wallImage, config.wallImagelen)

		# Ground collisions...
		vr.setGravity(0.0, -0.1, 0.0)
		vr.addPlaneGeom(0.0, 1.0, 0.0, 0.0, mu = 0.0)

		# Collisions for external walls...
		# this is to prevent weird issues drawing the wall if we're essentially inside it
		early_wall_distance=.01 
		vr.addPlaneGeom(-1.0, 0.0, 0.0, -(early_wall_distance+self.realsize[0]/2.0), mu = 0)
		vr.addPlaneGeom(1.0, 0.0, 0.0, -(early_wall_distance+self.realsize[0]/2.0), mu = 0)
		vr.addPlaneGeom(0.0, 0.0, 1.0, -(early_wall_distance+self.realsize[1]/2.0), mu = 0)
		vr.addPlaneGeom(0.0, 0.0, -1.0, -(early_wall_distance+self.realsize[1]/2.0), mu = 0)

		# Landmarks
		for item in self:
			if (item.type == "labelled") or (item.type == "distinct") or (item.type == "nondistinct"):
				img = config.sidewalkImage
				if hasattr(item, "image"):
					img = item.image
				itemName = "unknown"
				if hasattr(item, "name"):
					itemName = item.name
				vr.addBuildingBox(item.realpos[0], config.curbHeight, item.realpos[1], img, item.realsize[0], item.realsize[1])
				xsize=item.realsize[0]
				ysize=item.realsize[1] + config.curbHeight
				zsize=item.realsize[2]
				
				vr.addBoxGeom(item.realpos[0], ysize / 2, item.realpos[1], 
							item.realsize[0] + (2 * early_wall_distance), ysize, 
							item.realsize[2] + (2 * early_wall_distance), mu = 0,
                                                        callback = touchfunc, cbargs = (itemName,))
				vr.addBuildingBox(item.realpos[0], 0.0, item.realpos[1], config.curbImage, config.unitScale, 
							config.curbHeight, roofimage = config.sidewalkImage, texlen = config.curbHeight, 
							rooftexlen = config.sidewalkTexLen)

