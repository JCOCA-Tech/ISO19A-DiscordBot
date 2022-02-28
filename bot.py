import json
import discord

from discord.ext import commands
from levelsystem import update_data

# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=None)

# Meldung wenn der Bot erfolgreich gestartet wurde
@bot.event
async def on_ready():
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')


#Befehl Klassen werden importiert
bot.load_extension("helpCommand")
bot.load_extension("serverinfo")
bot.load_extension("userinfo")

# Willkommens Nachricht
# Update File wenn Benutzer joint
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(886972346336940055)
    embed = discord.Embed(title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    await channel.send(embed=embed)

    print("User gejoint")
    # File wird geöffnet
    with open('users.json', 'r') as f:
        users = json.load(f)
    await update_data(users, member)

    # File wird geschlossen
    with open('users.json', 'w') as f:
        json.dump(users, f)


# Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('OTAyMTc0MTMwMTc3MjEyNDM2.YXalIg.bGFr2BhBB4h2I0x6IUa5I1lzlE8')