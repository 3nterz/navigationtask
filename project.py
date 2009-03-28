#!/usr/bin/python

# File:   project.py
# Author: Nathan Tarr

# obtain PyEPL objects
from pyepl.locals import *
from xml.dom import minidom
import extensions
import generate
import testsquare
import sys

def prepare(exp, config, xmlconfig):
	"""
	This function persists the order the of tasks 
	involved in the Experiment
	"""
	# get the state
	state = exp.restoreState()

	# start with an empty list for the tasks
	taskList = []

	# start an empty pool for tasks that transcend sessions
	bigTaskPool = Pool()

	# for each task...
	for taskNum in xrange(config.numTasks):
		# get task specific configuration
		taskconfig = config.sequence(taskNum)

		# start with an empty pool for the tasks
		taskPool = Pool()

		# get the task log file name
		try:
			tasklogname = taskconfig.tasklogname
		except AttributeError:
			tasklogname = "task%d_log" % taskNum

		# for each town...
		for townNum in xrange(taskconfig.numTowns):
			# get town specific configuration
			townconfig = taskconfig.sequence(townNum)
			
			# get the town name
			try:
				townName = townconfig.townName
			except AttributeError:
				townName = "town%d_%d" % (taskNum, townNum)

			# get the practice flag
			try:
				townPractice = townconfig.practice
			except AttributeError:
				townPractice = False		

			# get the town layout
			try:
				townLayout = townconfig.townLayout
			except AttributeError:
				townLayout = [["N"]]

			# get the town route
			try:
				townRoute = townconfig.route
			except AttributeError:
				townRoute = []

			orderSwapped = xmlconfig["order"]

			# obtain landmark pools
			lmarkLabA, lmarkLabB, lmarkDistA, lmarkDistB, lmarkNonDistA, lmarkNonDistB = generate.chooseAllLandmarks(taskconfig.task_type, config, townconfig, bigTaskPool, orderSwapped)

			# TODO: create town class

			# append town name, town dist landmarks, 
			# town nondist landmarks, town labelled landmarks
			bigTaskPool.append(
				taskPool.append(
					subject = exp.getOptions()["subject"],
					order = xmlconfig["order"],
					supervisor = xmlconfig["suname"],
					name = townName,
					practice = townPractice,
					labelledA = lmarkLabA,
					labelledB = lmarkLabB,
					distinctA = lmarkDistA,
					distinctB = lmarkDistB,
					nondistinctA = lmarkNonDistA,
					nondistinctB = lmarkNonDistB,
					layout = townLayout,
					route = townRoute,
					logname = tasklogname
				)
			)

		# append the tasks to the task list
		taskList.append(taskPool)

	# save the information
	exp.saveState(
		state,
		s_townNum = 0,
		s_taskNum = 0,
		s_taskState = State(),
		s_taskList = taskList
	)

def run(exp, config):
	"""
	Program entry point
	"""
	# get the state
	state = exp.restoreState()

	# set up task...
	if state.s_taskNum >= len(state.s_taskList):
		# if all the tasks have been run, don't continue
		print "No more tasks!"
		return

	# set the session number (so PyEPL knows what directory to put the data in)
	# corresponds to task number
	exp.setSession(state.s_taskNum)

	# get task specific configuration
	taskconfig = config.sequence(state.s_taskNum)

	tasktype = taskconfig.task_type

	# create tracks
	video = VideoTrack("video")
	keyboard = KeyTrack("keyboard")
	vr = extensions.VRCamTrack("vr")

	# create a PresentationClock to handle timing
	clock = PresentationClock()
	
	task = testsquare.TestTask(config, None)
	task.run(clock)

	video.clear("black")
	flashStimulus(Text("Hello %s!" % exp.getOptions()["subject"]), 1000, 0.5, 0.5, None, clock)

	# do each town...
	while state.s_townNum < len(state.s_taskList[state.s_taskNum]):
		# get town specific configuration
		townconfig = taskconfig.sequence(state.s_townNum)

		# unpack the components of the town
		town = state.s_taskList[state.s_taskNum][state.s_townNum]

		# setup and run the current task on given town
		task = generate.buildTask(tasktype, config, town)
		task.run(clock)

		# ...and save the state so that the experiment can be restored from this point
		state = exp.saveState(state, s_townNum = state.s_townNum + 1)
		
	video.clear("black")
	flashStimulus(Text("You have finished..."), 1000, 0.5, 0.5, None, clock)

	# save the state when the session is finished
	# with town and task numbers set for the next session
	exp.saveState(state, s_townNum = 0, s_taskNum = state.s_taskNum + 1)

	# wait for the clock to catch up
	clock.wait()

def start():
	"""
	Function called to start the program
	Parses startconfig.xml
	"""
	xmldoc = minidom.parse("startconfig.xml")
	
	currSubject = None
	subjectTags = xmldoc.getElementsByTagName("name")
	if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
		currSubject = subjectTags[0].firstChild.wholeText

	if currSubject == None:
		print "No participant name is specified"
		exit()

	supervisor = None
	supervisorTags = xmldoc.getElementsByTagName("supervisor")
	if len(supervisorTags) > 0 and supervisorTags[0].hasChildNodes() == True:
		supervisor = supervisorTags[0].firstChild.wholeText

	if supervisor == None:
		print "No supervisor name is specified"
		exit()

	currFullscreen = True
	fullscreenTags = xmldoc.getElementsByTagName("fullscreen")
	if len(fullscreenTags) > 0 and fullscreenTags[0].hasChildNodes() == True:
		currFullscreen = fullscreenTags[0].firstChild.wholeText
		if currFullscreen not in("True", "Yes"):
			currFullscreen = False
		else:
			currFullscreen = True

	currResWidth = 640
	resWidthTags = xmldoc.getElementsByTagName("resolutionwidth")
	if len(resWidthTags) > 0 and resWidthTags[0].hasChildNodes() == True:
		currResWidth = resWidthTags[0].firstChild.wholeText
		currResWidth = int(currResWidth, 10)

	currResHeight = 480
	resHeightTags = xmldoc.getElementsByTagName("resolutionheight")
	if len(resHeightTags) > 0 and resHeightTags[0].hasChildNodes() == True:
		currResHeight = resHeightTags[0].firstChild.wholeText
		currResHeight = int(currResHeight, 10)

	orderSwapped = False
	orderSwappedTags = xmldoc.getElementsByTagName("orderswapped")
	if len(orderSwappedTags) > 0 and orderSwappedTags[0].hasChildNodes() == True:
		orderSwapped = orderSwappedTags[0].firstChild.wholeText
		if orderSwapped not in("True", "Yes"):
			orderSwapped = False
		else:
			orderSwapped = True

	# set up the experiment and PyEPL system
	exp = Experiment(use_eeg=False, sync_to_vbl=False, sconfig="tasks.py", 
					subject=currSubject, fullscreen=currFullscreen, resolution=(currResWidth, currResHeight))
	exp.setup()
	
	# allow users to break out of the experiment with escape-F1 (the default key combo)
	exp.setBreak()
	
	# get the subject configuration
	config = exp.getConfig()

	# setup the xml configuration
	xmlconfig = {
		"order" : orderSwapped,
		"suname" : supervisor
	}

	# if there was no saved state, run the prepare function
	if not exp.restoreState():
		prepare(exp, config, xmlconfig)
	
	# now run the subject
	run(exp, config)

# this experiment is run as a stand-alone program...
if __name__ == "__main__":
	start()
