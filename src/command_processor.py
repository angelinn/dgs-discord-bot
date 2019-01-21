
class CommandProcessor:
    
    def __init__(self, bot):
        self.bot = bot

        self.commands = {
            "r!about": self.about,
            "r!off": self.off,
            "r!on": self.on
        }

    async def process_command(self, message):
        if message.content in self.commands:
            cmd = self.commands[message.content]
            await cmd(message)

    async def about(self, message):
        await self.bot.about(message)

    async def on(self, message):
        await self.bot.on(message)

    async def off(self, message):
        await self.bot.off(message)
