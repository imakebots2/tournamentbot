import discord
from discord.ext import commands
from utils.is_owner import owner_check

class ChannelC(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(aliases=['kategori'])
    async def category(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('{0.command.name} ile ilgili komutlari gormek icin {0.prefix}help {0.command.name} yazin'.format(ctx))

    @category.command()
    async def limit(self,ctx, categoryName:str, number:int):
        if not owner_check(ctx):
            return await ctx.send('Yetkin yok dostum piahhauahuahuaha!')
        guild = ctx.guild
        cc = ''
        for x in guild.channels:
            if categoryName.upper() == x.name.upper():
                cc = x
                break
        
        if not cc:
            return await ctx.send('O isimde bir kanal bulunamadi')
        
        for channel in cc.voice_channels:
            if channel:
                await channel.edit(user_limit=number)

        await ctx.send('Butun kanallarin limiti {} ayarlandi'.format(number))

    @category.command()
    async def bitrate(self,ctx, categoryName:str, number:int):
        if not owner_check(ctx):
            return await ctx.send('Yetkin yok dostum piahhauahuahuaha!')
        if number < 8:
            return await ctx.send('Kanal bitrate i 8 den kucuk olamaz')
        elif number > 96:
            return await ctx.send('Kanal bitrate i 96 dan buyuk olamaz')


        guild = ctx.guild
        cc = ''
        for x in guild.channels:
            if categoryName.upper() == x.name.upper():
                cc = x
                break
        
        if not cc:
            return await ctx.send('O isimde bir kanal bulunamadi')
        
        for channel in cc.voice_channels:
            if channel:
                await channel.edit(bitrate=number)

        await ctx.send('Butun kanallarin limiti {} ayarlandi'.format(number))

    @category.command()
    async def channelcount(self,ctx,*,categoryName:str):

        guild = ctx.guild
        cc = ''
        for x in guild.channels:
            if categoryName.upper() == x.name.upper():
                cc = x
                break
        
        if not cc:
            return await ctx.send('O isimde bir kanal bulunamadi')

        await ctx.send('Kanal sayisi {}'.format(len(cc.voice_channels)))

    @commands.group(name='channel',aliases=['kanal'])
    async def _channel(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('{0.command.name} ile ilgili komutlari gormek icin {0.prefix}help {0.command.name} yazin'.format(ctx))


    @_channel.command(aliases=['mevcut'])
    async def exist(self,ctx, name:str):
        guild = ctx.guild
        cc = ''
        for x in guild.channels:
            if name.upper() == x.name.upper():
                cc = x
                break
        
        if not cc:
            return await ctx.send('O isimde bir kanal bulunamadi')
        else:
            await ctx.send('Kanal bulundu {}'.format(cc.mention))

    


def setup(bot):
    bot.add_cog(ChannelC(bot))