from asyncore import read
from http import client
from typing import AsyncIterable
import discord
import json
import os
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
    

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F"cmds.{extension}")
    await ctx.send(F"Loaded{extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F"cmds.{extension}")
    await ctx.send(F"Unloaded{extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F"cmds.{extension}")
    await ctx.send(F"Reloaded{extension} done.")

#list all the file under folder cmds
for Filename in os.listdir("./cmds"):
    #only import python file
    if Filename.endswith(".py"):
        #output from first to the last three
        #eg: main.py ---> main 
        bot.load_extension(F"cmds.{Filename[:-3]}")
        
if __name__ == "__main__":
    #json resourses are 字典
    bot.run(jdata["TOKEN"])
