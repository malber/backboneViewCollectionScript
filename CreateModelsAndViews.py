#!/usr/bin/python

import sys
import os

tname = "NEWTEMPLATE"

def mkdirIfNotThere(x_dir):
	if not os.path.exists(x_dir):
	    os.makedirs(x_dir)

def ReplaceAndCreate(x_fileList, x_directory,x_newName):
	for iFname in x_fileList:
		outDir = "output/" + x_directory + "/"
		mkdirIfNotThere(outDir)

		with open(outDir + iFname.replace(tname,obaseName), "wt") as fout:
			with open("templates/" + iFname, "rt") as fin:
				for line in fin:
					fout.write(line.replace(tname, obaseName))

if(len(sys.argv) < 2):
	print 'Please run as'
	print 'python CreateModelsAndViews.py NAME_OF_UNDERLYING_MODEL'

obaseName = sys.argv[1]

# First create output if it does not exist
mkdirIfNotThere("output")

iFnameList = ["NEWTEMPLATE.js", "NEWTEMPLATECollection.js", "NEWTEMPLATEView.js"]
ReplaceAndCreate(iFnameList,"js",obaseName)

iFnameList = ["NEWTEMPLATECollection.json"]
ReplaceAndCreate(iFnameList,"models",obaseName)

iFnameList = ["NEWTEMPLATE.html"]
ReplaceAndCreate(iFnameList,"html",obaseName)

