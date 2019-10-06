from core.arissploit import *
from core import colors
import zipfile
import threading, queue
from core import getpath
from os.path import relpath
import sys

conf = {
	"name": "zip_cracker", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Zip file brute-force attack using dictionary.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "22.12.2016", # Initial date
	"lastmod": "3.1.2017",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("file", ["none", "Target zip file."]),
	("dict", ["none", "Dictionary of words."]),
	("tc", [8, "Thread count (int)."]),
	("exto", ["none", "Extract directory."])
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def init():
	variables["exto"][0] = relpath(getpath.tmp(), getpath.main_module())
	variables["dict"][0] = relpath(getpath.db() + "dazzlepod.txt", getpath.main_module())

class PwdHolder:
	pwd = None
	error = None
	kill = False

	def __init__(self):
		self.pwd = None
		self.error = None
		self.kill = False

	def reset():
		PwdHolder.pwd = None
		PwdHolder.error = None
		PwdHolder.kill = False

class Worker(threading.Thread):
	pwdh = None
	words = None
	def __init__(self, words, pwdh):
		self.pwdh = pwdh
		self.words = words
		threading.Thread.__init__(self)

	def run(self):
		try:
			zipf = zipfile.ZipFile(variables["file"][0])
		
		except FileNotFoundError:
			self.pwdh.error = "zip file not found"
			return
		for word in self.words:
			if self.pwdh.pwd != None:
				return
			elif self.pwdh.error != None:
				return
			elif self.pwdh.kill == True:
				return
			try:
				word = word.decode("utf-8").replace("\n", "")
				if word[0] == "#":
					continue
				#animline("trying password: "+word)
				zipf.extractall(variables["exto"][0], pwd=word.encode("utf-8"))
				self.pwdh.pwd = word
				return
			except RuntimeError:
				pass
			except zipfile.BadZipFile:
				pass

def run():
	try:
		wordlist = open(variables["dict"][0], "rb")
		printInfo("Reading word list...")
		words = wordlist.read().splitlines()
	except FileNotFoundError:
		printError("Word list not found!")
		return ModuleError("Word list not found!")
	printInfo("Brute-force attack started...")

	pwdh = PwdHolder
	pwdh.reset()

	try:
		u = int(variables["tc"][0])
	except TypeError:
		printError("Invalid thread count!")
		return ModuleError("Invalid thread count!")
	threads = []

	for i in range(variables["tc"][0]):
		t = Worker(words[i::u], pwdh)
		threads.append(t)
		t.start()
	printInfo("Now cracking...")
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		pwdh.kill = True
		printInfo("Brute-force attack terminated!")

	if pwdh.pwd != None:
		printSuccess("Password found: "+pwdh.pwd)
		return pwdh.pwd

	elif pwdh.error != None:
		printError(pwdh.error)
		return ModuleError(pwdh.error)
