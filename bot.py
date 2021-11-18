import discord
from discord import message

from discord.ext import commands
import pytz
from datetime import datetime
import json
import os

# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=None)
os.chdir(r'D:\Python-Dev\Bot')


# Meldung wenn der Bot erfolgreich gestartet wurde
@bot.event
async def on_ready():
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')


# Willkommens Nachricht
# Update File wenn Benutzer joint
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(902177572975149126)
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


# Hilfe Befehl
@bot.command(name='help')
async def help(context):
    await context.send(f'```«= Bot Hilfe =»\r\n'
                       '!help - Zeigt diese Hilfe an\r\n'
                       '!userinfo [Name] - Zeigt Informationen über einen User an```')


# User Info Befehl
@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                          description='', color=0x4cd137, timestamp=datetime.now().astimezone(tz=de))

    embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
    embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)
    embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten', value=f'```{member.created_at}```', inline=True)
    embed.add_field(name='Rollen', value=f'```{len(member.roles)}```', inline=True)
    embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
    embed.set_footer(text=f'Angefordert von {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


# Server Info Befehl
@bot.command(name='about')
async def about(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    # Levelsystem


    # Update Punktzahl wenn User schreibt
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



# Client_ID DARF NICHT GEPUSHT WERDEN
bot.run('OTAyMTc0MTMwMTc3MjEyNDM2.YXalIg.fl8P2HRvXiZS4oFLbVBxerCqlH8')
