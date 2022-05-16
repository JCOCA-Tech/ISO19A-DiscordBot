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


# Willkommensnachricht
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(902176471844540486)
    embed = discord.Embed(
        title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    await channel.send(embed=embed)


@bot.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{bot.user}\"")


# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)


bot.load_extension("Functions.Games.Fact")
# The 'tictactoe' command also contains the 'place' command
bot.load_extension("Functions.Games.TicTacToe")
bot.load_extension("Functions.Games.8Ball")

bot.load_extension("Functions.Admin.Ban")
bot.load_extension("Functions.Admin.Mute")
bot.load_extension("Functions.Admin.Unmute")
bot.load_extension("Functions.Admin.Kick")
bot.load_extension("Functions.Admin.Antispam")
bot.load_extension("Functions.Music.Music")

bot.load_extension("Functions.Info.HelpCommand")
bot.load_extension("Functions.Info.Serverinfo")
bot.load_extension("Functions.Info.Userinfo")


bot.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))
