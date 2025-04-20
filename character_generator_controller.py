from character_sheet import CharacterSheet
from adolescence_backstory_builder import AdolescenceBackstoryBuilder
from adulthood_backstory_builder import AdulthoodBackstoryBuilder
from childhood_backstory_builder import ChildhoodBackstoryBuilder
from io_handler import IOHandler

gpt_provider_enabled = True
try:
    import gpt_provider
except ImportError:
    gpt_provider_enabled = False

class CharacterGeneratorController:
    def __init__(self, io_handler: IOHandler) -> None:
        self._io_handler = io_handler

    @property
    def io_handler(self) -> IOHandler:
        return self._io_handler

    async def start(self) -> None:
        await self.io_handler.output("What is your character's name?")
        character_sheet = CharacterSheet(await self.io_handler.input())

        character_sheet.addChildhoodBackstory(await ChildhoodBackstoryBuilder(self.io_handler).build())
        character_sheet.addAdolescenceBackstory(await AdolescenceBackstoryBuilder(self.io_handler).build())
        character_sheet.addAdulthoodBackstory(await AdulthoodBackstoryBuilder(self.io_handler).build(character_sheet.getAbilityScores()))

        await self.io_handler.output('Summarizing your character\'s backstory...')
        await character_sheet.summarizeBackstory()

        await self.io_handler.outputFile(str(character_sheet), character_sheet.name)