import discord, config, time, aiohttp, psutil, platform
from collections import Counter
from discord.ext import commands
from datetime import datetime
from utils import default

class botlogs(commands.Cog, name="Bot logs"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        log = self.bot.get_channel(755138117488345118)
        
        e = discord.Embed(color=config.color)
        e.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        e.description = f"""
**Message content:**
{ctx.message.content}

**Author ID:** [{ctx.author.id}](https://discord.com/users/{ctx.author.id})

**Guild:** {ctx.guild.name} (`{ctx.guild.id}`) 
"""
        e.set_footer(text=datetime.now().__format__('%a %d %b %y, %H:%M'))
        e.set_thumbnail(url=ctx.guild.icon_url)
        await log.send(embed=e)
        
        print(f"{datetime.now().__format__('%a %d %b %y, %H:%M')} - {ctx.guild.name} | {ctx.author} > {ctx.message.clean_content}") 

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log = self.bot.channel_get(762203326519181312)
        
        e = discord.Embed(color=config.green)
        e.set_author(name="Joined a new guild", icon_url=self.bot.user.avatar_url)
        e.set_thumbnail(url=guild.icon_url)

        owner = await self.bot.fetch_user(guild.owner.id)

        members = len(guild.humans)
        bots = len(guild.bots)
        text = len(guild.text_channels)
        voice = len(guild.voice_channels)

        e.description = f"""
**Guild name:** {ctx.guild.name} (`{guild.id}`)
**Guild owner:** {str(owner)} (`{guild.owner.id}`)
**Created:** {default.date(ctx.guild.created_at)}
**Members:** {members} humans & {bots} bots
**Channels:** {text} text channels & {voice} vc's
"""
        await log.send(embed=e)
              
def setup(bot):
    bot.add_cog(botlogs(bot))
