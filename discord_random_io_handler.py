import random
from discord_io_handler import DiscordIOHandler

class DiscordRandomIOHandler(DiscordIOHandler):
    async def initialize(self) -> None:
        await self.interaction.response.send_message("Generating Character.....")

    async def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt="") -> None:
        if min_value and max_value:
            return random.randint(min_value, max_value)
        elif accepted_values:
            return accepted_values[random.randint(0, len(accepted_values) - 1)]
        else:
            return "foobar"

    async def output(self, content, *, view=None) -> None:
        # No output when randomly generating character
        return