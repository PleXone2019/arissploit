

# Python modules

import requests
import json
import os
from packaging import version
import urllib.request
from glob import glob
import shutil
import sys
import distutils.dir_util

# Core modules

from core import colors
from core import info
from core import getpath
from core import mscop

def check_for_updates():
	try:
		print(colors.green+"Checking for updates..."+colors.end)
		r = requests.get("https://api.github.com/repos/entynetproject/arissploit/releases/latest")
		if(r.ok):
			items = json.loads(r.text or r.content)
			rver = items['tag_name']

			if "beta" in rver and "alpha" in info.version:
				print(colors.green+"Update found!"+colors.end)
				return True 

			elif "beta" not in rver and "alpha" not in rver:
				if "beta" in info.version or "alpha" in info.version:
					print(colors.green+"Update found!"+colors.end)
					return True

			elif version.parse(rver) > version.parse(info.version):
				print(colors.green+"Update found!"+colors.end)
				return True

			else:
				print(colors.yellow+"Updates not found."+colors.end)
				return False
		else:
			print("error")
	except Exception as error:
		print(colors.red+"error: "+str(error)+colors.end)

def update():
	answer = input("Do you want to start update [yes/no]? ")

	if answer != "yes" and answer != "y":
		return


	url = "https://github.com/entynetproject/arissploit/tarball/master"
	print(colors.green+"Downloading..."+colors.end)

	u = urllib.request.urlopen(url)

	print(colors.green+"Clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"Writing..."+colors.end)

	f = open(getpath.tmp()+"update.tar.gz", "wb")
	f.write(u.read())
	f.close()

	print(colors.green+"Extracting..."+colors.end)
	os.system("tar -zxvf '"+getpath.tmp()+"update.tar.gz' -C '"+getpath.tmp()+"'")

	files = glob(getpath.tmp()+"*/")
	update_path = None

	for file in files:
		if "arissploit" in file and os.path.isfile(file) == False:
			update_path = file
			break

	if update_path == None:
		print(colors.red+"Error: update package not found!"+colors.end)
		return

	files = glob(update_path+"*")

	print(colors.green+"Installing update..."+colors.end)

	for file in files:

		file_name = file.replace(update_path, "")
		print(getpath.main()+file_name)

		if os.path.isfile(file):
			shutil.copyfile(file, getpath.main()+file_name)
		else:
			distutils.dir_util.copy_tree(file, getpath.main()+file_name)


	print(colors.green+"Clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"Update installed!"+colors.end)
	sys.exit()
