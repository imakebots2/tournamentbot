import discord
from discord.ext import commands


komutlar = {
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
client.run('NDUxODM4NDU3NDg5MjYwNTUy.XdveAQ.fkjAj4cT7KTORrqAHRvDPn1a3kE')