"""
PR_Sign_Off.py

Created by Bill X Zhang
Email: xiaoyan.zhang@nyu.edu
All rights not reserved. (LOL Jk) All rights reserved!

Purpose: Initializing preparation for PwC FY17 PC Replacement Sign-off procedure.
"""

import sizeAndCount, openEXEs
import os, getpass

USERNAME = getpass.getuser()


def printStats(username):	
	print "AD Username: "+username
	print "...............Migrated Data Stats.............."
	sizeAndCount.printSizeAndCount(username)
	print "================================================"

def main():
	print "Starting Sign-off procedure preparation..."
	auraStatus = openEXEs.openAura()
	print "================================================"
	notesStatus = openEXEs.openNotes()
	if(notesStatus==1):
		print "Notes is successfully running..."
	elif(notesStatus==-1):
		print "Notes already running..."
	else:
		print "Error: Notes not found..."
	print "================================================"
	printStats(USERNAME)

	pstationStatus = openEXEs.openPrintStation()
	print "================================================"

	raw_input("Finished...")


main()