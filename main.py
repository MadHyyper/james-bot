import os # Needed for .env
from dotenv import load_dotenv
import discord # Necessary library

# Whatever the hell this does lol
intents = discord.Integration.default()
intents.message_content = True

# Get the discord token from the .env
load_dotenv() # Loads .env file
token = os.getenv("DISCORD_TOKEN") # Saves token into a variable

client = discord.Client(intents=intents) # Creates an instance of the client

@client.event
async def on_ready(): # Runs when the bot is turned on
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message): # Triggers for every message received
    if message.author == client.user: # If message comes from itself, skip
        return
    
    if message.content.startswith('Hey James'): # If message content starts with "Hey James" it sends "Hi!"
        await message.channel.send("Hi!")
        
client.run("token") # Insert token here