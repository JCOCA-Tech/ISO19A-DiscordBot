import discord
import pytz
from datetime import datetime

from discord.ext import commands


# Bot wird definiert, Prefix für Befehle wird festgelegt, Hilfe Befehl wird deaktiviert
bot = commands.Bot(intents=discord.Intents.all(),
                   command_prefix=".", help_command=None)

# User Info Befehl


@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                          description='', color=0x4cd137, timestamp=datetime.now().astimezone(tz=de))

    embed.add_field(
        name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(
        name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
    embed.add_field(
        name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)
    embed.add_field(name='Server beigetreten',
                    value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten',
                    value=f'```{member.created_at}```', inline=True)
    embed.add_field(
        name='Rollen', value=f'```{len(member.roles)}```', inline=True)
    embed.add_field(name='Höchste Rolle',
                    value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(
        name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
    embed.set_footer(
        text=f'Angefordert von {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_command(userinfo)
