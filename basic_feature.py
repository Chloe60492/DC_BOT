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
    async def prefix(self, ctx: Context, new_prefix: str):
        self.bot.command_prefix = new_prefix
        await ctx.send(f'Command prefix has been set to "{new_prefix}"')

    @commands.command()
    async def GPA(self, ctx: Context, *, grades: str = ""): 
        # *: 代表後面的參數不管有多少個都可以，因此可以解決空格問題
        def calculate_gpa(grades):
            grade_points = {
                'A+': 4.3,
                'A': 4,
                'A-': 3.7,
                'B+': 3.3,
                'B': 3,
                'B-': 2.7,
                'C+': 2.3,
                'C': 2,
                'C-': 1.7,
                'D': 1,
                'E': 0.8,
                'F': 0,
                'X': 0
            }

            total_grade_points = sum(grade_points.get(grade.upper(), 0) for grade in grades)
            gpa = total_grade_points / len(grades)
            return round(gpa, 2)
        grades_list = grades.split()
        gpa = calculate_gpa(grades_list)
        await ctx.send(gpa)
     

'''
class Extra(commands.Cog):
    def __init__(self, bot: commands.Bot):  #參數: 參數註解(轉換參數的型態)
        self.bot = bot
    @commands.command()
    async def union(self , ctx: Context, what: typing.Union[discord.TextChannel, discord.Member]):
        await ctx.send(what)
'''