# Import python modules

import sys
import os
import imp
import traceback
import curses
import time
import importlib
import glob

# Import getpath for lib path
from core import getpath

# Append lib path
sys.path.append(getpath.lib())

# Import core modules

from core import helptable
from core import helpin
from core import info
from core import colors
from core import moduleop
from prettytable import PrettyTable
import core.cowsay
import core.matrix
import core.sky
from core.hftest import check_module
from core import update
from core import mscop
from core import value_holder
from core import moddbparser
from core.messages import *
from core.apistatus import *

# Import exceptions
from core.exceptions import UnknownCommand
from core.exceptions import ModuleNotFound
from core.exceptions import VariableError

class Cmethods:

	# Module manager object

	mm = None
	modadd = None

	# Init

	def __init__(self, mmi):
		self.mm = mmi

	# Module custom commands

	def mcu(self, command):
		try:
			if command[0] in self.modadd.customcommands.keys():
				call = getattr(self.modadd, command[0])
				try:
					return call(command[1:])
				except Exception as e:
					print(colors.red+"Unexpected error in module:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
					if api.enabled == True:
						raise
			else:
				raise UnknownCommand("Unknown command!")
		except AttributeError:
			raise UnknownCommand("Unknown command!")

	# Built in commands

	def exit(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			sys.exit()

	def clear(self, args):
		if len(args) != 0 and args[0] == "tmp":
			mscop.clear_tmp()
		else:
			sys.stderr.write("\x1b[2J\x1b[H")

	def os(self, args):
		CYAN = '\033[1;34m'
		ENDL = '\033[0m'
		os.system(' '.join(args))

	def help(self, args):
		print("")
		if self.mm.moduleLoaded == 0:
			print(helptable.generateTable(helpin.commands))
		else:
			try: 
				print(helptable.generatemTable(helpin.mcommands, self.modadd.customcommands))
			except AttributeError:
				print(helptable.generateTable(helpin.mcommands))
			try:
				print('\n',self.modadd.help_notes,'\n')
			except AttributeError:
				pass
		print("")

	def version(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
			except:
				print(colors.red+"Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			print("Arissploit Framework " + info.version + " " + info.codename)

	def ifconfig(self, args):
		os.system("ifconfig"+" "+' '.join(args))

	def scan(self, args):
		network_scanner = importlib.import_module("core.network_scanner")
		network_scanner.scan()
		del network_scanner

	def use(self, args):
		init = False
		if "modules."+args[0] not in sys.modules:
			init = True

		if self.mm.moduleLoaded == 0:
			try:
				self.modadd = importlib.import_module("modules."+args[0])
				self.mm.moduleLoaded = 1
				self.mm.setName(self.modadd.conf["name"])
				try:
					print(self.modadd.conf["message"])
				except KeyError:
					pass
				try:
					if self.modadd.conf["outdated"] == 1:
						printWarning("This module is outdated and might not be working!")
				except KeyError:
					pass
				try:
					if self.modadd.conf["needroot"] == 1:
						if not os.geteuid() == 0:
							printWarning("This module requires root permissions for full functionality!")
				except KeyError:
					pass
				if init == True:
					try:
						self.modadd.init()
					except AttributeError:
						pass
			except ImportError:
				print(colors.red + "Module not found!" + colors.end)
				raise ModuleNotFound("Module not found!")
			except IndexError:
				print(colors.red + "Please enter module name!" + colors.end)
				raise ModuleNotFound("Module not found!")
			except:
				print(colors.red+"Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			raise UnknownCommand("Module in use!")

	def show(self, args):
		try:
			if args[0] == "modules":
				t = PrettyTable([colors.bold+'Modules:', ''+colors.end])
				t.align = 'l'
				t.valing = 'm'
				t.border = False
				xml = moddbparser.parsemoddb()
				root = xml[0]
				for category in root:
					if category.tag == "category":
						t.add_row(["", ""])
						t.add_row([colors.red+colors.uline+category.attrib["name"]+colors.end, colors.red+colors.uline+"Description"+colors.end])

					for item in category:
						if item.tag == "module":
							for child in item:
								if child.tag == "shortdesc":
									t.add_row([item.attrib["name"], child.text])
									break
				print("")
				print(t)
				print("")

			elif args[0] == "options" and self.mm.moduleLoaded == 1:
				try:
					moduleop.printoptions(self.modadd)
				except:
					print(colors.red+"Unexpected error in module:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
					if api.enabled == True:
						raise
			else:
				raise UnknownCommand("Module not loaded or unknown command!")
		except IndexError:
			raise UnknownCommand("Unknown command!")

	def back(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			raise UnknownCommand("Unknown command!")

	def reload(self, args):
		try:
			if self.mm.moduleLoaded == 0:
				try:
					mod = "modules."+args[0]
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print (colors.bold+"Module "+ args[0] +" reloaded"+colors.end)
					else:
						importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print(colors.bold+"Module "+ args[0] +" imported"+colors.end)

				except IndexError:
					print (colors.red+"Please enter module's name"+colors.end)
			else:
				try:
					mod = "modules."+args[0]
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass				
						print (colors.bold+"Module "+ args[0] +" reloaded"+colors.end)
					else:
						importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print(colors.bold+"Module "+ self.mm.moduleName +" reloaded"+colors.end)
				except IndexError:
					mod = "modules."+self.mm.moduleName
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print (colors.bold+"Module "+ self.mm.moduleName +" reloaded"+colors.end)

					else:
						modadd = importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print(colors.bold+"Module "+ self.mm.moduleName +" reloaded"+colors.end)
		except:
			print(colors.red+"Faced unexpected error during reimporting:\n")
			traceback.print_exc()
			print(colors.end)
			if api.enabled == True:
				raise

	def run(self, args):

		if self.mm.moduleLoaded == 1:
			try:
				return self.modadd.run()

			except KeyboardInterrupt:
				print(colors.red+"Module terminated!"+colors.end)
			except PermissionError:
				printError("Permission denied!")
				return "[err] Permission denied!"
			except:
				print(colors.red+"Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			raise UnknownCommand("Module not loaded!")

	def set(self, args):
		try:
			self.modadd.variables[args[0]][0] = args[1]
			print(colors.bold+args[0] +" => "+ str(args[1]) + colors.end)

		except (NameError, KeyError):
			print(colors.red + "Option not found!" + colors.end)
			raise VariableError("Option not found!")
		except IndexError:
			print(colors.red + "Please enter variable's value" + colors.end)
			raise VariableError("No value!")
		except:
			print(colors.red+"Unexpected error in module:\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)
			if api.enabled == True:
				raise

	def new(self, args):
		try:
			if args[0] == "module":
				try:
					completeName = os.path.join(getpath.modules(), args[1]+".py")
					if os.path.exists(completeName):
						print(colors.red+"Module already exists!"+colors.end)

					else:
						mfile = open(completeName, 'w')
						template = os.path.join('core', 'module_template')
						f = open(template, 'r')
						template_contents = f.readlines()
						template_contents[5] = "	\"name\": \""+args[1]+"\", # Module's name (should be same as file name)\n"
						template_contents[11] = "	\"initdate\": \""+(time.strftime("%d.%m.%Y"))+"\", # Initial date\n"
						template_contents[12] = "	\"lastmod\": \""+(time.strftime("%d.%m.%Y"))+"\", # Last modification\n"
						mfile.writelines(template_contents)
						mfile.close()
						print(colors.bold+"Module "+ args[1] +".py" +" saved to ./modules"+colors.end)

				except IndexError:
					print(colors.red + "Please enter module name!" + colors.end)

				except PermissionError:
					print(colors.red + "Error: permission denied!" + colors.end)

				except IOError:
					print(colors.red + "Something went wrong!" + colors.end)

			else:
				raise UnknownCommand("Unknown command!")
		except IndexError:
			raise UnknownCommand("Unkown command!")

	def check(self, args):
		try:
			if args[0] == "module":
				try:
					self.modadd = importlib.import_module("modules."+args[1])
					print(colors.green+"module found"+colors.end)
					check_module(self.modadd)
					print(colors.green+"\ntest passed"+colors.end)

				except IndexError:
					print(colors.red + "Please enter module name!"+ colors.end)

				except ImportError:
					print(colors.red+"Error: module not found!"+colors.end)

				except:
					print(colors.red + "error:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
			else:
				raise UnknownCommand("Unknown command!")
		except IndexError:
			raise UnknownCommand("Unkown command!")

	def matrix(self, args):
		try:
			core.matrix.main()
		except KeyboardInterrupt:
			curses.endwin()
			curses.curs_set(1)
			curses.reset_shell_mode()
			curses.echo()

	def cowsay(self, args):
		try:
			message = ' '.join(args)
			print(core.cowsay.cowsay(message))
			return
		except ValueError:
			print(core.cowsay.cowsay("Arissploit Framework"))

	def make(self, args):
		try:
			if args[0] == "exit":
				sys.exit(0)
			else:
				raise UnknownCommand("Unkown command!")
		except IndexError:
			raise UnknownCommand("Unkown command!")

	def sky(self, args):
		core.sky.main()

	def update(self, args):
		if update.check_for_updates() == True:
			try:
				update.update()
			except PermissionError:
				printError("Permission denied!")

			except Exception as error:
				printError(str(error))

	def loaded(self, args):
		print(sys.modules.keys())

	def list(self, args):
		if args[0] == "dependencies":
			if self.mm.moduleLoaded == 0:
				modules = glob.glob(getpath.modules()+"*.py")
				dependencies = []
				for module in modules:
					try:
						modadd = importlib.import_module("modules."+os.path.basename(module).replace(".py", ""))
						for dep in modadd.conf["dependencies"]:
							if dep not in dependencies:
								dependencies.append(dep)
					except ImportError:
						print(colors.red+"import error: "+os.path.basename(module).replace(".py", "")+colors.end)
						break
					except KeyError:
						pass
				for dep in dependencies:
					print(dep)
			else:
				try:
					for dep in self.modadd.conf["dependencies"]:
						print(dep)
				except KeyError:
					printInfo("This module doesn't require any dependencies!")
		else:
			raise UnknownCommand("Unknown command!")

	def init(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				self.modadd.init()
				print("Module initialized!")
			except AttributeError:
				print("This module doesn't have init function!")
		else:
			raise UnknownCommand("Unknown command!")

	def redb(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				moduleop.addtodb(self.modadd)
			except PermissionError:
				print(colors.red+"Error: permission denied!"+colors.end)
			except KeyboardInterrupt:
				print()
			except:
				print(colors.red+"Faced unexpected:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise

		else:
			answer = input("Do you want to update whole database [yes/no]? ")
			if answer == "yes" or answer == "y":
				try:
					modules = glob.glob(getpath.modules()+"*.py")
					for module in modules:
						module = module.replace(getpath.modules(), '').replace('.py', '')
						if module != '__init__' and module != "test":
							modadd = importlib.import_module("modules."+module)
							moduleop.addtodb(modadd)
				except PermissionError:
					print(colors.red+"Error: permission denied!"+colors.end)
				except KeyboardInterrupt:
					print()
				except:
					print(colors.red+"Faced unexpected:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
					if api.enabled == True:
						raise
