import discord
import asyncio
import json
import os
import sys

from repost_manager import RepostManager

repost_manager = RepostManager()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if repost_manager.is_repost(message):
        try:
            await client.send_message(message.channel, message.author.display_name + ' just reposted a meme.')
            await client.delete_message(message)
        except discord.Forbidden:
            await client.send_message(message.channel, 'I need permissions to manage messages in order to work.')

def main():
    with open(os.path.join(sys.path[0], 'settings.json')) as f:
        data = json.load(f)

    TOKEN = data['token']

    client.run(TOKEN)


if __name__ == '__main__':
    main()
