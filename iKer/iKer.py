import sys
import platform
import os
from time import sleep
from colorama import Fore as f
import subprocess




color1 = f.BLUE
color2 = f.WHITE
color3 = f.LIGHTGREEN_EX

x = ""

if sys.platform == "linux" or sys.platform == "win32": 
      x = str(subprocess.check_output("whoami", shell = True, text = True))
elif sys.platform == "darwin" : 
      x = str(subprocess.check_output("id -un", shell = True, text = True))
else :
      print(f.RED + " [✘] Undefined Operating System !")
      sleep(2)
      sys.exit()

username = x[:-1]


def ClearTerminalScreen() :
      if sys.platform == "linux" or sys.platform == "darwin": 
            os.system("clear")
      elif sys.platform == "win32" : 
            os.system("cls")
      else :
            print(f.RED + " [✘] Undefined Operating System !")
            sleep(2)
            sys.exit()


def PrintTheBanner(sec) : 
      print(color1 + """

   ██╗██╗  ██╗███████╗██████╗ 
   ██║██║ ██╔╝██╔════╝██╔══██╗
   ██║█████╔╝ █████╗  ██████╔╝
   ██║██╔═██╗ ██╔══╝  ██╔══██╗
   ██║██║  ██╗███████╗██║  ██║
   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")
      print("   Developed by " + "kindkali")
      print(color1 + "   v 0.1")
      print(f.LIGHTYELLOW_EX + """

   [!] For Informations that you don't Know yet, Enter "-" .
   [!] For Informations that are not Existed, Enter "None" .""")
      sleep(sec)
      print("")
      print("")


try :
      ClearTerminalScreen()
      PrintTheBanner(2)

      print(color3 + "  >->-> [Personality]")
      print(color1 + "")
      name = str(input(" [1] Victim's Name -> "))
      lastName = str(input(" [2] Victim's Last Name -> "))
      nickName = str(input(" [3] Victim's Nick Name -> "))
      age = str(input(" [4] Victim's Age (0-99) -> "))
      educations = str(input(" [5] Victim's Educations -> "))
      job = str(input(" [6] Victim's Job -> "))
      relationship = str(input(" [7] Victim's Relationship -> "))
      brother = str(input(" [8] Victim's Brother -> "))
      sister = str(input(" [9] Victim's Sister -> "))



      ClearTerminalScreen()
      PrintTheBanner(0)

      print(color3 + "  >->-> [Social Media]")
      print(color1 + "")
      email = str(input(" [1] Victim's Email (with domain) -> "))
      instagramID = str(input(" [2] Victim's Instagram ID -> "))
      phoneNumber = str(input(" [3] Victim's Phone Number (with country code) -> "))
      publicIP = str(input(" [4] Victim's Phublic IP Address -> "))
      mac = str(input(" [5] Victim's MAC Address -> "))



      ClearTerminalScreen()
      PrintTheBanner(0)

      print(color3 + "  >->-> [Environment]")
      print(color1 + "")
      homeAddress = str(input(" [1] Victim's Home Address -> "))
      jobAddress = str(input(" [2] Victim's Job Address -> "))
      nationality = str(input(" [3] Victim's Nationality -> "))
      ethnicity = str(input(" [4] Victim's Ethnicity -> "))


      ClearTerminalScreen()
      sleep(0.7)


      for i in range(15) :
            print(color1 + """
      [/] Creating files ...""")
            sleep(0.1)
            ClearTerminalScreen()
            print(color1 + """
      [-] Creating files ...""")
            sleep(0.1)
            ClearTerminalScreen()
            print(color1 + """
      [\] Creating files ...""")
            sleep(0.1)
            ClearTerminalScreen()


      if sys.platform == "linux" : 
            if os.path.exists(f"/home/{username}/Documents/iKer Documents") == False :
                  os.mkdir(f"/home/{username}/Documents/iKer Documents")
      elif sys.platform == "win32" : 
            if os.path.exists(f"C:/Documents/iKer Documents") == False :
                  os.mkdir(f"C:/Documents/iKer Documents")
      elif sys.platform == "darwin" :
            if os.path.exists(f"subfolder/Users/{username}/Documents/iKer Documents") == False :
                  os.mkdir(f"subfolder/Users/{username}/Documents/iKer Documents")
      else :
            print(f.RED + " [✘] Undefined Operating System !")
            sleep(2)
            sys.exit()


      try :
            if sys.platform == "linux" : 
                  document = open(f"/home/{username}/Documents/iKer Documents/{name.strip().title()} {lastName.strip().title()}.txt", "w")
            elif sys.platform == "win32" : 
                  document = open(f"C:/Documents/iKer Documents/{name.strip().title()} {lastName.strip().title()}.txt", "w")
            elif sys.platform == "darwin" :
                  document = open(f"subfolder/Users/{username}/Documents/iKer Documents/{name.strip().title()} {lastName.strip().title()}.txt", "w")
            else :
                  print(f.RED + " [✘] Undefined Operating System !")
                  sleep(2)
                  sys.exit()

            document.write(f"""
      iKer Document 

      {"-" * 45}

                  -< Personality >-
      Victim's Name              : {name.strip().title()}
      Victim's Last Name         : {lastName.strip().title()}
      Victim's Nick Name         : {nickName.strip().title()}
      Victim's Age               : {age.strip().title()}
      Victim's Educations        : {educations.strip().title()}
      Victim's Job               : {job.strip().title()}
      Victim's Relationship      : {relationship.strip().title()}
      Victim's Brother           : {brother.strip().title()}
      Victim's Sister            : {sister.strip().title()}

            -< Social Media >-
      Victim's Email             : {email.strip()}
      Victim's Instagram ID      : {instagramID.strip()}
      Victim's Phone Number      : {phoneNumber.strip().title()}
      Victim's Public IP Addre   : {publicIP.strip().title()}
      Victim's MAC Address       : {mac.strip().title()}

                  -< Environment >-
      Victim's Home Address      : {homeAddress.strip().title()}
      Victim's Job Address       : {jobAddress.strip().title()}
      Victim's Nationality       : {nationality.strip().title()}
      Victim's Ethnicity         : {ethnicity.strip().title()}
      """)
            document.close()
      except :
            print(f.RED + " [✘] Error while creating the document !")
            sleep(2)
            sys.exit()


      print(f.GREEN + """
      [✔] Files have been created successifuly !""")
      sleep(2.5)
      print(f.LIGHTYELLOW_EX + f"""
      [!] Documents location in Linux    --> /home/{username}/Documents/iKer Documents/
      [!] Documents location in Windows  --> C:/Documents/iKer Documents/
      [!] Documents location in MacOS    --> subfolder/Users/{username}/Documents/iKer Documents/
      """)
      sleep(7)
      sys.exit()
except KeyboardInterrupt : 
      print(f.RED + "\n Quiting ... ")
      sleep(1.5)
      sys.exit()