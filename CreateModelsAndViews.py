#!/usr/bin/python

import sys

tname = "NEWTEMPLATE"

def ReplaceAndCreate(x_fileList, x_directory,x_newName):

	for iFname in x_fileList:
		with open("output/" + x_directory + "/" + iFname.replace(tname,obaseName), "wt") as fout:
			with open("templates/" + iFname, "rt") as fin:
				for line in fin:
					fout.write(line.replace(tname, obaseName))

if(len(sys.argv) < 2):
	print 'Please run as'
	print 'python CreateModelsAndViews.py NAME_OF_UNDERLYING_MODEL'

obaseName = sys.argv[1]

iFnameList = ["NEWTEMPLATE.js", "NEWTEMPLATECollection.js"]
ReplaceAndCreate(iFnameList,"js",obaseName)

iFnameList = ["NEWTEMPLATECollection.json"]
ReplaceAndCreate(iFnameList,"models",obaseName)

