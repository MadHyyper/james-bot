import os # Needed for .env
from dotenv import load_dotenv
import random # For the score system
import discord # Necessary library

# Whatever the hell this does lol
intents = discord.Intents.default()
intents.message_content = True

# Get the discord token from the .env
load_dotenv() # Loads .env file
token = os.getenv("DISCORD_TOKEN") # Saves token into a variable

client = discord.Client(intents=intents) # Creates an instance of the client

# Class to save matchup score
class Scores:
    def __init__(self):
        self.james = 200
        self.coleslaw = 200
        
scores = Scores() # Save scores into a variable for later

@client.event
async def on_ready(): # Runs when the bot is turned on
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message): # Triggers for every message received
    if message.author == client.user: # If message comes from itself, skip
        return
    
    if message.content.startswith('Hey James'): # If message content starts with "Hey James" it sends "Hi!"
        await message.channel.send("Hi!")
    
    if message.content.startswith('Whats the score James'): # Tells the score between him and the guy who invented coleslaw
        winner = random.randint(1,3) # selects who won the last matches | 1: James 2: Coleslaw 3: Both
        
        if winner == 1:
            scores.james += random.randint(1,10)
        elif winner == 2:
            scores.coleslaw += random.randint(1,10)
        elif winner == 3:
            scores.james += random.randint(1,10)
            scores.coleslaw += random.randint(1,10)
        
        await message.channel.send('The current score between me and the guy who invented coleslaw is ' + str(scores.james) + ':' + str(scores.coleslaw))
        
        
client.run(token) # Insert token here