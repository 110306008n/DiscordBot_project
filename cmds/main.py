from cgitb import text
from datetime import datetime
import discord
import datetime
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

    @commands.command()
    async def embed(self, ctx):
        embed=discord.Embed(title="test", url="https://i.guim.co.uk/img/media/3aab8a0699616ac94346c05f667b40844e46322f/0_123_5616_3432/master/5616.jpg?width=300&quality=45&auto=format&fit=max&dpr=2&s=a9b8ddacc7b4dc6625d259fa38fef9ba", description="description", color=0xff0000, timestamp=datetime.datetime.now())
        embed.set_author(name="name")
        embed.set_thumbnail(url="https://i.imgur.com/XxjJq7r.jpeg")
        embed.add_field(name="fields name", value="text", inline=True)
        embed.add_field(name="f2", value="text", inline=False)
        embed.set_footer(text="footer")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))