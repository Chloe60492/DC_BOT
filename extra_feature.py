
import discord
from discord.emoji import Emoji
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.ext.commands.context import Context

#要額外import的
from discord.ui import Button, View  
import random


########
# Extra Bot Features
########

class Listener(commands.Cog):
    def __init__(self, bot: commands.Bot):  #參數: 參數註解(轉換參數的型態)
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content.lower()
        if 'thanks' in content or 'thank' in content or 'thx' in content:
            response = ["Anytime!", "No worries.", "You're welcome.", "Sure, no problem!"]
            await message.add_reaction('\U0001F917')
            await message.reply(random.choice(response)) 
            
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await before.channel.send(
            f'{before.author} edit a message.\n'
            f'before: {before.content}\n'
            f'after: {after.content}'
        )

class Extra(commands.Cog):
    def __init__(self, bot: commands.Bot):  #參數: 參數註解(轉換參數的型態)
        self.bot = bot
    @commands.command()
    async def helper(self, ctx:Context):
        embed = discord.Embed(
            title='BOT COMMANDS',
            description='Welcome! This is help section. Here are all the aommands.',
            color=discord.Colour.blue()
        )
        embed.set_thumbnail(url='https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/282194066/original/a77044363ee19df78b11600281de6dc2795ae806/do-telegram-bots-of-varying-complexity.png')
        embed.add_field(
            name='!helper',
            value='List all of the commands',
            inline=False
        )
        embed.add_field(
            name='!hello',
            value='Greeting',
            inline=False
        )
        embed.add_field(
            name='!say',
            value='Repeat what you said',
            inline=False
        )
        embed.add_field(
            name='!prefix',
            value='Custom prefix',
            inline=False
        )
        embed.add_field(
            name='!GPA',
            value='Calculate the GPA averge for the grades sequence',
            inline=False
        )
        embed.add_field(
            name='!food',
            value='Give you common food delivery websites',
            inline=False
        )
        embed.add_field(
            name='!shop',
            value='Give you common online shopping websites',
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def food(self, ctx: Context):
        button1 = Button(label="Foodpanda", style=discord.ButtonStyle.link, url="https://reurl.cc/qLzDrg", emoji='🐼')
        button2 = Button(label="UberEats", style=discord.ButtonStyle.link, url="https://reurl.cc/2LM4EE", emoji='🛵')
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await ctx.send("I recommend the following websites.", view=view)
    @commands.command()
    async def shop(self, ctx: Context):
        button1 = Button(label="Shopee", style=discord.ButtonStyle.link, url="https://reurl.cc/kXN5nx", emoji='1️⃣')
        button2 = Button(label="PChome", style=discord.ButtonStyle.link, url="https://reurl.cc/gDkvYQ", emoji='2️⃣')
        button3 = Button(label="MOMO", style=discord.ButtonStyle.link, url="https://reurl.cc/94oznY", emoji='3️⃣')
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        await ctx.send("I recommend the following websites.", view=view)    
