#!/bin/python3

# Import pip modules
import discord
import os
import requests
import random
import json
import numpy
import random
# Make sure to install the discord module (python -m pip install discord)
from discord.ext import commands
# Make sure to install the dotenv module (python -m pip install python-dotenv)
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Load the environment variables from the .env file
load_dotenv()

# Configure the command options
prefix = '.'
intents = discord.Intents().guilds
bot = commands.Bot(command_prefix=prefix)

# Startup handler


@bot.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{bot.user}\"")


# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)


bot.load_extension("Fact")
# The 'tictactoe' command also contains the 'place' command
bot.load_extension("TicTacToe")
bot.load_extension("8Ball")

bot.load_extension("Ban")
bot.load_extension("Mute")
bot.load_extension("Unmute")
bot.load_extension("Kick")
bot.load_extension("Music")

# bot.load_extension("Help")
bot.load_extension("About")
bot.load_extension("Userinfo")


bot.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))
