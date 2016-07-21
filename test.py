import subprocess, psutil, os, signal, sys
from os.path import join, getsize
def run():
	print ("Opening Aura v6 Navigator")
	try:
		subprocess.Popen( 'C:\\Program Files (x86)\\IBM\Lotus\\Notes\\notes.exe')
	except:
		print ("Error: Aura v6 Navigator not found...")
		return 0
	print ("Aura is successfully running...")
	return 1

def killps():
	ps_pid = 0
	for i in psutil.pids():
		if("PrintStation 2.0.exe" == psutil.Process(i).name()):
			ps_pid = i
			break

	psutil.Process(ps_pid).kill()


def runUnicodeDir(directory):  
    size = 0 
    count = 0
    for root, dirs, files in os.walk(directory):
    	for name in files:
    		size+=float(getsize(join(root,name)))
    		count+=1
    	size += float(sum([getsize(join(root, name)) for name in files]) )
    	
    print (size, count)

#subprocess.Popen("C:\\Program Files\\PrintStation 2.0\\PrintStation 2.0.exe")

try:
	if( "PrintStation 2.0.exe" in [psutil.Process(i).name() for i in psutil.pids()]):
		print("PrintStation already runnning, restarting...")
		print("No err.")
	print("IDK..")
except OSError as err:
		print(err)