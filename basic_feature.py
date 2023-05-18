import discord
from discord.ext import commands
from discord.ext.commands.context import Context

########
# Basic Bot Features
########

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot):  #參數: 參數註解(轉換參數的型態)
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx: Context, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member
    
    @commands.command()
    async def say(self, ctx: Context, *, s: str):
        await ctx.send(s)
        
    @commands.command()
    async def prefix(self, ctx: Context, s: str):
        new_prefix = s
        await ctx.prefix(new_prefix)

    @commands.command()
    async def GPA(self, ctx: Context, *, s: str = ""): 
        # *: 代表後面的參數不管有多少個都可以，因此可以解決空格問題
        # [TODO]
        pass
