#DownloadManagerExtensionSort.py
#File extension sorter
#Description: Parses through files in download folder and moves them into folders categorized by their file extension
#Author: Jordan Kam
#Github: github.com/jdkam
#Date Created: Dec 22, 2019
#Date Modified: Dec 22, 2019

import os
import shutil

#goTo Downloads folder
os.chdir('E:\Downloads')

#print(os.getcwd())

fExt = []

#Loop thru each file
for f in os.listdir():
	_, ext = os.path.splitext(f) #split name to get file extension 
	#fExt.append(ext)

	#If directory doensn't already exist, create one
	if not os.path.exists("\\Downloads\\" + ext):
		os.mkdir(ext)

	#Initialize the source and destination paths for moving the file
	source = "\\Downloads\\" + f
	dest = "\\Downloads\\" + ext
	
	#if it is a file, then move it to its respective directory
	if os.path.isfile(f):
		shutil.move(source, dest)
