"""
MIT License

Copyright (c) 2025 Que

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED. 1nstagram made this <3 TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHERLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import colorama
from colored import fg, attr
from colorama import Fore, Back, Style, init
import requests
from time import sleep
import os
import os.path
from requests.api import options
import sys
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)


def menu():
    print(f"""{Fore.WHITE}
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                                 
     {Fore.LIGHTYELLOW_EX}Made by 1nstagram 
     https://discord.gg/dt5AfMdBC5{Fore.RESET}{Fore.LIGHTYELLOW_EX}
    ╔═════════════════════════╗
    ║[1] > Start Server Lookup║
    ╠═════════════════════════╣
    ║[2] > Join Discord       ║
    ╠═════════════════════════╣
    ║[3] > Exit               ║
    ╚═════════════════════════╝
""")
menu()

option = int(input(f"{Fore.WHITE} [>] {Fore.RESET}"))


def fetch_data():
        menu()
if option == 1:
        sleep(1)
 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{Fore.WHITE}

███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                    
{Fore.LIGHTYELLOW_EX}SHARE THIS WITH YOUR FRIENDS AND FOLLOW MY GITHUB! <3
https://discord.gg/dt5AfMdBC5{Fore.RESET}{Fore.LIGHTYELLOW_EX}
""")

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n{Fore.WHITE}[>] Token: ")
        }

        guildId = input(f"\n{Fore.LIGHTRED_EX} Enter Guild ID. [>] ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""{Fore.LIGHTBLUE_EX}
 Guild/Server | Name > {response['name']} 
 Guild/Server | ID > {response['id']}
 Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
 Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
 Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
 Guild/Server | Owner ID > {response['owner_id']}
 Guild/Server | Region > {response['region']}
""")
        sleep(10)
        exit()

elif option == 2:
    print(f"{Fore.LIGHTGREEN_EX}Redirecting in 3 Seconds...")
    sleep(3)
    webbrowser.open_new('https://discord.gg/dt5AfMdBC5')
    sleep(2)
    print(f"{Fore.RED}Bye!!")
    sleep(2)
    exit()
elif option == 98:
    sleep(1)
    print(f"{Fore.LIGHTGREEN_EX}Bye!")
    sleep(0.5)
    exit()
if __name__ == '__main__':
        fetch_data()