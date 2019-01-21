import discord
import asyncio

from repost_manager import RepostManager
from configuration_manager import ConfigurationManager


class RepostBot:
    HASHES_FILENAME = 'hashes.txt'
    CONFIGURATION_FILENAME = 'settings.json'

    def __init__(self, client):
        self.manually_overriden = False

        self.configuration_manager = ConfigurationManager(self.CONFIGURATION_FILENAME)
        self.repost_manager = RepostManager(self.HASHES_FILENAME)

        self.configuration_manager.load_configuration()

        self.TOKEN = self.configuration_manager.configuration['token']

        self.MASTER_ADMIN_ID = self.configuration_manager.configuration['admin']

        self.ABOUT_MESSAGE = self.configuration_manager.configuration['about']

        self.commands = {
            "r!about": self.about,
            "r!off": self.off,
            "r!on": self.on
        }

        self.client = client

    def run(self):
        self.client.run(self.TOKEN)

    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')

    async def on_message(self, message):
        await self.process_command(message)
        if not self.manually_overriden and self.repost_manager.is_repost(message):
            try:
                await self.client.send_message(message.channel, message.author.display_name + ' just reposted a meme.')
                await self.client.delete_message(message)
            except discord.Forbidden:
                await self.client.send_message(message.channel, 'I need permissions to manage messages in order to work.')


    def is_admin(self, author):
        if (author.id == self.MASTER_ADMIN_ID):
            return True

        for role in author.roles:
            if role.permissions.administrator:
                return True

        return False

    async def about(self, message):
        await self.client.send_message(message.channel, self.ABOUT_MESSAGE)

    async def off(self, message):
        if self.is_admin(message.author):
            self.manually_overriden = True
            await self.client.send_message(message.channel, 'Repost control turned off.')

    async def on(self, message):
        if self.is_admin(message.author):
            self.manually_overriden = False
            await self.client.send_message(message.channel, 'Repost control turned on.')

    async def process_command(self, message):
        if message.content in self.commands:
            cmd = self.commands[message.content]
            await cmd(message)
    
