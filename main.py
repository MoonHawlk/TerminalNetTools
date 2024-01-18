# Project: TerminalNetTools
# Name: Filipe Moreno
# Start Date: 22-12-23
# Version: 0.0.2
# Language: PT-Br
# Orinal Repo:
# Active maintenance: Yes

# Default Packages
import platform

# Source Folders Packages
from src.funcMenu import *
from src.funcMacOS import *
from src.funcWin import *

# System Info
menuOS = {
    "Darwin":"MacOS",
    "Windows":"Windows",
    "Linux":"Linux"
}
os = platform.system()
if os in menuOS:
     print("==========================================================")
     print(f"Seu sistema operacional é:{menuOS[os]}                   ")
     print("==========================================================")
else:
     print("==========================================================")
     print(f"Sistema Operacional não reconhecido                      ")
     print("==========================================================")

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

# Main variables
choice = str()

# Mapping of Options
menuOptions = {
     "1":getIpConfig,
     "2":getPublicIP,
     "3":getOpenPorts,
     "4":getPing,
     "5":getInfoDns,
     "6":getRoutingTable,
     "11":clear_screen,
     "0":exit
}

# Choices state
while(1):

     menu()
     choice = str(input().lower())
     if choice in menuOptions:
        menuOptions[choice]()

     else:
        menuErro()