import discord
from bot import RepostBot

client = discord.Client()
bot = RepostBot(client)

@client.event
async def on_ready():
    await bot.on_ready()

@client.event
async def on_message(message):
    await bot.on_message(message)

def main():
    bot.run()

if __name__ == '__main__':
    main()
