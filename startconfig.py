#!/usr/bin/python

# File:   project.py
# Author: Nathan Tarr

import wx
from xml.dom import minidom

exitstatus = 0

class ExperimentConfig(wx.Frame):
	"""
	"""
	def __init__(self, parent, id, title):
		"""
		"""
		wx.Frame.__init__(self, parent, id, title, size=(300, 250))

		pnl = wx.Panel(self, -1)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(pnl, -1, 'Name:')
		self.text = wx.TextCtrl(pnl, -1)

		hbox1.Add(label, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
		hbox1.Add(self.text, 1)
		vbox.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

		vbox.Add((-1, 10))

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		label2 = wx.StaticText(pnl, -1, 'Supervisor:')
		self.text2 = wx.TextCtrl(pnl, -1)
		
		hbox2.Add(label2, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
		hbox2.Add(self.text2, 1)
		vbox.Add(hbox2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

		vbox.Add((-1, 10))

		self.resolutions = [('640', '480'), ('800', '600'), ('1024', '768')]
		options = ['640x480', '800x600', '1024x768']

		hboxResL = wx.BoxSizer(wx.HORIZONTAL)
		label2 = wx.StaticText(pnl, -1, 'Resolution:')
		self.cmbBox = wx.ComboBox(pnl, -1, choices=options, style=wx.CB_READONLY)
		self.cmbBox.SetSelection(0)
		hboxResL.Add(label2, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
		hboxResL.Add(self.cmbBox, 1)
		vbox.Add(hboxResL, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

		vbox.Add((-1, 10))

		hboxFullScr = wx.BoxSizer(wx.HORIZONTAL)
		self.chkFullScr = wx.CheckBox(pnl, -1, 'Fullscreen?')
		self.chkFullScr.SetValue(True)
		hboxFullScr.Add(self.chkFullScr, 0)
		vbox.Add(hboxFullScr, 0, wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT, 10)

		vbox.Add((-1, 10))

		hboxOrder = wx.BoxSizer(wx.HORIZONTAL)
		self.chkOrder = wx.CheckBox(pnl, -1, 'Swap visible landmark group?')
		self.chkOrder.SetValue(False)
		hboxOrder.Add(self.chkOrder, 0)
		vbox.Add(hboxOrder, 0, wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT, 10)

		vbox.Add((-1, 30))

		hboxBttn = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(pnl, -1, 'Ok')
		btn1.Bind(wx.EVT_BUTTON, self.OnClickOkay)
		btn2 = wx.Button(pnl, -1, 'Cancel')
		btn2.Bind(wx.EVT_BUTTON, self.OnClickCancel)
		hboxBttn.Add(btn1, 0, 0)
		hboxBttn.Add(btn2, 0, 0)
		vbox.Add(hboxBttn, 0,  wx.ALIGN_RIGHT, 10)

		pnl.SetSizer(vbox)
		
		self.Centre()
		self.Show(True)

	def OnClickOkay(self, event):
		"""
		"""
		global exitstatus

		if not self.text.IsEmpty() and not self.text2.IsEmpty():

			name = self.text.GetValue()
			supervisor = self.text2.GetValue()
			fullscreen = 'False'
			if self.chkFullScr.GetValue():
				fullscreen = 'True'
			resIdx = self.cmbBox.GetCurrentSelection()
			res = self.resolutions[resIdx]
			swaporder = 'False'
			if self.chkOrder.GetValue():
				swaporder = 'True'
			
			xmldoc = minidom.parse("startconfig.xml")
	
			subjectTags = xmldoc.getElementsByTagName("name")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(name)

			subjectTags = xmldoc.getElementsByTagName("supervisor")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(supervisor)

			subjectTags = xmldoc.getElementsByTagName("fullscreen")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(fullscreen)

			subjectTags = xmldoc.getElementsByTagName("resolutionwidth")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(res[0])

			subjectTags = xmldoc.getElementsByTagName("resolutionheight")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(res[1])

			subjectTags = xmldoc.getElementsByTagName("orderswapped")
			if len(subjectTags) > 0 and subjectTags[0].hasChildNodes() == True:
				subjectTags[0].firstChild.replaceWholeText(swaporder)

			fHandle = open("startconfig.xml", 'w')
			fHandle.truncate(0)
			fHandle.write( xmldoc.toprettyxml(indent='', newl='') )
			fHandle.close()

			exitstatus = 0
			self.Destroy()

	def OnClickCancel(self, event):
		"""
		"""
		global exitstatus
		exitstatus = 1
		self.Destroy()

	def GetExitStatus():
		"""
		"""
		return self.exitstatus

app = wx.App()
win = ExperimentConfig(None, -1, 'Experiment Configuration')
app.MainLoop()
exit(exitstatus)
