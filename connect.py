import os

import discord
from dotenv import load_dotenv
import random
import test


load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['GUILD']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    temp = test.piazza_parse(message.content)

    if "piazza.com" in message.content:
        response = temp
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!\n')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to the following guild: {guild.name}(id: {guild.id})')

client.run(TOKEN)