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
    setTitle("Mark-Tool Checking For Updates. . .")
    for i in tqdm(range(100),
                    desc="Searching for updates. . .",
                    ascii=False, ncols=100):
                    sleep(0.003)
    r = requests.get("https://github.com/MarkThe/Mark-Tools/releases/latest", headers=header)
    clear()
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        setTitle("Mark-Tool New Update Found!")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.LIGHTRED_EX}Looks like this Mark-Tool {THIS_VERSION} is outdated '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.LIGHTRED_EX}'))

        if choice.upper() == 'Y':
            print(f"{Fore.WHITE}\nUpdating. . .{Fore.RESET}")
            setTitle(f'Mark-Tool Updating...')
            #if they are running Mark.exe
            if psutil.Process(os.getpid()).name() == 'Mark.exe':
                try:
                    soup = BeautifulSoup(requests.get("https://github.com/MarkThe/Mark-Tools/releases", headers=header).text, 'html.parser')
                    for link in soup.find_all('a'):
                        if "releases/download" in str(link):
                            update_url = f"https://github.com/{link.get('href')}"
                    new_version = requests.get(update_url)
                    with open("Mark-Tools-master.zip", 'wb')as zipfile:
                        zipfile.write(new_version.content)
                    with ZipFile("Mark-Tools-master.zip", 'r') as filezip:
                        filezip.extractall()
                    os.remove("Mark-Tools-master.zip")
                    cwd = os.getcwd()+'\\Mark\\'
                    shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                    shutil.copyfile(cwd+'Mark.exe', 'Mark.exe')
                    shutil.copyfile(cwd+'README.md', 'README.md')                   
                    shutil.rmtree('Mark')
                    setTitle('Mark-Tool Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                    sleep(1)
                    os.startfile("Mark.exe")
                    exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.LIGHTRED_EX}\nMark Tool-{THIS_VERSION} doesn't have enough permission to update\ntry re-running again as admin or turn off anti-virus otherwise try and download it manually here {update_url}\n\n\"{err}\"")
                    sleep(10)
            
            else:
                try:
                    new_version = requests.get("https://github.com/MarkThe/Mark-Tools/archive/refs/heads/main.zip")
                    with open("MarkThe/Mark-Tools-main.zip", 'wb')as zipfile:
                        zipfile.write(new_version.content)
                    with ZipFile("MarkThe/Mark-Tools-master.zip", 'r') as filezip:
                        filezip.extractall()
                    os.remove("MarkThe/Mark-Tools-main.zip")
                    cwd = os.getcwd()+'\\MarkThe/Mark-Tools-master'
                    shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                    shutil.rmtree(cwd)
                    setTitle('Mark-Tools Update Complete!')
                    print(f"{Fore.GREEN}Update Successfully Finished!{Fore.RESET}")
                    sleep(1)
                    os.startfile("run.bat")
                    exit()
                except Exception as err:
                    clear()
                    print(f"{Fore.LIGHTRED_EX}An error occured while Updating MarkThe/Mark-Tools-{THIS_VERSION}\n\nIf this keeps occuring try and download it manually here github.com/MarkThe/Mark-Tools\n\n\"{err}\"")
                    sleep(7)

        else:
            input
            return
