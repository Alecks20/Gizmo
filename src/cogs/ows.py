from discord.ext import commands
from discord.commands import Option
import discord
from src.config import bot, db
import src.embeds
import traceback

class ows(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ows = discord.SlashCommandGroup("ows", "Configuration related to the one word story module.")

    #Configuring 
    @ows.command(name="channel",description="Set the channel for your one word story to operate")
    async def ows_channel(self, ctx: discord.ApplicationContext, option: Option(discord.TextChannel, "Channel you wish for one word story to commence in", required = True)):
      await ctx.defer()
      try:

        #Check if user has permissions to run command
        if not ctx.interaction.user.guild_permissions.manage_guild:
            await ctx.send_followup(embed=src.embeds.get("core","denied","You don't have permission to run this command!"))
            return
        
        #Database config and variables
        new_ows_channel = option
        ows_config = db.ows_configs.find_one({"guild_id": ctx.guild_id})

        if ows_config:
            db.ows_configs.update_one({"guild_id": ctx.guild.id},{"$set": {"channel_id": new_ows_channel.id}})
        else:
            #Perform initial setup if config doesn't exist
            db.ows_configs.insert_one({"guild_id": ctx.guild.id,"channel_id": new_ows_channel.id,"words": [],"last_author": None})

        await ctx.send_followup(embed=src.embeds.get("core","success",f"Successfully setup the one word story in {new_ows_channel.mention}"))

      except Exception:
         await ctx.send_followup(embed=src.embeds.get("core","error",traceback.format_exc()))



def setup(bot):
  bot.add_cog(ows(bot))