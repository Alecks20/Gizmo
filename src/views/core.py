import discord

class requested_by(discord.ui.View):
   def __init__(self, user: discord.User):
      super().__init__()
      self.user = user
      self.add_item(discord.ui.Button(label=f"Requested by {self.user.name.capitalize()}",style=discord.ButtonStyle.gray, disabled=True))
