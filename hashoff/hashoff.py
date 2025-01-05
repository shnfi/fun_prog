#!/bin/python3

import sys
import os
from time import sleep
from colorama import Fore as f
import argparse 
import hashlib




parser = argparse.ArgumentParser(description="Describtion: A Fast and Powerfull Cracking hashes Tool .")

parser.add_argument("-f", "--function", type=str, help="Specifies the hashing function .")
parser.add_argument("-e", "--encryptedFile", type=str, help="Name of the file that includes hashed text .")
parser.add_argument("-w", "--wordlist", type=str, help="Name of the wordlist .")
parser.add_argument("-o", "--output", type=str, help="Save result in a File .")

args = parser.parse_args()


def ClearTerminalScreen() :
      if sys.platform == "linux" or sys.platform == "darwin": 
            os.system("clear")
      elif sys.platform == "win32" : 
            os.system("cls")
      else :
            print(f.RED + " [✘] Undefined Operating System !")
            sleep(2)
            sys.exit()


def getCountOfLines(f) :
      count = 0
      for i in f : 
            count += 1
      
      return count


banner = f.WHITE + """
    ██░ ██  ▄▄▄       ██████   ██░ ██  ▒█████   ▒ ████▒ ▒ ████▒
  ▒▓██░ ██ ▒████▄   ▒██    ▒ ▒▓██░ ██ ▒██▒  ██▒▒▓██    ▒▓██    
  ░▒██▀▀██ ▒██  ▀█▄ ░ ▓██▄   ░▒██▀▀██ ▒██░  ██▒░▒████  ░▒████  
   ░▓█ ░██ ░██▄▄▄▄██  ▒   ██▒ ░▓█ ░██ ▒██   ██░░░▓█▒   ░░▓█▒   
   ░▓█▒░██▓▒▓█   ▓██▒██████▒▒ ░▓█▒░██▓░ ████▓▒░ ░▒█░    ░▒█░   
    ▒ ░░▒░▒░▒▒   ▓▒█▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒░▒░▒░   ▒ ░     ▒ ░   
    ▒ ░▒░ ░░ ░   ▒▒ ░ ░▒  ░ ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░       ░     
    ░  ░░ ░  ░   ▒  ░  ░  ░    ░  ░░ ░░ ░ ░ ▒    ░ ░     ░ ░   
    ░  ░  ░      ░        ░    ░  ░  ░    ░ ░                  
   v 0.1
   developed by kindkali

"""

if args.function != "md5" and args.function != "sha256" : 
      print(f.RED + "\n [!] Hash Function is not Supported . Supporting Functions = (md5, sha256)")
      sleep(1.5)
      sys.exit()
else :
      hashFunction = args.function

try : 
      hashedFile = open(f"{args.encryptedFile}", "r")
except FileNotFoundError : 
      print(f.RED + "\n [ERR] Encrypted File not Found!")
      sleep(1.5)
      sys.exit()
try : 
      wordlistFile = open(f"{args.wordlist}", "r")
except FileNotFoundError : 
      print(f.RED + "\n [ERR] Wordlist File not Found!")
      sleep(1.5)
      sys.exit()

if args.output : 
      outputFile = open(f"{args.output}.txt", "w")


hashedFileContent = hashedFile.read()
wordlistFileLength = 0
found = False
crackedAnswer = ""
hashedCrackedAnswer = ""
attemps = 0

rightColor = f.GREEN
wrongColor = f.RED
sign = ""

ClearTerminalScreen()
print(banner)


try :
      sleep(2)

      for word in wordlistFile : 
            if attemps % 20 == 0 : 
                  attemps += 1
                  sleep(0.15)
                  ClearTerminalScreen()
                  print(banner)
            else : 
                  attemps += 1

            if hashFunction == "md5" : 
                  hashed = hashlib.md5(word.encode())
            elif hashFunction == "sha256" :
                  hashed = hashlib.sha256(word.encode())
            
            if hashed.hexdigest() == hashedFileContent :
                  c = rightColor
                  sign = "✔"
            else :
                  c = wrongColor
                  sign = "✘"

            print(c + f" {sign} {word[:-1]}  -->  {hashed.hexdigest()}")

            sleep(0.06)

            if hashed.hexdigest() == hashedFileContent :
                  found = True
                  crackedAnswer = word
                  hashedCrackedAnswer = hashed.hexdigest()
                  wordlistFile.close()
                  hashedFile.close()
                  break


      wordlistFile = open(f"{args.wordlist}", "r")
      wordlistFileLength = getCountOfLines(wordlistFile)
      wordlistFile.close()


      sleep(2)

      ClearTerminalScreen()
      print(banner)

      print(f"""
      Process finished .

      CRACKED..................{rightColor + "YES" if found == True else wrongColor + "NO"}
      {f.WHITE + "HASHING FUNCTION"}.........{hashFunction.upper()}
      TOTAL ATTEMPS............{attemps} / {wordlistFileLength}
      POSSIBLE ANSWERS.........{"1" if found == True else "0"}
      ANSWERS..................{rightColor + crackedAnswer[:-1] if found == True else wrongColor + "Undefined"}
      {f.WHITE + "HASHED TARGET"}............{hashedFileContent}
      OUTPUT...................{"YES" if args.output else "NO"}
      """)

      if args.output : 
            outputFile.write(f"""Process finished .

CRACKED..................{"YES" if found == True else "NO"}
{"HASHING FUNCTION"}.........{hashFunction.upper()}
TOTAL ATTEMPS............{attemps} / {wordlistFileLength}
POSSIBLE ANSWERS.........{"1" if found == True else "0"}
ANSWERS..................{crackedAnswer[:-1] if found == True else "Undefined"}
{"HASHED TARGET"}............{hashedFileContent}
""")
            outputFile.close()

      sleep(5)
      sys.exit()
except KeyboardInterrupt :
      print(f.RED + "\n Quiting...")
      sleep(1.5)
      sys.exit()