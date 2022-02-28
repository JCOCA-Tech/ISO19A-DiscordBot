#!/bin/python

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

# Configure the command options
prefix = '.'
intents = discord.Intents().guilds
#client = commands.Bot(command_prefix=prefix,intents=intents)
bot = commands.Bot(command_prefix=prefix)


bot.load_extension("Functions.Emanuell.mute")
bot.load_extension("Functions.Emanuell.unmute")
bot.load_extension("Functions.Emanuell.ban")

bot.run("OTAyMTkwMTYxOTE4NTY2NDkx.YXa0EA.WiG0vs8OLHVarXccCUrluLpHNc4")
