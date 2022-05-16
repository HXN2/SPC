import os
try:
    import requests
    import socket as s
    import webbrowser
    from sys import platform
    import colorama
    import ISS_Info

except ModuleNotFoundError:
    os.system("pip install ISS_Info")
    os.system("pip install requests")
    os.system("pip install socket")
    os.system("pip install webbrowser")
    os.system("pip install sys")
    os.system("pip install platform")
    os.system("pip install colorama")
    os.system("pip install Today")
    os.system("pip install Date")
    os.system("pip install os")
    os.system('cls' if os.name == 'nt' else 'clear')
else: 
    pass
import webbrowser
url = "https://t.me/HEXiN1K"
webbrowser.open(url)
from sys import platform
from colorama import *
import socket
import requests
from datetime import datetime

now = datetime.now()

current_time = now.strftime

name = socket.gethostname()

myHostName = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n===========================================================")
name = ("""\n                    Hello sir """ +name+Style.RESET_ALL)
print(name)

import datetime
e = datetime.datetime.now()
print (Fore.CYAN+"""\n                   Your Day is """+"%s/%s/%s" % (e.day, e.month, e.year))
print ("""\n                   The time is """+ "%s:%s:%s" % (e.hour, e.minute, e.second))

host = (Fore.WHITE+"""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)

api = "https://api.ipify.org/?format=json"
req = requests.get(api)
response = req.json()
a = response["ip"]

IP = ("""\n                Your Local iP is """+Fore.RED+a+Style.RESET_ALL)
print(IP)

v = (Fore.RED+"""\n                    Your iNFO PROXY is\n"""+Style.RESET_ALL)

print(v)
print(s)

print("\n===========================================================")

lib = input("""
\n  من صنع هيكسن انستجرام @hxn.py
\n  BY HEXiN INSTA @hxn.py
\n  tarafından yapılmış HEXiN Instagram @hxn.py
\n
===========================================================
\n   من صنع هيكسن تيليجرام @HEXiN1K
\n  BY HEXiN TELeGRaM @HEXiN1K
\n  Bir telgraf HEXiN oluşturun @HEXiN1K
\n ===========================================================
 
 [1] DOWNLOAD LiP & UPDATE . تنزيل وتحديث المكاتب

\n [2] SKiP DOWNLOAD & UPDATE LiP . تخطي تنزيل وتحديث المكاتب 

\n [+] Please Choice >> """)

if lib == "1":
    try:
        os.system('pip install ISS_Info')
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except:
        pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
import ISS_Info
from colorama import *
bn1 = (Fore.RED+"""
:'######::'########:::::'###:::::'######::'########:
'##... ##: ##.... ##:::'## ##:::'##... ##: ##.....::
 ##:::..:: ##:::: ##::'##:. ##:: ##:::..:: ##:::::::
. ######:: ########::'##:::. ##: ##::::::: ######:::
:..... ##: ##.....::: #########: ##::::::: ##...::::
'##::: ##: ##:::::::: ##.... ##: ##::: ##: ##:::::::
. ######:: ##:::::::: ##:::: ##:. ######:: ########:
:......:::..:::::::::..:::::..:::......:::........::
""")
print (bn1)
gg = input(Fore.YELLOW+" [=] Press Enter to continue : ")

if gg == '':
	nap = ISS_Info.iss_people_in_space()
	print(Fore.CYAN+" \n  Currently there {} astronauts in space:"
	.format(nap['number']))
for n in nap['people']:
	print("  Name: {} ('Craft: {}'))"
	.format(n['name'],n['craft']))

loc = ISS_Info.iss_current_loc()
print(" 📍The current location of the International Space Station: ",loc)

url = "https://instagram.com/hxn.py/"
webbrowser.open(url)
