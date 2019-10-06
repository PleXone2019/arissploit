from core.arissploit import *
import os
from core import colors
from scapy.all import *
from core import network_scanner
import random
from core import getpath
from core.setvar import setvar

conf = {
	"name": "mac_spoof",
	"version": "1.0",
	"shortdesc": "MAC spoof.",
	"author": "Entynetproject",
	"initdate": "9.3.2016",
	"lastmod": "3.1.2017",
	"apisupport": True,
	"needroot": 1,
	"dependencies": ["ethtool"]
}

# Custom commands
customcommands = {
	'scan': 'Scan network.',
	'random_mac': 'Generate random MAC.',
	'reset': 'End MAC spoof.'
}

# List of the variables
variables = OrderedDict((
	('fake_mac', ['02:a0:04:d3:00:11', 'Fake MAC.']),
	('interface', ['eth0', 'Network interface.']),
))

# Additional help notes
help_notes = colors.red+"This module will not work without root permissions, and ethtool!"+colors.end

# Additional notes to options
option_notes = colors.yellow+"You can generate fake_mac using 'random_mac' command.\n Use 'reset' command to end MAC spoof"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	xterm1 = "service network-manager stop"
	xterm2 = "ifconfig "+variables['interface'][0]+" hw ether "+variables['fake_mac'][0]
	xterm3 = "service network-manager start"
	printInfo("Status: starting MAC spoof...")
	os.system(xterm1)
	printInfo("Status: trying to set fake MAC address...")
	os.system(xterm2)
	os.system(xterm3)
	printSuccess("Status: done!")

def scan(args):
	network_scanner.scan()

def random_mac(args):
	mac = "f4:ac:c1:%02x:%02x:%02x" % (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)
	setvar('fake_mac', mac, variables)

def reset(args):
	command = ['ethtool', '-P', variables['interface'][0]]
	output = subprocess.Popen( command, stdout=subprocess.PIPE ).communicate()[0]
	realmac = str(output)
	realmac = realmac.replace("b'Permanent address: ", "")
	realmac = realmac.replace("'", "")
	realmac =  realmac[:-2]
	if not realmac:
		printError("Error!")
		return ModuleError("Error!")
	else:
		printInfo("RealMAC: "+realmac)
		xterm1a = "service network-manager stop"
		xterm2a = "ifconfig "+variables['interface'][0]+" hw ether "+realmac
		xterm3a = "service network-manager start"
		printInfo("Setting real MAC...")
		os.system(xterm1a)
		printInfo("Trying to set real MAC address...")
		os.system(xterm2a)
		os.system(xterm3a)
		printSuccess("Status: done!")
