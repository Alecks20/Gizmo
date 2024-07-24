import pymongo
from dotenv import load_dotenv
from discord.ext import commands
import os
import discord

#Variables and configuration
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Bot(intents=intents)

try:
    testing = os.environ["TESTING"]
except:
    testing = "false"
try:
    testing_token = os.environ["TESTING_TOKEN"]
except:
    print("Testing token was not set.")


#Database Setup
if testing == "false":
    username = os.environ["MONGO_INITDB_ROOT_USERNAME"]
    password = os.environ["MONGO_INITDB_ROOT_PASSWORD"]
    mongo = pymongo.MongoClient(f"mongodb://{username}:{password}@mongodb/")
    db = mongo.soar
elif testing == "true":
    mongo = pymongo.MongoClient(os.environ["MONGO_TESTING"])
    db = mongo.soar_testing

#Keys
giphy_api_key = os.environ["GIPHY_API_KEY"]