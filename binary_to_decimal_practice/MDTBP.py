from time import sleep
from sys import exit
from os import system
from math import floor
from random import randint

system("clear")

def binaryConvertion(dec) :
	_dec = dec
	dividingCount = 0

	while dec != 1 :
		dec /= 2
		dec = floor(dec)
		dividingCount += 1

	dividingCount += 1

	binaryVal = ""

	for i in range(dividingCount) :
		if _dec % 2 == 0 :
			_dec /= 2
			binaryVal += "0"
		else :
			_dec /= 2
			_dec = floor(_dec)
			binaryVal += "1"

	if len(binaryVal) != 8 :
		binaryVal += "0" * (8 - len(binaryVal))

	reversedBinaryVal = ""

	x = 7

	for i in range(8) :
		reversedBinaryVal +=  binaryVal[x]
		x -= 1

	return reversedBinaryVal

print("Choose your practice :\n\n1) Binary to Decimal\n2) Decimal to Binary\n")

answer = input("[1-2]> ")
decimalNumbers = [i for i in range(128)]

if answer == "1" :
	attemps = 1

	dec = decimalNumbers[randint(0, len(decimalNumbers))]
	binary = binaryConvertion(dec)

	system("clear")

	print(f"Binary: {binary}\n")

	guess = input(f"[DECIMAL]-[{attemps}]> ")

	while guess != str(dec) :
		attemps += 1
		guess = input(f"[DECIMAL]-[{attemps}]> ")

	print(f"\nCORRECT!\nAttemps: {attemps}\n{binary} = {dec}\n")

elif answer == "2" :
	attemps = 1

	dec = decimalNumbers[randint(0, len(decimalNumbers))]
	binary = binaryConvertion(dec)

	system("clear")

	print(f"Decimal: {dec}\n")

	guess = input(f"[BINARY]-[{attemps}]> ")

	while guess != binary :
		attemps += 1
		guess = input(f"[BINARY]-[{attemps}]> ")

	print(f"\nCORRECT!\nAttemps: {attemps}\n{dec} = {binary}\n")

else :
	print("[ER] Invalid choice!")
	sleep(2)
	exit()
