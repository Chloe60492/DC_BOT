import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import typing


class Extra(commands.Bot):
    def __init__(self, bot: commands.Bot):  #參數: 參數註解(轉換參數的型態)
        self.bot = bot
    @commands.command()
    async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
        await ctx.send(what)
