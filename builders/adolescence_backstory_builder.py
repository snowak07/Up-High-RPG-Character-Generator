from ..models.adolescence_backstory import AdolescenceBackstory, AdolescenceBackstoryEvent
from ..constants import ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP
from ..io.io_handler import IOHandler
import math

class AdolescenceBackstoryBuilder():
    @property
    def io_handler(self) -> IOHandler:
        return self._io_handler

    def __init__(self, io_handler) -> None:
        self._io_handler = io_handler

    async def build(self) -> AdolescenceBackstory:
        potential_backstory_options = self.getAdolescenceEventGroups()
        backstory = await self.promptAdolescenceBackstoryGroup(potential_backstory_options)

        for i in range(0, len(backstory.events)):
            event = backstory.events[i]
            backstory.events[i] = await self.buildAdolescenceBackstoryEvent(event)

        return backstory

    async def promptAdolescenceBackstoryGroup(self, potential_backstory_options: list[AdolescenceBackstory]) -> AdolescenceBackstory:
        await self.io_handler.output("Now moving on to adolescence...\nRoll a d10 to determine your backstory path.")

        roll_result = await self.io_handler.input(min_value=1, max_value=10)
        backstory_path = potential_backstory_options[math.floor((roll_result - 1) / 2)]
        return backstory_path

    def getAdolescenceEventGroups(self) -> list[AdolescenceBackstory]:
        '''Construct list of potential backstory event lists'''
        backstory_event_group_options = []
        for question_group in ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP:
            backstory = AdolescenceBackstory()
            for adolescence_event_data in question_group:
                backstory.addEvent(AdolescenceBackstoryEvent(adolescence_event_data['question'], adolescence_event_data['question_options'], adolescence_event_data['answer_options']))
            backstory_event_group_options.append(backstory)

        return backstory_event_group_options

    async def buildAdolescenceBackstoryEvent(self, backstory_event: AdolescenceBackstoryEvent) -> AdolescenceBackstoryEvent:
        descriptions = [backstory_event.question_options[option] for option in backstory_event.answer_options]
        backstory_event.answer = await self.io_handler.input(
            accepted_values=backstory_event.answer_options, 
            descriptions=descriptions, 
            prompt=backstory_event.question
        )

        await self.io_handler.output("Now roll 2d6 to determine ability increases.\nWhat was the first roll?")
        backstory_event.addRoll(await self.io_handler.input(min_value=1, max_value=6))
        await self.io_handler.output("What was the second roll?")
        backstory_event.addRoll(await self.io_handler.input(min_value=1, max_value=6))

        return backstory_event
