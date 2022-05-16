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
    channel = bot.get_channel(902177572975149126)
    embed = discord.Embed(
        title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    await channel.send(embed=embed)


# Levelsystem
"""@bot.event
async def on_message(message):
    mycursor = mydb.cursor()
    #User Id wird ausgelesen
    userId = str(message.author.id)
    print("Author ID: " + userId )
    #Existiert Benutzer schon
    mycursor.execute("SELECT points FROM users Where userId = " + userId)
    result = mycursor.fetchall()
    print(result)
    x = len(result)
    print(x)
    if x == 0:
        print("Test 1")
        #User wird erstellt
        mycursor.execute("INSERT INTO users (userId) VALUES (" + userId + ")")
    else:
        print("Test 2")
        #Jetzige Punktzahl wird abgefragt
        mycursor.execute("SELECT points FROM users Where userId = " + userId)
        result = mycursor.fetchall()
        newresult = str(result)
        print(newresult)
        #Neue Punktzahl wird gesetzt
        sql = "UPDATE users SET points = " + newresult + "WHERE userId = " + userId
        mycursor.execute(sql)"""


@bot.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{bot.user}\"")


# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)


@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        # Specify API endpoint on the rasa instance
        message_url = 'http://localhost:5005/webhooks/rest/webhook'
        # Request headers
        headers = {'Content-type': 'application/json'}
        # Request payload
        payload = '{"sender": "' + str(message.author.id) + \
            '", "message": "' + message.content + '"}'
        # Post request
        r = requests.post(message_url, data=payload.encode(
            'utf-8'), headers=headers)
        # Log the response message from rasa, preceeded by user id
        print(f"[DEBUG][RASA]: {json.loads(r.content)}")
        try:
            # Parse response
            res = json.loads(r.content)[0]
            # Answer to the user that sent the message (mentions the recipient)
            await message.reply(res['text'])
        except:
            await message.reply("Oopsie! looks like i am currently not able to handle this")
    return


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
