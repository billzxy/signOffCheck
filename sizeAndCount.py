"""
sizeAndCount.py

Created by Bill X Zhang
Email: xiaoyan.zhang@nyu.edu
All rights not reserved. (LOL Jk) All rights reserved!

Purpose: Count files in and calculate size of a folder

"""
import os
from os.path import join, getsize

def getDirSizeAndCount(directory):  
    size = 0 
    count = 0
    for root, dirs, files in os.walk(directory):
    	for name in files:
    		#size+=float(getsize(join(root,name)))
    		count+=1
    	#size += float(sum([getsize(join(root, name)) for name in files]) )
    	
    return size, count

def printSizeAndCount(username):
	"""
	Documents, Notes, Desktop, Favorites
	"""
	size, count = getDirSizeAndCount(r'C:\\Users\\%s\\Documents'%username )  
	if(size<1073741824):
		print("My Documents		Size: %.2f MBytes, 	File counts: %i" % (size/1024/1024, count))
	else:
		print("My Documents		Size: %.2f GBytes, 	File counts: %i" % (size/1073741824, count))
	size, count = getDirSizeAndCount(r'C:\\Users\\Public\\Lotus\\Notes\\Data' )  
	if(size<1073741824):
		print("Notes Data		Size: %.2f MBytes, 	File counts: %i" % (size/1024/1024, count))
	else:
		print("Notes Data		Size: %.2f GBytes, 	File counts: %i" % (size/1073741824, count))
	size, count = getDirSizeAndCount(r'C:\\Users\\%s\\Desktop'%username )  
	if(size<1073741824):
		print("Desktop			Size: %.2f MBytes, 	File counts: %i" % (size/1024/1024, count))
	else:
		print("Desktop			Size: %.2f GBytes, 	File counts: %i" % (size/1073741824, count))
	size, count = getDirSizeAndCount(r'C:\\Users\\%s\\Favorites'%username )  
	print("Favorites		Size: %.2f Bytes, 	File counts: %i" % (size, count))

