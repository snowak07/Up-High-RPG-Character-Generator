import os
import discord
from discord.ext import commands
from discord import ui
import asyncio
from character_generator_controller import CharacterGeneratorController

TOKEN = os.environ['DISCORD_PYTHON_API_KEY']

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name='ping')
async def ping(interaction: discord.Interaction):
    print('Successful Ping from ' + interaction.client.user.name + '!')
    await interaction.response.send_message('pong ' + interaction.client.user.name)

@bot.tree.command(name='chargen', description='Generate a character')
async def chargen(interaction: discord.Interaction):
    controller = CharacterGeneratorController(bot, interaction)
    await controller.start()

bot.run(TOKEN)