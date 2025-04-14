import discord
import os
import random
from discord_io_handler import DiscordIOHandler

class DiscordIOHandlerTest(DiscordIOHandler):
    async def initialize(self) -> None:
        await self.interaction.response.send_message("Generating Character.....")

    async def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt="") -> None:
        if min_value and max_value:
            return random.randint(min_value, max_value)
        elif accepted_values:
            return accepted_values[random.randint(0, len(accepted_values) - 1)]
        else:
            return "foobar"

    async def output(self, content, *, view=None, file=None) -> None:
        if file:
            await self.interaction.followup.send(
                    content,
                    file=discord.File(file, filename=os.path.basename(file.name))
                )