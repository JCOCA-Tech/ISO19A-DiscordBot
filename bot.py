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
    channel = bot.get_channel(902176471844540486)
    embed = discord.Embed(title="Willkommen!", description=f"{member.mention} ist unserem Server beigetreten")
    await channel.send(embed=embed)

#Levelsystem
@bot.event
async def on_message(message):
    # File wird geöffnet
    print(f'Test 1')

    with open('users.json', 'r') as f:
        users = json.load(f)

        print(f'Test 2')

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

        # File wird geschlossen
        with open('users.json', 'w') as f:
            json.dump(users, f)


async def update_data(users, user):
    if not user.id in users:
        users[user.id] = []
        user[user.id]['experience'] = 0
        users[user.id]['level'] = 1


async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp


async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1 / 4))

    if lvl_start < lvl_end:
        await bot.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end

# Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('')