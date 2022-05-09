import discord
import json
import os
import mysql.connector

from discord.ext import commands

# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=None)
os.chdir(r'C:\dev\ISO19A-DiscordBot')


# Meldung wenn der Bot erfolgreich gestartet wurde
@bot.event
async def on_ready():
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')

bot.load_extension("helpCommand")
bot.load_extension("serverinfo")
bot.load_extension("userinfo")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="discordbot"
)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(902176471844540486)
    embed = discord.Embed(title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    channel.send(embed=embed)

    #User in Datenbank abfüllen
    mycursor = mydb.cursor()
    username = member;
    print(member)

    sql = "INSERT INTO users (username, exp) VALUES (%s, %s)"
    val = ( username, 0)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

@bot.event
async def on_message(message):
    mycursor = mydb.cursor()

    #User Id wird ausgelesen
    userId = str(message.author.id)
    print(userId)

    #Jetzige Punktzahl wird abgefragt
    mycursor.execute("SELECT points FROM users Where userId = " + userId)
    result = mycursor.fetchall()
    print(result)

    newresult = result + 5

    mycursor.execute("UPDATE users SET points =" + newresult + " WHERE userId =" + userId)
    print(newresult)

#Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('OTAyMTc0MTMwMTc3MjEyNDM2.YXalIg.tFS_YfivuAjPHcPpLNEUTdJZPaA')