#!/bin/python

# Import pip modules
from discord.ext import commands
import discord

# Configure the command options
prefix = '.'
intents = discord.Intents().guilds
#client = commands.Bot(command_prefix=prefix,intents=intents)
bot = commands.Bot(command_prefix=prefix)


bot.load_extension("KickBot.kick")

bot.run("OTAyMTkwMTYxOTE4NTY2NDkx.YXa0EA.WiG0vs8OLHVarXccCUrluLpHNc4")
