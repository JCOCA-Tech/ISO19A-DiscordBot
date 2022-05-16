import discord

from discord.ext import commands


# Hilfe Befehl
@commands.command(name='helpcommand')
async def helpcommand(context):
    await context.send(f'```«= Bot Hilfe =»\r\n'
                       '.helpcommand - Zeigt diese Hilfe an\r\n'
                       '.userinfo [Name] - Zeigt Informationen über einen User an\r\n'
                       '.serverinfo - Zeigt Informationen über den Server an\r\n'
                       '.server - Startet einen Web-Server\r\n'
                       '\r\n'
                       '«= Musik Befehle =»\r\n'
                       '.join - Bot joint in den Voice Channel\r\n'
                       '.leave - Bot verlässt den Channel\r\n'
                       '.pause - Song wird pausiert\r\n'
                       '.play - Spiele Song ab\r\n'
                       '.skip - Song überspringen\r\n'
                       '.resume - Setzt den Song fort\r\n'
                       '.stop - Stopt den Song\r\n'
                       '\r\n'
                       '«= Spiele =»\r\n'
                       '.fact - Zeigt verschiedene Fakten an\r\n'
                       '.tictactoe - Spiele TicTacToe\r\n'
                       '.8ball - Spiele 8ball\r\n'
                       '\r\n'
                       '«= Moderation =»\r\n'
                       '.ban [Name] - Bannt einen Spieler vom Server\r\n'
                       '.mute [Name] - Stummt einen Spieler\r\n```'
                       )


def setup(bot):
    bot.add_command(helpcommand)
