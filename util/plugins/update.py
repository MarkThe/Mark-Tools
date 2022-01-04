# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import os
import shutil
import re
import psutil

from tqdm import tqdm
from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore, Style

from util.plugins.common import *

def search_for_updates():
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    clear()
    setTitle("Hazard Nuker Checking For Updates. . .")
    for i in tqdm(range(100),
                    desc="Searching for updates. . .",
                    ascii=False, ncols=100):
                    sleep(0.003)
    r = requests.get("https://github.com/Rdimo/Hazard-Nuker/releases/latest", headers=header)
    clear()
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        setTitle("Hazard Nuker New Update Found!")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.LIGHTRED_EX}Looks like this Hazard Nuker {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.LIGHTRED_EX}'))

        if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .{Fore.RESET}")
            setTitle(f'Hazard Nuker Updating...')
            #if they are running hazard.exe
            if psutil.Process(os.getpid()).name() == 'HazardNuker.exe':
                try:
                    soup = BeautifulSoup(requests.get("https://github.com/Rdimo/Hazard-Nuker/releases", headers=header).text, 'html.parser')
                    for link in soup.find_all('a'):
                        if "releases/download" in str(link):
                            update_url = f"https://github.com/{link.get('href')}"
                    new_version = requests.get(update_url)
                    with open("HazardNuker.zip", 'wb')as zipfile:
                        zipfile.write(new_version.content)
                    with ZipFile("HazardNuker.zip", 'r') as filezip:
                        filezip.extractall()
                    os.remove("HazardNuker.zip")
                    cwd = os.getcwd()+'\\HazardNuker\\'
                    shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                    shutil.copyfile(cwd+'HazardNuker.exe', 'HazardNuker.exe')
                    shutil.copyfile(cwd+'README.md', 'README.md')                   
                    shutil.rmtree('HazardNuker')
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                    sleep(1)
                    os.startfile("HazardNuker.exe")
                    exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.LIGHTRED_EX}\nHazard Nuker-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)
            #if they are running hazard source code
            else:
                try:
                    new_version = requests.get("https://github.com/Rdimo/Hazard-Nuker/archive/refs/heads/master.zip")
                    with open("Hazard-Nuker-master.zip", 'wb')as zipfile:
                        zipfile.write(new_version.content)
                    with ZipFile("Hazard-Nuker-master.zip", 'r') as filezip:
                        filezip.extractall()
                    os.remove("Hazard-Nuker-master.zip")
                    cwd = os.getcwd()+'\\Hazard-Nuker-master'
                    shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                    shutil.rmtree(cwd)
                    setTitle('Hazard Nuker Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                    sleep(1)
                    os.startfile("run.bat")
                    exit()
                except Exception as err:
                    clear()
                    print(f"{Fore.LIGHTRED_EX}An error occured while Updating Hazard Nuker-{THIS_VERSION}\n\nIf this keeps occuring try and download it manually here github.com/Rdimo/Hazard-Nuker\n\n\"{err}\"")
                    sleep(7)

        else:
            input
            return