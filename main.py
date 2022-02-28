#!/bin/python

# Import pip modules
import discord, os, requests, random, json, numpy, random
from discord.ext import commands  # Make sure to install the discord module (python -m pip install discord)
from dotenv import load_dotenv # Make sure to install the dotenv module (python -m pip install python-dotenv)
from datetime import datetime
from dateutil.relativedelta import relativedelta

# TODO Send R. a personal message which contains an .env file with working active secrets
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

# TODO Add support for the other python modules (bot function implementations)
# TODO Notifiy the other teammembers to push their changes by creating a new issue and assigning all of them

# _ Facts
bot.load_extension("Fact")

# _ TicTacToe
# TODO fix and find the working ttt implementation source code "PASTE HERE"
# bot.load_extension("TicTacToe")

# _ RPC

# _ 8Ball
bot.load_extension("8Ball")

# _ @ Random response

# _ Play

# _ Mute @
bot.load_extension("Mute")

# _ Ban
bot.load_extension("Ban")

# _ Kick
bot.load_extension("Kick")

# _ Anti Spam

# _ Help


# _ Info
bot.load_extension("Info")

# _ Willkommens Nachricht

# _ User Level

# _ DB

# TODO Test and create new pull request for the master branch, then merge with the master branch

# TODO Notify all teammebmbers to checkout to the new 'Combined' branch

bot.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))