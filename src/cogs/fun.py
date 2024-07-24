from discord.ext import commands
from discord.commands import Option
import discord
from src.config import bot, db
import src.embeds
import src.functions.fun

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Grabbing a gif from giphy
    @discord.slash_command(name="gif",description="Fetch a gif from giphy")
    async def ping(self, ctx: discord.ApplicationContext, query: Option(str, "Search for a specific gif", required = False)):

        #Giving the giphy api some time to respond (Preventing command timeouts)
        await ctx.defer()

        gif = await src.functions.fun.fetch_gif(query)
        
        #Catch errors from giphy api
        if gif == None:
            embed = discord.Embed(colour=src.embeds.embed_colour, description="Unable to find a gif or giphy is having issues")
            await ctx.send_followup(embed=embed)
            return

        #Putting the giphy url into a discord embed
        if query == None:
            title = "Random Gif"
            description = ""
        else:
            title = "Custom Gif"
            description = f"{query}"

        embed = discord.Embed(colour=src.embeds.embed_colour,title=title,description=description)
        embed.set_image(url=gif)
        embed.set_footer(text="Fetched from api.giphy.com")

        await ctx.send_followup(embed=embed)
        

def setup(bot):
  bot.add_cog(fun(bot))