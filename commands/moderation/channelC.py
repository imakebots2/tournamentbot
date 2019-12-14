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
                await channel.edit(bitrate=number*1000)

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


    @category.command()
    async def channelNames(self,ctx, *,categoryName:str):
        guild = ctx.guild
        cc = ''
        for x in guild.channels:
            if categoryName.upper() == x.name.upper():
                cc = x
                break
        
        if not cc:
            return await ctx.send('O isimde bir kanal bulunamadi')

        embed = discord.Embed()
        a = []
        i = 0
        for channel in cc.voice_channels:
            a.append(channel.name)

        channels = '\n'.join(a)
        embed.add_field(name="Names",value=channels)
        await ctx.send(embed=embed)

    @commands.group(name='channel',aliases=['kanal'])
    async def _channel(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('{0.command.name} ile ilgili komutlari gormek icin {0.prefix}help {0.command.name} yazin'.format(ctx))

    @_channel.command()
    async def userlimit(self,ctx,channelName:str,limit:int=0):
        if not owner_check(ctx):
            return await ctx.send('Yetkin yok dostum piahhauahuahuaha!')

        if limit < 0:
            await ctx.send("Limit 0 dan kucuk olamaz")
        elif limit >= 100:
            await ctx.send("Limit 99 dan butuk olamaz")

        channel = ''
        for x in guild.channels:
            if channelName.upper() == x.name.upper():
                channel = x
                break
        if not channel:
            return await ctx.send("Bu isimde bir kanal mevcut degil")

        await channel.edit(user_limit=limit)
        await ctx.send('{0.mention}` {1.name} kullanici limiti {2} ile degistirildi.'.format(ctx.author,channel,limit))

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

    @_channel.command(aliases=["boşlarıal"])
    async def emptydelete(self,ctx,*,channelName:str):
        if not owner_check(ctx):
            return await ctx.send('Yetkin yok dostum piahhauahuahuaha!')
                
        guild = ctx.guild
        channel = ''
        for x in guild.channels:
            if channelName.upper() == x.name.upper():
                channel = x
                break
        if not channel:
            return await ctx.send("Bu isimde bir kanal mevcut degil")
        if channel.type != discord.ChannelType.category:
            return await ctx.send("Böyle bir kategori kanalı mevcut değil.")

        voiceChannels = channel.voice_channels
        ss = []

        for chan in voiceChannels:
            if not chan.members:
                ss.append(chan)

        for rC in ss:
            await rC.delete()

        await ctx.send('{0.mention}` {1} tane kanal silindi'.format(ctx.author,len(rC)))


def setup(bot):
    bot.add_cog(ChannelC(bot))