import discord
import traceback
from src.config import db, bot
import src

embed_colour = 0x404D67

def get(primary, category, content):
  try:
     if primary == "core":
        
        if category == "simple":
           embed = discord.Embed(colour=embed_colour,description=content)

        if category == "success":
           embed = discord.Embed(colour=0x1fff8b,description=f"<:online:1078291279756136488>  {content}")

        if category == "denied":
           embed = discord.Embed(colour=0xff3939,description=f"<:offline:1078291224840114186> {content}")
         
        if category == "error":
           embed = discord.Embed(colour=embed_colour,description=f"Uh oh! An error occured, thankfully it was caught by our handler. If this error continues report it to our support server```{content}```")

     return embed

  except Exception:
      embed = get("core","error",traceback.format_exc())
      return embed