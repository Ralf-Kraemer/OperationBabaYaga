import random
import time
import dataloader
import BabaYaga

dataloader.loadNames()
dataloader.loadProviders()
dataloader.loadProxyList()
dataloader.loadNewsletters()
dataloader.loadUserAgents()

firstNames = dataloader.firstNames
lastNames = dataloader.lastNames
mailProviders = dataloader.mailProviders
proxyList = dataloader.proxyList
Newsletters = dataloader.Newsletters
userAgents = dataloader.userAgents

def pickRandomElement(x):
	y = len(x)
	z = random.randint(1, y)-1
	return x[z]

def runtime(n):
	i = 0;
	while i < n:
		curse = BabaYaga.prepare(
			pickRandomElement(firstNames),
			pickRandomElement(lastNames),
			pickRandomElement(mailProviders),
			pickRandomElement(proxyList),
			pickRandomElement(Newsletters),
			pickRandomElement(userAgents)
		)
		BabaYaga.cast(curse)
		time.sleep(random.random()*0.002*delayMultiplier)
		i+=1
		print(i)
	print("I've cast "+str(n)+" curses against the invading forces.")

print("0  O  0  O  0  O  0  O  0  O  0  O  0")
print(" 0  O  0  O  0  O  0  O  0  O  0  O  0")
print("  0  O  0  O  0  O  0  o  0  O  0  O  0")
print(" 0  O   0  O  0   O  0  O  0  O  0  O  0")
print("0  O  0  O  0   O  0  O  0  O  0  O  0")
print(" 0  O  0  O  0   O  0  O  o  O  0  O  0")
print("  0   O  0 O  0   0  O  0  0  O  0  O  0")
print(" 0  O  0  O  0  O  0  O  0  O  0  O  0")
print("0  O  0  O  0  O  0  O  o  O  0  O  0")
print(" 0  O  0   O  0  O  0  O  0  O  0  O  0")
print("  0  O  0  O  0   O  0   O  0  O  0  O  0")
print(" 0  O   0 O  0  O  0  O  0  o   0  O  0")
print("0   O  0  O   0  O   0   O  0  O  0  0  0")
print(" 0  O  0  O  0  O  0  O  0 O   0  o  O")
print("\n")
print("Privyet! I'm Baba Yaga, the 21st century witch.")
print("\n")
print("I have the ability to curse wannabe-emperors and their grunts.")
print("\n")
print("How many victims shall I hunt for you tonight?")

seq = int(input())

print("\nI usually wait a short while between my attacks, to stay under the radar.")
print("How long should I linger, on average, between curses? (In milliseconds)")

delayMultiplier = int(input())

runtime(seq)
