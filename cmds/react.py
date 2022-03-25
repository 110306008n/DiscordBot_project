import discord
from discord.ext import commands
import random
import json

from core.classes import Cog_Extention
#import file:Cog_Extention  Autometical add the line    OMG :)

#mode=read      utf8 could encode chinese
with open("setting.json", mode="r", encoding="utf8") as jFile:
    jdata=json.load(jFile)


class React(Cog_Extention):
    #Main extends Cog_Extention
    @commands.command()
    async def rPic(self, ctx):
        random_pic=random.choice(jdata["Pic"])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def wPic(self, ctx):
        random_pic=random.choice(jdata["wPic"])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))