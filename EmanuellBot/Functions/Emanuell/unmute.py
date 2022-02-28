from asyncio.tasks import wait
from collections import namedtuple
import discord
from discord import permissions
from discord import role
from discord import guild

from discord.ext import commands
from discord.flags import Intents


@commands.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" you have unmutedd from: - {ctx.guild.name}")
    embed = discord.Embed(
        title="unmute", description=f" unmuted-{member.mention}", colour=discord.Colour.light_gray())
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_command(unmute)
