from core.arissploit import *
from scapy.all import *

conf = {
	"name": "arp_monitor", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Arp packet monitor.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "31.12.2016", # Initial date
	"lastmod": "31.12.2016", # Last modification
	"apisupport": False, # Api support
	"needroot": 1, # Alert user if root permissions not available (remove variable below if root permissions not needed)
}

# List of the variables
variables = OrderedDict((
	
))

# Additional notes to options
option_notes = "This module doesn't have any options."

# Simple changelog
changelog = "Version 1.0:\nrelease"

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		return "Request: " + pkt[ARP].psrc + " is asking about " + pkt[ARP].pdst
	if pkt[ARP].op == 2: #is-at (response)
		return "*Response: " + pkt[ARP].hwsrc + " has address " + pkt[ARP].psrc

# Run function
def run():
	printInfo("Starting arp monitor...")
	printInfo("Ctrl + C to end.")
	print(sniff(prn=arp_display, filter="arp", store=0))
	printInfo("Monitoring ended!")
