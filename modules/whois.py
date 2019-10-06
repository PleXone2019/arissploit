from core.arissploit import *
import whois

conf = {
	"name": "whois", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Perform whois query.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "18.12.2016", # Initial date
	"lastmod": "29.12.2016",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	("target", ["google.com", "Target address."]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	# Run
	w = whois.whois(variables["target"][0])
	print(w)
	return w
