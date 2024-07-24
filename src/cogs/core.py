from discord.ext import commands
import discord
from src.config import bot, db
import src.embeds

class core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Simple latency/healthcheck
    @discord.slash_command(name="ping",description="Health check, see system ping")
    async def ping(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(colour=src.embeds.embed_colour, description=f"Pong! Connections take {round(bot.latency * 1000)}ms")
        await ctx.respond(embed=embed)

def setup(bot):
  bot.add_cog(core(bot))