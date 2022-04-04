import json
import discord

from discord.ext import commands

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
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(902176471844540486)
    embed = discord.Embed(title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    await channel.send(embed=embed)


# Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('OTAyMTc0MTMwMTc3MjEyNDM2.YXalIg.xKy78PrGbZ06PB-6QMBHgNBrZGA')