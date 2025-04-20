import discord
from io.io_handler import IOHandler

EMOJI_MAP = {
    "STR": "💪",
    "DEX": "🤸",
    "CON": "🛡️",
    "INT": "🧠",
    "WIS": "🦉",
    "CHA": "🎭",
    "Army": "🛡️",
    "Clergy": "⛪",
    "Criminal": "🕶️",
    "Forest": "🌲",
    "Noble": "👑",
    "Rural": "🌾",
    "Town": "🏘️",
    "Wizard's Apprentice": "🧙‍♂️"
}

class DiscordIOHandler(IOHandler):
    @property
    def bot(self) -> discord.ext.commands.Bot:
        return self._bot

    @property
    def interaction(self) -> discord.Interaction:
        return self._interaction

    def __init__(self, bot: discord.ext.commands.Bot, interaction: discord.Interaction) -> None:
        self._bot = bot
        self._interaction = interaction

    async def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt="") -> str | int:
        if min_value != None and max_value != None:
            return await self.__inputInt(min_value, max_value)
        elif accepted_values != None:
            view = SelectView(accepted_values=accepted_values, descriptions=descriptions, prompt=prompt)
            await self.output("", view=view)

            await view.wait()

            return view.select.selected_value
        else:
            return await self.__inputString()

    async def __inputInt(self, min_value, max_value) -> int:
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        if message.content.isdigit():
            num = int(message.content)
            if min_value <= num <= max_value:
                return int(num)
            else:
                await self.output(f'Please enter a number between {min_value} and {max_value}.')
                return await self.__inputInt(min_value, max_value)
        else:
            await self.output('Please enter a valid roll result.')
            return await self.__inputInt(min_value, max_value)

    async def __inputString(self) -> str:
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        return message.content.strip()

    async def output(self, content, *, view=None) -> None:
        if view:
            await self.send(content=content, view=view, ephemeral=True)
        else:
            await self.send(content=content, ephemeral=True)

    async def outputFile(self, content, filename) -> None:
        file_location = self.saveFile(content, filename)
        await self.send(file=discord.File(file_location))

    def isSameAuthorAndChannel(self, message) -> bool:
        if hasattr(message, "author"):
            return message.author == self.interaction.user and message.channel == self.interaction.channel
        else:
            return message.user == self.interaction.user and message.channel == self.interaction.channel

    async def send(self, *, content=None, view=None, file=None, ephemeral=None):
        args = {
            "content": content,
            "view": view,
            "file": file,
            "ephemeral": ephemeral
        }

        # Filter out any arguments with a value of None
        args = {key: value for key, value in args.items() if value is not None}

        if not self.interaction.response.is_done():
            await self.interaction.response.send_message(**args)

        else:
            await self.interaction.followup.send(**args)

class SelectComponent(discord.ui.Select):
    def __init__(self, options: list[str], descriptions: list[str] = None, question: str = "") -> None:
        self.selected_value = ""
        self.question = question
        self.descriptions = descriptions
        if descriptions is None:
            self.descriptions = [""] * len(options)

        select_component_options = []
        for i in range(len(options)):
            emoji = EMOJI_MAP[options[i]]
            option_value = options[i]
            description = self.descriptions[i]
            select_component_options.append(discord.SelectOption(label=option_value, emoji=emoji, description=description))

        super().__init__(placeholder="Choose an option", max_values=1, min_values=1, options=select_component_options)

    async def callback(self, interaction: discord.Interaction) -> None:
        self.selected_value = self.values[0]
        after_interaction_content_edit = self.question
        if self.descriptions[0] != "":
            after_interaction_content_edit += "\n - " + "\n - ".join(description for description in self.descriptions)
        after_interaction_content_edit += "\nYou chose: " + self.selected_value

        await interaction.response.edit_message(content=after_interaction_content_edit, view=None)
        self.view.stop()

class SelectView(discord.ui.View):
    def __init__(self, *, accepted_values=None, descriptions=None, prompt="", timeout = 180) -> None:
        super().__init__(timeout=timeout)
        self.select = SelectComponent(accepted_values, descriptions, prompt)
        self.add_item(self.select)