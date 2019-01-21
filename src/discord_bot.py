import discord
import asyncio

from repost_manager import RepostManager
from configuration_manager import ConfigurationManager

HASHES_FILENAME = 'hashes.txt'
CONFIGURATION_FILENAME = 'settings.json'
MASTER_ADMIN_ID = ''
ABOUT_MESSAGE = ''

repost_manager = RepostManager(HASHES_FILENAME)
configuration_manager = ConfigurationManager(CONFIGURATION_FILENAME)

client = discord.Client()

manually_overriden = False

async def about(message):
    await client.send_message(message.channel, ABOUT_MESSAGE)

def is_admin(author):
    if (author.id == MASTER_ADMIN_ID):
        return True

    for role in author.roles:
        if role.permissions.administrator:
            return True

    return False

async def off(message):
    if is_admin(message.author):
        manually_overriden = True
        await client.send_message(message.channel, 'Repost control turned off.')

async def on(message):
    if is_admin(message.author):
        manually_overriden = False
        await client.send_message(message.channel, 'Repost control turned on.')

commands = {
    "r!about": about,
    "r!off": off,
    "r!on": on
}

async def process_command(message):
    if message.content in commands:
        cmd = commands[message.content]
        await cmd(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await process_command(message)
    if not manually_overriden and repost_manager.is_repost(message):
        try:
            await client.send_message(message.channel, message.author.display_name + ' just reposted a meme.')
            await client.delete_message(message)
        except discord.Forbidden:
            await client.send_message(message.channel, 'I need permissions to manage messages in order to work.')

def main():
    configuration_manager.load_configuration()
    TOKEN = configuration_manager.configuration['token']

    global MASTER_ADMIN_ID
    MASTER_ADMIN_ID = configuration_manager.configuration['admin']

    global ABOUT_MESSAGE
    ABOUT_MESSAGE = configuration_manager.configuration['about']

    client.run(TOKEN)


if __name__ == '__main__':
    main()
