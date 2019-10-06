from core import colors
import http.client
from core.arissploit import *
import socket

conf = {
	"name": "webserver_scout",
	"version": "1.0",
	"shortdesc": "Get information from webserver.",
	"author": "Entynetproject",
	"initdate": "17.5.2016",
	"lastmod": "3.1.2017",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['google.com', 'Target address.']),
	('timeout', ['1', 'Timeout (default: 1).']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		try:
			socket.setdefaulttimeout(float(variables['timeout'][0]))
		except ValueError:
			printError('Invalid timeout!')
			return ModuleError("Invalid timeout!")
		conn = http.client.HTTPConnection(variables['target'][0])
		conn.request("HEAD","/index.html")
		res = conn.getresponse()
		results = res.getheaders()
		print('')
		for item in results:
			print(colors.yellow+item[0], item[1]+colors.end)
		print('')
		return results
	except http.client.InvalidURL:
		printError('Invalid URL!')
		return ("Invalid URL!")
	except socket.gaierror:
		printError('Name or service not known!')
		return ModuleError("Name or service not known!")
	except socket.timeout:
		printError('Timeout!')
		return ModuleError("Timeout!")
