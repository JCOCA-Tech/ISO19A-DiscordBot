import discord
from discord.ext import commands
commands = commands.Bot(command_prefix=".")


@commands.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked from the server.')


def setup(bot):
    bot.add_command(kick)
