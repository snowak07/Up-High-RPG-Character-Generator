# Unused class
import os

import discord
from discord.ext import commands
from discord import ui
import asyncio

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

@bot.command(name='ping')
async def ping(context):
    print('Successful Ping from ' + context.author.name + '!')
    await context.send('pong ' + context.author.name)

@bot.command(name='select')
async def select(context):
    options = [
        discord.SelectOption(label='Option 1', description='This is option 1'),
        discord.SelectOption(label='Option 2', description='This is option 2'),
    ]
    dropdown = ui.Select(placeholder='Choose an option...', options=options)
    await context.send('Select an option:', view=SelectView())

@bot.tree.command(name='chargen', description='Generate a character')
async def chargen(interaction: discord.Interaction):
    modal = Questionnaire()
    await interaction.response.send_modal(modal)

@bot.tree.command(name='number_input_modal', description='Choose a number')
async def number_input_modal(interaction: discord.Interaction):
    modal = NumberInputModal()
    await interaction.response.send_modal(modal)

# How to chain together prompts?

@bot.command()
async def number_input(context):
    first_num = await d10(context)

def isSameAuthorAndChannel(context, message):
    return message.author == context.author and message.channel == context.channel

async def d10(context):
    await context.send('Please enter a number between 1 and 10:')

    check = lambda message: isSameAuthorAndChannel(context, message)

    try:
        message = await bot.wait_for('message', check=check, timeout=30.0)
        if message.content.isdigit():
            num = int(message.content)
            if 1 <= num <= 10:
                await context.send(f'Thanks for your input: {num}')
                return num
            else:
                await context.send('Please enter a number between 1 and 10.')
        else:
            await context.send('Please enter a valid number.')
    except asyncio.TimeoutError:
        await context.send('You took too long to respond.')

class NumberInputModal(ui.Modal, title='Number Input'):
    number = ui.TextInput(
        label='Enter a number',
        style=discord.TextStyle.short,
        placeholder='Enter a number between 1 and 10',
        min_length=1,
        max_length=2  # Allows for 2-digit numbers
    )
    error_message = ui.TextInput(
        label='',
        style=discord.TextStyle.paragraph,
        placeholder='Error message will appear here',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_item(self.error_message)

    async def on_submit(self, interaction: discord.Interaction):
        if self.number.value.isdigit():
            num = int(self.number.value)
            if 1 <= num <= 10:
                await interaction.response.send_message(f'Thanks for your input: {num}', ephemeral=True)
            else:
                self.error_message.label = 'Error:'
                self.error_message.placeholder = 'Please enter a number between 1 and 10.'
                await interaction.response.edit_message(view=self)
        else:
            self.error_message.label = 'Error:'
            self.error_message.placeholder = 'Please enter a valid number.'
            await interaction.response.edit_message(view=self)

# class NumberInputModal(ui.Modal, title='Number Input'):
#     number = ui.TextInput(
#         label='Enter a number',
#         style=discord.TextStyle.short,
#         placeholder='Enter a number between 1 and 10',
#         min_length=1,
#         max_length=2  # Allows for 2-digit numbers
#     )

#     async def on_submit(self, interaction: discord.Interaction):
#         if self.number.value.isdigit():
#             num = int(self.number.value)
#             if 1 <= num <= 10:
#                 await interaction.response.send_message(f'Thanks for your input: {num}', ephemeral=True)
#             else:
#                 await interaction.response.send_message('Please enter a number between 1 and 10.', ephemeral=True)
#         else:
#             await interaction.response.send_message('Please enter a valid number.', ephemeral=True)

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="This is option 1!"),
            discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
        ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Option 1":
            await interaction.response.edit_message(content="This is the first option from the entire list!")
        elif self.values[0] == "Option 2":
            await interaction.response.send_message("This is the second option from the list entire wooo!",ephemeral=False)
        elif self.values[0] == "Option 3":
            await interaction.response.send_message("Third One!",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

    # options = [
    #     discord.SelectOption(label='Option 1', description='This is option 1'),
    #     discord.SelectOption(label='Option 2', description='This is option 2'),
    # ]
    # dropdown = ui.Select(placeholder='Choose an option...', options=options)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'Thanks for your response, {self.name}! Response is as follows: {self.answer}', 
            ephemeral=True)

bot.run(TOKEN)

### Planning
# Call character_generator_controller.py class to generate the character (and handle the print to file?)
    # Recreate the character generation walkthrough in a discord modal
    # Send data from the modal to the character_generator_controller.py class
        # Might be easier to have an object/class that holds the character data
        # Static class that handles the content of the questions for character generation
        # ToString or print function in character data class
# Send the generated file through discord