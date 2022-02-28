import discord

from discord.ext import commands

import json

# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=None)

#
@bot.event
async def on_message(message):
    # File wird geöffnet
    with open('users.json', 'r') as f:
        users = json.load(f)

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

def setup(bot):
    bot.add_command(help)