import discord
from discord.ext import commands

from core.classes import Cog_Extention
#import file:Cog_Extention  Autometical add the line    OMG :)

class Main(Cog_Extention):
    #Main extends Cog_Extention
    

    @commands.command()
    # fuction name is the commmand line u have to type
    #ctx = the word before and after 
    #eg: 
    #A:hi   (before)    feature(Id. server, channel, etc)
    #B:LOL  (after)     read the feature above to let the bot know where should bot send msg
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000, 2)}ms")
        await ctx.send("test reload")

def setup(bot):
    bot.add_cog(Main(bot))