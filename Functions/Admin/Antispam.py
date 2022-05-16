from asyncio.tasks import wait
from collections import namedtuple
import discord
from discord import permissions
from discord import role
from discord import guild
import datetime
import time
from discord.flags import Intents
from discord.ext import commands
import asyncio

time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
# Struct:
# {
#    "<author_id>": ["<msg_time", "<msg_time>", ...],
#    "<author_id>": ["<msg_time"],
# }


@commands.command(description="Detects spam")
async def on_message(ctx):
    global author_msg_counts
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    author_id = ctx.author.id
    # Get current epoch time in milliseconds
    curr_time = datetime.datetime.now().timestamp() * 500

    # Make empty list for author id, if it does not exist
    if not author_msg_times.get(author_id, False):
        author_msg_times[author_id] = []

    # Append the time of this message to the users list of message times
    author_msg_times[author_id].append(curr_time)

    # Find the beginning of our time window.
    expr_time = curr_time - time_window_milliseconds

    # Find message times which occurred before the start of our window
    expired_msgs = [
        msg_time for msg_time in author_msg_times[author_id]
        if msg_time < expr_time
    ]

    # Remove all the expired messages times from our list
    for msg_time in expired_msgs:
        author_msg_times[author_id].remove(msg_time)
    # ^ note: we probably need to use a mutex here. Multiple threads
    # might be trying to update this at the same time. Not sure though.

    if len(author_msg_times[author_id]) > max_msg_per_window:
        await ctx.author.send("If you spam again you getting banned")
        await ctx.send(ctx.author.id, reason="Stop Spamming")
        await ctx.guild.ban(ctx.author, reason="Spamming")
        await asyncio.sleep(1)
        await ctx.guild.unban(ctx.author)


def setup(bot):
    bot.add_command(on_message)
