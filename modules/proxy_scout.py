import sys
from core import colors
import urllib.request
import socket
from core.arissploit import *
import http.client
import re

conf = {
	"name": "proxy_scout",
	"version": "1.0",
	"shortdesc": "Verify http proxy.",
	"author": "Entynetproject",
	"initdate": "19.5.2016",
	"lastmod": "29.12.2016",
	"apisupport": False

}

# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.2', 'Target address.']),
	('port', ['80', 'Target port.']),
	('timeout', ['1', 'Timeout (default: 1).']),
	('port_range', ['1-100000', 'Port range (default: 1-100000).']),
	('use_range', ['0', 'Scan port range (1=yes/0=no).']),
	('scan_common', ['0', 'Scan commonly used ports (1=yes/0=no).']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	commonports = ['80', '8080', '8888', '25', '3128', '8003', '9529', '8088', '8118', '4624', '9090', '82', '8090', '5555', '81', '7004', '9797', '7777', '8998', '9999', '10200']
	variables['target'][0] = variables['target'][0].replace("http://", "").replace("https://", "")
	if variables['target'][0] == 'google.com':
		printError('Not valid address!')
		return
	try:
		try:
			socket.setdefaulttimeout(int(variables['timeout'][0]))
		except ValueError:
			printError('Not valid timeout!')
			return
		if variables['use_range'][0] != '1' and variables['scan_common'][0] != '1':
			proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+variables['port'][0]})
			opener = urllib.request.build_opener(proxy_support)
			urllib.request.install_opener(opener)

			html = urllib.request.urlopen("http://www.google.com").read()
			printSuccess('Proxy server detected.')
		if variables['scan_common'][0] == '1':
			for port in commonports:
				try:
					status = colors.yellow+'[*] Scanning port: '+ port+colors.end
					sys.stdout.write("\r%s" % status)
					sys.stdout.flush()
					proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+port})
					opener = urllib.request.build_opener(proxy_support)
					urllib.request.install_opener(opener)

					html = urllib.request.urlopen("http://www.google.com").read()
					print(' :'+colors.green+' proxy detected.'+colors.end)

				except http.client.BadStatusLine:
					printSuccess('\nProxy server detected.')
					break

				except urllib.error.URLError:
					pass
				
				except socket.timeout:
					pass
				
				except ConnectionResetError:
					print(' :'+colors.green+' proxy detected.'+colors.end)
			printSuccess('\ndone')

		if variables['use_range'][0] == '1':
			ports = re.sub("-", " ",  variables['port_range'][0]).split()
			for port in range(int(ports[0]), int(ports[1])):
				try:
					status = colors.yellow+'[*] Scanning port: '+ str(port)+colors.end
					sys.stdout.write("\r%s" % status)
					sys.stdout.flush()
					proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+str(port)})
					opener = urllib.request.build_opener(proxy_support)
					urllib.request.install_opener(opener)

					html = urllib.request.urlopen("http://www.google.com").read()
					print(' :'+colors.green+' proxy detected.'+colors.end)

				except http.client.BadStatusLine:
					printSuccess('\nProxy server detected.')
					break

				except urllib.error.URLError:
					pass
				
				except socket.timeout:
					pass
				
				except ConnectionResetError:
					print(' :'+colors.green+' proxy detected.'+colors.end)
			printSuccess('\nDone.')

	except http.client.BadStatusLine:
		printSuccess('Proxy server detected.')

	except urllib.error.URLError:
		printError('URLError!')
	
	except socket.timeout:
		printError('Timeout!')
	
	except ConnectionResetError:
		printSuccess('Proxy detected.')
