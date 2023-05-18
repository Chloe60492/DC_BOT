import discord
from discord.ext import commands



# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

#成員加入後觸發的事件(在terminal出現)
@bot.event 
async def on_ready():
    print(">> BOT IS ONLINE! <<")

#在特定頻道裡發送訊息

@bot.event
async def on_member_join(member):
    print(f'{member} joins!')
    channel = bot.get_channel(1108247685263282247) 
    #channel id: 要打開使用者設定裡的開發者設定選項才能按右鍵複製到id
    await channel.send(f'{member} joins!')

@bot.event
async def on_member_remove(member):
    print(f"{member} leavs!")
    channel = bot.get_channel(1108248143218356394)
    await channel.send(f"{member} leaves!")





#put token
bot.run("MTEwNzU1NjAzOTE0Mzk4MTExNg.GAZM18.L55ooxfsrkPRhUizPcYT52APhQvln0wsXr1IEk")


