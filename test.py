import subprocess, psutil, os, signal
def run():
	print "Opening Aura v6 Navigator"
	try:
		subprocess.Popen( 'C:\\Program Files (x86)\\IBM\Lotus\\Notes\\notes.exe')
	except:
		print "Error: Aura v6 Navigator not found..."
		return 0
	print "Aura is successfully running..."
	return 1

def killps():
	ps_pid = 0
	for i in psutil.pids():
		if("PrintStation 2.0.exe" == psutil.Process(i).name()):
			ps_pid = i
			break

	psutil.Process(ps_pid).kill()

def logging():
	os.system('echo %s>"\%userprofile\%\\Desktop\\signoff.log"' %(" "))

logging()
