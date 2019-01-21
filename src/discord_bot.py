import discord
import asyncio

from repost_manager import RepostManager
from configuration_manager import ConfigurationManager

HASHES_FILENAME = 'hashes.txt'
CONFIGURATION_FILENAME = 'settings.json'

repost_manager = RepostManager(HASHES_FILENAME)
configuration_manager = ConfigurationManager(CONFIGURATION_FILENAME)

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
    configuration_manager.load_configuration()
    TOKEN = configuration_manager.configuration['token']

    client.run(TOKEN)


if __name__ == '__main__':
    main()
