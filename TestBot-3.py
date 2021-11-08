#!/bin/python
import discord, os, requests, random, json
from discord.ext import commands # Make sure to install the discord module (python -m pip install discord)
from dotenv import load_dotenv # Make sure to install the dotenv module (python -m pip install python-dotenv)
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Setup state
load_dotenv()  # load environment variables from .env
prefix='.'
client = commands.Bot(command_prefix=prefix)

# Startup handler
@client.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{client.user}\"")

# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)

# Fact Command handler
@client.command(name='fact')
async def _fact(ctx, arg1="onion", arg2=1, arg3="popularity"): # channel object, topic, months into past
    fact_date_to=datetime.now().date().strftime("%Y-%m-%d")
    print(f"[DEBUG][fact]: fact_date_to is '{fact_date_to}'")

    fact_date_from=(datetime.now().date() - relativedelta(months=int(arg2))).strftime("%Y-%m-%d")
    print(f"[DEBUG][fact]: fact_date_from is '{fact_date_from}'")

    fact_topic=arg1
    print(f"[DEBUG][fact]: fact_topic is '{fact_topic}'")

    fact_api_key = os.getenv("FACT_API_KEY", "[ERROR]: getenv('FACT_API_KEY') failed")
    print(f"[DEBUG][fact]: fact_api_key is '{fact_api_key}'")

    fact_sort=str(arg3)

    titles=["You wanted it. You'll get it!","Roger Roger.","Did you know that google exists?","End my suffering...","Here's what I found:","Yooo. It's lit!","Cactus Jack sent me...","Fascinating","Go on. Read it. I dare you!"]

    title = random.choice (titles)
    request = "https://newsapi.org/v2/everything?q="+fact_topic+"&from="+fact_date_from+"&to="+fact_date_to+"&sortBy="+fact_sort+"&apiKey="+fact_api_key
    print(f"[DEBUG][fact]: request is '{request}'")

    api_data = requests.get(request)

    await ctx.send(embed=embed(title,request,description=api_data.json(),color=0x2211EE))

# Message handler
#@client.event
#async def on_message(message):
#    if(message.author == client.user):
#        return
#    
#    if(message.content.startswith('.hello')):
#        await message.channel.send("Hello!")

client.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))