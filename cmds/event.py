import discord
from discord.ext import commands
import json

from core.classes import Cog_Extention
#import file:Cog_Extention  Autometical add the line    OMG :)

with open("setting.json", mode="r", encoding="utf8") as jFile:
    jdata=json.load(jFile)

class Event(Cog_Extention):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        #convert from String to int data type
        channel=self.bot.get_channel(int(jdata["Welcome_channel"]))
        channel_2=self.bot.get_channel(int(jdata["General_channel"]))
        print(">>member_join")
        await channel.send(f"{member}join!")
        await channel_2.send(f"{member}join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel=self.bot.get_channel(int(jdata["Leave_channel"]))
        channel_2=self.bot.get_channel(int(jdata["General_channel"]))
        print(">>member_leave")
        await channel.send(f"{member}leave!")
        await channel_2.send(f"{member}leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        #msg.author!=self.bot.user to check whether the msg was from bot
        #to avoid infinite loop(bot called itself)
        #could active the function with multiple keyword by using list
        keyword=["apple", "pen", "pie"]
        if msg.content in keyword and msg.author!= self.bot.user:
            #msg.channel could spot the channel bot should reply
            await msg.channel.send("hi")

def setup(bot):
    bot.add_cog(Event(bot))