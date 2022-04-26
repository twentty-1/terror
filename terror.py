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

token = "TOKEN"

def murder(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("...".center(width))
        print()
        print("[-] twentty#0001 [-]".center(width))
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