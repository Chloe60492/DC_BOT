import discord
from discord.ext import commands
from discord.ext.commands.context import Context

########
# Basic Bot Features
########

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
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
    async def say(self, ctx: Context, *args):
        await ctx.send("{}".format(" ".join(args)))
        
    @commands.command()
    async def prefix(self, ctx: Context, s: str):
        # [TODO]
        pass

    @commands.command()
    async def GPA(self, ctx: Context, *, s: str = ""):
        # [TODO]
        pass
