import csv
import json

firstNames = []
lastNames = []
def loadNames():
	with open("data/names.csv") as namesFile:
		print("=== Opening names.csv ===")
		reader = csv.reader(namesFile)
		for row in reader:
			firstNames.append(row[0])
			lastNames.append(row[1])
			print(row)
		print("=== Names loaded. ===")

mailProviders = []
def loadProviders():
	with open("data/mailProviders.csv") as providersFile:
		print("=== Opening mailProviders.csv ===")
		reader = csv.reader(providersFile)
		for row in reader:
			mailProviders.append(row[0])
			print(row)
		print("=== Providers loaded. ===")
		
proxyList = []
def loadProxyList():
	with open("data/proxyList.csv") as proxyListFile:
		print("=== Opening proxyList.csv ===")
		reader = csv.reader(proxyListFile)
		for row in reader:
			proxyList.append(row[0])
			print(row)
		print("=== Proxy Servers loaded. ===")

Newsletters = []
def loadNewsletters():
	with open("data/Newsletters.json") as NewslettersFile:
		print("=== Opening Newsletters.json ===")
		jsonLoader = json.load(NewslettersFile)
		for obj in jsonLoader:
			Newsletters.append(obj)
			print(obj)
		print("=== Newsletters loaded. ===")

userAgents = []
def loadUserAgents():
	with open("data/userAgents.csv") as userAgentsFile:
		print("=== Opening userAgents.csv ===")
		reader = csv.reader(userAgentsFile)
		for row in reader:
			userAgents.append(row[0])
			print(row)
		print("=== User agents loaded. ===")