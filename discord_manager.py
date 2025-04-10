class DiscordManager():
    _instance = None

    @property
    def bot(self) -> discord.ext.commands.Bot:
        return self._bot

    @property
    def interaction(self) -> discord.Interaction:
        return self._interaction

    def __new__(cls, *args, **kwargs):
        # Ensure only one instance is created (Singleton)
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, bot: discord.ext.commands.Bot, interaction: discord.Interaction):
        if not hasattr(self, '_bot'):
            self._bot = bot
        if not hasattr(self, '_interaction'):
            self._interaction = interaction

    async def print(self, content, view=discord.ui.View(), file=None):
        if not self.interaction.response.is_done():
            if file is None:
                await self.interaction.response.send_message(content, view=view, ephemeral=True)
            else:
                await self.interaction.response.send_message(
                    content,
                    view=view,
                    file=discord.File(file, filename=os.path.basename(file.name))
                )
        else:
            if file is None:
                await self.interaction.followup.send(content, view=view, ephemeral=True)
            else:
                # Not ephemeral when sending files so anyone can see them.
                await self.interaction.followup.send(
                    message,
                    view=view,
                    file=discord.File(file, filename=os.path.basename(file.name))
                )

    def isSameAuthorAndChannel(self, message):
        if hasattr(message, "author"):
            return message.author == self.interaction.user and message.channel == self.interaction.channel
        else:
            return message.user == self.interaction.user and message.channel == self.interaction.channel

    async def waitForAndValidateIntInput(self, min_value, max_value) -> int:
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        if message.content.isdigit():
            num = int(message.content)
            if min_value <= num <= max_value:
                return int(num)
            else:
                await self.print(f'Please enter a number between {min_value} and {max_value}.')
                return await self.waitForAndValidateIntInput(min_value, max_value)
        else:
            await self.print('Please enter a valid roll result.')
            return await self.waitForAndValidateIntInput(min_value, max_value)

    async def waitForAndValidateStringInput(self):
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        return message.content.strip()