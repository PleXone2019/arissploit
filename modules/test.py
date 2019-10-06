from core.arissploit import *

# Info about the module

conf = {
	"name": "test", # Module's name (should be same as file's name)
	"version": "1.0", # Module version
	"shortdesc": "Only test.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "24.2.2016", # Initial date
	"lastmod": "29.12.2016",
	"apisupport": True, # Api support

	"message": "hello"
}

# List of the variables
variables = OrderedDict((
	("value", [0, "Description."]),
))

customcommands = {
	"test": "Test."
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(variables['value'][0])
	print(variables['value'][1])
	printWarning("Warning!")
	return variables

def test(args):
	return "Ok."
