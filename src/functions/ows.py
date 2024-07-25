from src.config import bot, db

async def process_ows(msg):

    if msg.author.bot == True:
        return

    #Fetching configuration from database
    ows_config = db.ows_configs.find_one({"channel_id":msg.channel.id})

    if not ows_config:
        return

    #Set all the configuration as variables
    ows_words = ows_config["words"]
    ows_last_author = ows_config["last_author"]
    ows_guild_id = ows_config["guild_id"]
    ows_channel_id = ows_config["channel_id"]

    #Static variables
    ows_character_limit = 4096
    ows_max_word_length = 45


    #Check if channel is configured as ows channel
    if ows_guild_id == msg.guild.id and ows_channel_id == msg.channel.id:
      
      #Checks to stop bad messages being added
      
      #Block from sending 2 messages in a row
      if ows_last_author == msg.author.id:
         await msg.delete()
         return

      #Make sure story stays under character limit 
      if ows_words:
        words_list = []
        for item in ows_words:
            words_list.append(item + " ")
        ows_words.append(msg.content)
        ows_words = "".join(ows_words)

        if len(ows_words) > ows_character_limit:
           await msg.delete()
           return

        
      #Block non alpha-numeric characters
      if (any(not character.isalnum() for character in msg.content)):
        await msg.delete()
        return

      #Block messages over the individual character limit
      if len(msg.content) > ows_max_word_length:
        await msg.delete()
        return

      
      #Add checkmark reaction to users message
      await msg.add_reaction("☑")

      #Push updates to database
      db.ows_configs.update_one({"guild_id": msg.guild.id},{"$set": {"last_author": msg.author.id}}) #Update the last author so user cannot send 2 messages in a row
      db.ows_configs.update_one({ "guild_id": msg.guild.id },{ "$push": { "words": msg.content } }) #Adding message to one word story word cache
        
        
    
