import discord
import openai
import os
from dotenv import load_dotenv
from discord.ext import commands
# Connect to the OpenAI API using your API key
openai.api_key = "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"

# Create a client instance of Discord.py
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>',intents=intents)

# Event listener that listens for messages sent to the bot

@client.event 
async def on_ready():
    print('the bot is on')
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    # Send the message to OpenAI API for processing
    response = openai.Completion.create(
        engine="davinci", # Choose the OpenAI GPT model to use
        prompt=message.content, # Use the message content as prompt for GPT
        max_tokens=250 # Set the maximum number of tokens GPT can generate
    )

    # Send the response received from OpenAI API to the channel where the message was sent
    await message.channel.send(response.choices[0].text)

# Connect the bot to Discord using the bot token
load_dotenv()

client.run(os.environ['TOKEN'])
