import src.config
import aiohttp #Requests drop in replacement
import traceback
import random #Used to randomize which gif to return

async def fetch_gif(query):
  try:
    headers = {'Accept': 'application/json'}

    #Searching for gifs with a query
    if query != None:
     #Ask for 20 gifs so one can be randomly picked (Means that the same query won't respond with the same gif everytime)
     params = {'api_key': src.config.giphy_api_key, 'q': query, 'limit': 20}
       
     async with aiohttp.ClientSession() as session:

         async with session.get("https://api.giphy.com/v1/gifs/search", headers=headers, params=params) as resp:
              if resp.status == 200:
                   data = await resp.json()

                   #Choosing a random gif out of the 20 returned
                   gifs = data["data"]
                   random_gif = random.choice(gifs)

                   return random_gif["images"]["original"]["url"]
              else:
                   return f"Error fetching gif: {resp.status}"
    
    #Random gifs (No Query)
    else:
     params = {'api_key': src.config.giphy_api_key, 'limit': 1}
       
     async with aiohttp.ClientSession() as session:
       async with session.get("https://api.giphy.com/v1/gifs/random", headers=headers, params=params) as resp:
          
          if resp.status == 200:
             data = await resp.json()
             return data["data"]["images"]["original"]["url"]
             
          else:
             return "Error fetching random gif"
       
            
  except Exception:
     print(traceback.format_exc())
  