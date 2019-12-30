# Libraries
from datetime import datetime
import pyttsx3

# Init engine and ctime and set properties
now = datetime.now()
ctime = now.strftime("%H:%M:%S")
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)

# Queue up starting text and run
engine.say("New Years Countdown active")
engine.runAndWait()

# Time check loop
while True:
	# Code left over from debugging, not needed.
	# print(ctime)
	now = datetime.now()
	ctime = now.strftime("%H:%M:%S")
	if ctime == "23:59:55":
		engine.say("5")
		engine.say("4")
		engine.say("3")
		engine.say("2")
		engine.say("1")
		engine.runAndWait()
	if ctime == "00:00:00":
		engine.say("HAPPY NEW YEAR!")
		engine.runAndWait()
		exit()
