

# Import python modules
import sys

# Import core modules
from core.module_manager import ModuleManager
from core import colors
from core import command_handler

shellface = "["+colors.bold+"arissploit"+colors.end+"]:"
mm = ModuleManager

def run():
	global shellface
	global mm

	ch = command_handler.Commandhandler(mm, False)

	while True:
		try:
			setFace()
			command = input(shellface+" ")

			ch.handle(command)
		except KeyboardInterrupt:
			if mm.moduleLoaded == 0:
				print()
				sys.exit(0)
			else:
				print()
				mm.moduleLoaded = 0
				mm.moduleName = ""
				print(colors.bold + colors.red + "Ctrl + C detected, going back..." + colors.end)

def setFace():
	global shellface
	global mm
	if mm.moduleLoaded == 0:
		shellface = "["+colors.bold+"arissploit"+colors.end+"]:"
	else:
		shellface = "["+colors.bold+"arissploit"+colors.end+"]"+"("+colors.red+mm.moduleName+colors.end+"):"
