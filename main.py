import discord
from discord.ext import commands
import os

komutlar = {
    "commands.owner.owner",
    "commands.moderation.channelC"
}


class MyClient(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='c!',pm_help=None, description='Discord bot')

        for x in komutlar:

            self.load_extension(x)
            print('{0} is loaded!'.format(x))
  

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.author.bot:
            return

        await self.process_commands(message)


client = MyClient()
client.run(os.environ['BOT_TOKEN'])