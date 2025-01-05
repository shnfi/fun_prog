#!/bin/python3

import sys
import os
from time import sleep
from colorama import Fore



textWords = []

asciiTable = {
	"A" : 65,	"Q" : 81,	 "K" : 75,				"a" : 97,	"q" : 113,	 "k" : 107,				"0" : 48,
	"B" : 66,	"R" : 82,	 "L" : 76,				"b" : 98,	"r" : 114,	 "l" : 108,				"1" : 49,
	"C" : 67,	"S" : 83,	 "M" : 77,				"c" : 99,	"s" : 115,	 "m" : 109,				"2" : 50,
	"D" : 68,	"T" : 84,	 "N" : 78,				"d" : 100,	"t" : 116,	 "n" : 110,				"3" : 51,
	"E" : 69,	"U" : 85,	 "O" : 79,				"e" : 101,	"u" : 117,	 "o" : 111,				"4" : 52,
	"F" : 70,	"V" : 86,	 "P" : 80,				"f" : 102,	"v" : 118,	 "p" : 112,				"5" : 53,
	"G" : 71,	"W" : 87,							"g" : 103,	"w" : 119,							"6" : 54,
	"H" : 72, 	"X" : 88,							"h" : 104, 	"x" : 120,							"7" : 55,
	"I" : 73, 	"Y" : 89,							"i" : 105, 	"y" : 121,							"8" : 56,
	"J" : 74, 	"Z" : 90,							"j" : 106, 	"z" : 122,							"9" : 57,
}



if len(sys.argv) >= 2 :
	for w in sys.argv[1:] :
		textWords.append(w)
else : 
	print("[ERR] Invalid Count of Arguments!")
	sleep(2)
	sys.exit()


os.system("clear")
sleep(0.5)

print(Fore.LIGHTCYAN_EX + """

         __    _       _            
   _____/ /_  (_____  (_____  ____ _
  / ___/ __ \/ / __ \/ / __ \/ __ `/
 (__  / / / / / / / / / / / / /_/ / 
/____/_/ /_/_/_/ /_/_/_/ /_/\__, /  
                           /____/   
v 1.0
developed by kindkali

""")
print(Fore.LIGHTGREEN_EX + "")

sleep(0.5)

def HowManyTimesDevivdeByTwo(num) :
	count = 0
	while num > 1 :
		if num != 1 :
			num /= 2
			count += 1

	return count


for w in textWords : 
	for l in w : 
		numberInAscii = asciiTable[l]
		
		remains = []

		for i in range(HowManyTimesDevivdeByTwo(numberInAscii)) :
			remains.append(int(numberInAscii % 2))
			numberInAscii /= 2

		if len(remains) < 8 :
			remains.append(0)

		remains.reverse()

		text = ""

		for i in remains :
			text += str(remains[i])
		
		print(f"[{l}]  {text}")
		sleep(0.2)

	print(" ")

print("")
