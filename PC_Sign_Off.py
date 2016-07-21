"""
PR_Sign_Off.py

Created by Bill X Zhang
Email: xiaoyan.zhang@nyu.edu
All rights not reserved. (LOL Jk) All rights reserved!

Edit with: Python 3.4.4

Purpose: Initializing preparation for PwC FY17 PC Replacement Sign-off procedure.

TODOs:
	Fix printstation windows process error
"""

import openEXEs
import os, time

#PATH = "C:\\Users\\Bill X Zhang\\Desktop\\SignOff0.2\\exe.win-amd64-3.4\\count\\sizeAndCount.exe"
COUNT_PATH = "%cd%\\count\\sizeAndCount.exe"
#USERNAME = getpass.getuser()

"""
def printStats(username):	
	print("AD Username: "+username)
	print("...............Migrated Data Stats..............")
	sizeAndCount.printSizeAndCount(username)
	print("================================================")
"""

def main():
	print("Starting Sign-off procedure preparation...")
	print("================================================")
	print("Calling file size calculator script (in a new window)...")
	os.system('start cmd /c "'+COUNT_PATH+'"')
	print("================================================")
	auraStatus = openEXEs.openAura()
	print("================================================")
	notesStatus = openEXEs.openNotes()
	if(notesStatus==1):
		print("Notes is successfully running...")
	elif(notesStatus==-1):
		print("Notes already running...")
	else:
		print("Error: Notes not found...")
	print("================================================")
	#printStats(USERNAME)

""" ERROR TO BE FIXED HERE """

	pstationStatus = openEXEs.openPrintStation()
	print("================================================")

	print("Finished...")
	print("This window will be closed automatically in 5 seconds...")
	print("================================================")
	time.sleep(5)
	#os.system("pause")


main()