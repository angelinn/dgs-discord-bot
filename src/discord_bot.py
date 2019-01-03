import discord
import asyncio
import json
import os
import sys

with open(os.path.join(sys.path[0], 'settings.json')) as f:
    data = json.load(f)

TOKEN = data['token']

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
        #counter = 0
        #tmp = await client.send_message(message.channel, 'Calculating messages...')
        #async for log in client.logs_from(message.channel, limit=100):
        #    if log.author == message.author:
        #        counter += 1

        # await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        await client.send_message(message.channel, 'Cura is.')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(TOKEN)
