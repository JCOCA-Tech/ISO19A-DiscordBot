import discord, random
from discord.ext import commands

# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)

# 8Ball command
@commands.command(name='_ball')
async def _ball(ctx):
    # Magic 8 ball function
    positive_responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes."
    ]
    neutral_responses = [
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
    ]
    negative_responses = [
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    # Generate return value
    responses = positive_responses+neutral_responses+negative_responses
    message = random.choice(responses)
    # directly send the embed and return
    await ctx.send(embed=embed("8 Ball","",message,color=0x2211EE))

def setup(bot):
    bot.add_command(_ball)
    
