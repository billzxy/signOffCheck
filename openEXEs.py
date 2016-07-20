"""
openEXEs.py

Created by Bill X Zhang
Email: xiaoyan.zhang@nyu.edu
All rights not reserved. (LOL Jk) All rights reserved!

Edit with: Python 3.4.4

Purpose: Methods for opening Aura, Notes, PrintStation, and etc...
"""

import os, psutil, subprocess, time

NOTESTAT = ["Initiallizing","Opening"]
NOTES_PROCESS_NAME = "notes2.exe"
NOTES_LOC = 'C:\\Program Files (x86)\\IBM\Lotus\\Notes\\notes.exe'
AURA_PROCESS_NAME = "PwC.Aura.Navigator.App.exe"
AURA_LOC = 'C:\\Program Files (x86)\\PricewaterhouseCoopers\\Aura\\Navigator\\PwC.Aura.Navigator.App.exe'
PSTATION_PROCESS_NAME = "PrintStation 2.0.exe"
PSTATION_LOC = "C:\\Program Files\\PrintStation 2.0\\PrintStation 2.0.exe"


def openAura():
	print("Opening Aura v6 Navigator")
	
	"""
	if(AURA_PROCESS_NAME in [psutil.Process(i).name() for i in psutil.pids()]):
		print "Error: Aura is already running..."
		return 0
	"""

	try:
		subprocess.Popen( AURA_LOC )
	except:
		print("Error: Aura v6 Navigator not found...")
		return 0
	else:
		print("Aura is successfully running...")
		return 1

def runNotes( stat=0 ):
	"""
	arg:
	0 if first time opening notes
	1 if not first time opening notes

	return:
	0 if notes not found in dir, else 1
	"""
	print(NOTESTAT[stat]+" Lotus Notes")
	try:
		subprocess.Popen( NOTES_LOC )	
	except:
		return 0
	else:
		return 1
	
def openNotes():
	"""s
	return:
	-1 if opening notes time-out/notes does not require reopen
	0 if notes not found in directory
	1 if notes sucessfully opened

	#Code:
	noteStatus = runNotes(0)
	notesInProcess = 1
	for i in range(0,10):
		if(notesInProcess):
			print("Configuring Notes, please wait......"+str(i)) 
			time.sleep(5)
		else:
			return runNotes(1)
		if (NOTES_PROCESS_NAME not in [psutil.Process(i).name() for i in psutil.pids()]):
			notesInProcess = 0 
	return -1
	"""


def openNotes():
	"""
	Alternative function
	
	"""
	noteStatus = runNotes(0)
	print("Configuring Notes, please wait......") 
	time.sleep(30)
	return runNotes(1)

def killPrintStation():
	ps_pid = 0
	for i in psutil.pids():
		if("PrintStation 2.0.exe" == psutil.Process(i).name()):
			ps_pid = i
			break
	psutil.Process(ps_pid).kill()	

def openPrintStation():
	print("Opening PrintStation 2.0...")
	if(PSTATION_PROCESS_NAME in [psutil.Process(i).name() for i in psutil.pids()]):
		print("PrintStation already runnning, restarting...")
		killPrintStation()
	try:
		subprocess.Popen( PSTATION_LOC )	
	except:
		print("Error: PrintStation not found...")
		return 0
	else:
		print("PrintStation is successfully running...")
		return 1