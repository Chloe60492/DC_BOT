import os
import asyncio

from dotenv import load_dotenv
from discord.ext import commands
import discord

from basic_feature import Basic
from extra_feature import Listener, Extra
#要額外import的
from discord.ui import Button, View
import random  

class MyCommandBot(commands.Bot):
    # 初始化，*args: 參數，**kwargs: 關鍵字參數
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ''' 這裡的super()意指把父層(parent)commands.Bot的設定再進行初始化一次
            如果不這麼做的話，這邊的(child)初始化會把父層設定蓋掉
            因此這一行程式碼等同於父層的初始化
        '''
        # self.target_massage_id = 1109724337109471292

    async def on_ready(self):
        print("Bot is online!")
        print('Logged in as {0} ({0.id})'.format(self.user))

    async def on_message(self, message: discord.Message, /) -> None:
        print(f'Message from {message.author}: {message.content}')
        return await super().on_message(message)

async def create_bot():
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Add commands by cog
    bot = MyCommandBot(command_prefix='!', intents=intents)

    await bot.add_cog( Basic(bot) )
    await bot.add_cog( Extra(bot) )
    await bot.add_cog( Listener(bot) )
    return bot

def main():
    load_dotenv()

    bot = asyncio.run( create_bot() )

    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

