import os
import discord
from discord.ext import commands
from .builders.character_sheet_builder import CharacterSheetBuilder
from .io.discord_io_handler import DiscordIOHandler
from .io.discord_random_io_handler import DiscordRandomIOHandler

TOKEN = os.environ['DISCORD_PYTHON_API_KEY']

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready() -> None:
    print(f'{bot.user.name} has connected to Discord!')

    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name='ping')
async def ping(interaction: discord.Interaction) -> None:
    print('Successful Ping from ' + interaction.client.user.name + '!')
    await interaction.response.send_message('pong ' + interaction.client.user.name, ephemeral=True)

@bot.tree.command(name='chargen', description='Generate a character')
async def chargen(interaction: discord.Interaction) -> None:
    discord_io_handler = DiscordIOHandler(bot, interaction)
    controller = CharacterSheetBuilder(discord_io_handler)
    await controller.start()

@bot.tree.command(name='randchargen', description='Randonly generate a character')
async def chargen(interaction: discord.Interaction) -> None:
    discord_random_io_handler = DiscordRandomIOHandler(bot, interaction)
    await discord_random_io_handler.initialize()
    controller = CharacterSheetBuilder(discord_random_io_handler)
    await controller.start()

bot.run(TOKEN)