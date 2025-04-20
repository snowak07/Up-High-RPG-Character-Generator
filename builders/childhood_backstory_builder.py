from constants import ABILITY_NAMES, CHILDHOOD_ROLL_MAPS
from ..models.childhood_backstory import ChildhoodBackstory, ChildhoodBackstoryEvent
from ..io.io_handler import IOHandler

class ChildhoodBackstoryBuilder():
    @property
    def io_handler(self) -> IOHandler:
        return self._io_handler

    def __init__(self, io_handler) -> None:
        self._io_handler = io_handler

    async def build(self) -> ChildhoodBackstory:
        backstory = ChildhoodBackstory()
        for ability in ABILITY_NAMES:
            backstory.addEvent(await self.buildChildhoodEvent(ability))

        return backstory

    async def buildChildhoodEvent(self, ability: str) -> ChildhoodBackstoryEvent:
        '''Prompt user for childhood event roll and return the event'''
        backstory_event_options = self.getChildhoodBackstoryEventList(ability)
        backstory_event = await self.promptChildhoodStatRoll(ability, backstory_event_options)

        return backstory_event

    def getChildhoodBackstoryEventList(self, ability) -> list[ChildhoodBackstoryEvent]:
        return [ChildhoodBackstoryEvent(ability, backstory_event['bonus'], backstory_event['lore']) for backstory_event in CHILDHOOD_ROLL_MAPS[ability]]

    async def promptChildhoodStatRoll(self, ability: str, backstory_event_options: list[ChildhoodBackstoryEvent]) -> ChildhoodBackstoryEvent:
        await self.io_handler.output(f'Roll a d12 for {ability}.')

        roll_result = await self.io_handler.input(min_value=1, max_value=12)
        backstory_event = backstory_event_options[roll_result - 1]
        await self.io_handler.output(backstory_event.lore)
        return backstory_event
