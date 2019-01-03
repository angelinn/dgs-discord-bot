import discord
import asyncio
import json
import os
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if 'pleb' in message.content:
        await client.send_message(message.channel, 'Cura is.')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

def main():
    with open(os.path.join(sys.path[0], 'settings.json')) as f:
        data = json.load(f)

    TOKEN = data['token']

    client.run(TOKEN)


if __name__ == '__main__':
    main()
