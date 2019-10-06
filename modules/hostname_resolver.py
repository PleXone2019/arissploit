from core.arissploit import *
import socket

conf = {
	"name": "hostname_resolver",
	"version": "1.0",
	"shortdesc": "Resolve hostname using ip.",
	"author": "Entynetproject",
	"initdate": "9.5.2016",
	"lastmod": "3.1.2017",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.1', 'Target ip address.']),
))

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'][0])
		printSuccess("Resolved hostname: "+ querly[0])
		return querly[0]
	except(socket.herror):
		printError("Unknown host!")
		return ModuleError("Unknown host!")
	except(socket.gaierror):
		printError("Name or service not known!")
		return ModuleError("Name or service not known!")
