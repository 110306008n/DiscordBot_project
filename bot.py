from asyncore import read
from http import client
from typing import AsyncIterable
import discord
import json
import random
from discord.ext import commands

#mode=read      utf8 could encode chinese
with open("setting.json", mode="r", encoding="utf8") as jFile:
    jdata=json.load(jFile)

intents=discord.Intents.default()
intents.members=True    #set member event true


#create bot object.    intents is v1.5 update, decide what your bot can do(?)
bot=commands.Bot(command_prefix="!", intents=intents)

@bot.event
# onready=active   async complicated kind of function
async def on_ready():
    print(">>Bot is online")
    

@bot.event
async def on_member_join(member):
    #convert from String to int data type
    channel=bot.get_channel(int(jdata["Welcome_channel"]))
    channel_2=bot.get_channel(int(jdata["General_channel"]))
    print(">>member_join")
    await channel.send(f"{member}join!")
    await channel_2.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata["Leave_channel"]))
    channel_2=bot.get_channel(int(jdata["General_channel"]))
    print(">>member_leave")
    await channel_2.send(f"{member}leave!")

@bot.command()
# fuction name is the commmand line u have to type
#ctx = the word before and after 
#eg: 
#A:hi   (before)    feature(Id. server, channel, etc)
#B:LOL  (after)     read the feature above to let the bot know where should bot send msg
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000, 2)}ms")

@bot.command()
async def rPic(ctx):
    random_pic=random.choice(jdata["Pic"])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def wPic(ctx):
    random_pic=random.choice(jdata["wPic"])
    await ctx.send(random_pic)

#json resourses are 字典
bot.run(jdata["TOKEN"])
