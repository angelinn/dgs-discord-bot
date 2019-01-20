import discord
import asyncio
import json
import os
import sys
import requests
import hashlib

client = discord.Client()
image_hashes = set()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def has_image(message):
    return len(message.attachments) > 0

def load_hashes():
    if os.path.exists(os.path.join(sys.path[0], 'hashes.txt')):
        with open(os.path.join(sys.path[0], 'hashes.txt')) as f:
            lines = f.read().splitlines()
            for hash in lines:
                image_hashes.add(hash)

def save_hashes():
    with open(os.path.join(sys.path[0], 'hashes.txt'), 'w') as f:
        for item in image_hashes:
            f.write("%s\n" % item)

def calculate_hash(bytes):
    return hashlib.md5(bytes).hexdigest()

def download_image(url):
    return requests.get(url).content

def is_repost(message):
    if has_image(message):
        url = message.attachments[0]['url']
        img_data = download_image(url)
        hash = calculate_hash(img_data)

        return hash in image_hashes

    return False

@client.event
async def on_message(message):
    if is_repost(message):
        try:
            await client.send_message(message.channel, message.author.display_name + ' just reposted a meme.')
            await client.delete_message(message)
        except discord.Forbidden:
            await client.send_message(message.channel, 'I need permissions to manage messages in order to work.')
    else:
        image_hashes.add(hash)
        save_hashes()

def main():
    with open(os.path.join(sys.path[0], 'settings.json')) as f:
        data = json.load(f)

    TOKEN = data['token']

    load_hashes()

    client.run(TOKEN)


if __name__ == '__main__':
    main()
