#!/bin/python

# Import pip modules
import discord, os, requests, random, json, numpy, random
from discord.ext import commands  # Make sure to install the discord module (python -m pip install discord)
from dotenv import load_dotenv # Make sure to install the dotenv module (python -m pip install python-dotenv)
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Load the environment variables from the .env file
load_dotenv()

# Configure the command options
prefix='.'
intents = discord.Intents().guilds
#client = commands.Bot(command_prefix=prefix,intents=intents)
bot = commands.Bot(command_prefix=prefix)

# Startup handler
@bot.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{bot.user}\"")
    

# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)

bot.load_extension("Fact")
bot.load_extension("TicTacToe")
bot.load_extension("8Ball")

bot.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))