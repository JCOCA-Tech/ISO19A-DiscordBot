import discord
import mysql.connector

from discord.ext import commands

# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=None)

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

@bot.event
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
        mycursor.execute(sql)

#Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('')