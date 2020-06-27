import os, discord, random, test
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['GUILD']

client = discord.Client()

@client.event
async def on_message(message):
    '''
    For every new message on the server, on_message() is called
    with the messaged passed in.
    '''

    # Ignore the bots own messages to the server
    if message.author == client.user:
        return

    # brooklyn 99 quotes just for fun
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    # If message is a piazza link, call test.piazza_parse()
    # Then send piazza post to server
    if "piazza.com" in message.content:
        response = test.piazza_parse(message.content)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_ready():
    '''
    Prints to console when bot is connected to Discord and server.
    '''
    print(f'{client.user} has connected to Discord!\n')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to the following guild: {guild.name}(id: {guild.id})')

client.run(TOKEN)