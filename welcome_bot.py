# This file will be used for the Welcome Bot to welcome new members into the server
import os
import discord

from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents().all()
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')
GUILDS = os.getenv('DISCORD_GUILD')
# GUILDS = os.getenv('DISCORD_SERVER_LIST').split(',')

@client.event
async def on_ready():
    # These next lines are going to be the confirmation process of which servers this bot is connected to as well as
    # verifying the count of total servers it's connected to
    server_count = 0

    # Here we're stating that the bot has connected to all servers and printing out all servers it's connected to
    print(f'user named {client.user.name} has connected to all associated Discord servers!')
    connected_servers = '\n '.join([f'{(server_count := server_count + 1)}. {server.name}'for server in client.guilds])
    print(f"Our bot {client.user.name} is associated with {server_count} servers: \n {connected_servers}")

# This event function will send a message to the specified channel when a new user joins the server
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome-bot")
    await channel.send(f'Everyone get a load of the newcomer <@{member.id}>, Welcome!')

# This event function will send a message to the specified channel when a user leaves the server
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome-bot")
    await channel.send(f'Sorry to see you go <@{member.id}> :cry: ')

# Run the client Bot utilizing the provided TOKEN
client.run(TOKEN)
