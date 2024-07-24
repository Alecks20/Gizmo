import discord
import traceback
from src.config import db, bot
import src

embed_colour = 0x404D67

def get(primary, category, content):
  try:
     pass # This is a work in progress

  except Exception:
      embed = get("core","error",traceback.format_exc())
      return embed