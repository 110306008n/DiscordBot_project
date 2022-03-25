from asyncore import read
from http import client
from typing import AsyncIterable
import discord
intents=discord.Intents.default()
intents.members=True    #set member event true


from discord.ext import commands

#create bot object.    intents is v1.5 update, decide what your bot can do(?)
bot=commands.Bot(command_prefix="!", intents=intents)

@bot.event
# onready=active   async complicated kind of function
async def on_ready():
    print(">>Bot is online")
    

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(956858446416855060)
    channel_2=bot.get_channel(956849102635823135)
    await channel.send(f"{member}join!")
    await channel_2.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(956858485172219914)
    channel_2=bot.get_channel(956849102635823135)
    await channel.send(f"{member}leave!")
    await channel_2.send(f"{member}join!")


bot.run("OTU2ODQxNDE5NDc2MTg5MjE0.Yj2GAw.PTy4oiVM6dqalLvTOV1hJhONMV0")
