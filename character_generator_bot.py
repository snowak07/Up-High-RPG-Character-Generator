import math
import os
from adolescence_backstory import AdolescenceBackstory, AdolescenceBackstoryEvent
from adulthood_backstory import AdulthoodBackstoryEvent
from character_sheet import AbilityScore
from childhood_backstory import ChildhoodBackstoryEvent
from constants import PROFESSION_NAMES
from io_handler import IOHandler

class CharacterGeneratorBot():
    @property
    def io_handler(self) -> IOHandler:
        return self._io_handler

    def __init__(self, io_handler):
        self._io_handler = io_handler

    async def presentBackstorySummarizeLoadingAlert(self):
        await self.io_handler.output('Summarizing your character\'s backstory...')

    async def presentAdulthoodIntroduction(self):
        await self.io_handler.output("\nNow finishing up with adulthood...")

    async def promptCharacterName(self):
        await self.io_handler.output("What is your character's name?")
        return await self.io_handler.input()

    async def promptChildhoodStatRoll(self, ability: str, backstory_event_options: list[ChildhoodBackstoryEvent]):
        await self.io_handler.output('Roll a d12 for ' + ability + '.')

        roll_result = await self.io_handler.input(min_value=1, max_value=12)
        backstory_event = backstory_event_options[roll_result - 1]
        await self.io_handler.output(backstory_event.lore)
        return backstory_event

    async def promptAdolescenceBackstoryGroup(self, potential_backstory_options: list[AdolescenceBackstory]):
        await self.io_handler.output("Now moving on to adolescence...\nRoll a d10 to determine your backstory path.")

        roll_result = await self.io_handler.input(min_value=1, max_value=10)
        backstory_path = potential_backstory_options[math.floor((roll_result - 1) / 2)]
        return backstory_path

    async def promptAdolescenceBackstoryEvent(self, backstory_event: AdolescenceBackstoryEvent) -> list[AbilityScore]:
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

    async def promptAdulthoodProfessionChoice(self):
        return await self.io_handler.input(accepted_values=PROFESSION_NAMES)

    async def promptAdulthoodEventRoll(self, potential_events) -> AdulthoodBackstoryEvent:
        await self.io_handler.output("Roll a d24 (d2 + d12):")
        roll_result = await self.io_handler.input(min_value=1, max_value=24)
        return potential_events[roll_result - 1]

    async def promptAbilityTest(self, scenario, tested_ability, tested_ability_score):
        await self.io_handler.output(f"{scenario} [{tested_ability} ({tested_ability_score})] (Roll a d12):")
        roll_result = await self.io_handler.input(min_value=1, max_value=12)
        test_result = roll_result <= tested_ability_score
        if test_result:
            await self.io_handler.output("Success!")
        else:
            await self.io_handler.output("Failure!")

        return test_result

    async def promptRandomSkill(self, skill_options) -> str:
        await self.io_handler.output("Roll a d100:")
        roll_result = await self.io_handler.input(min_value=1, max_value=100)
        learned_skill = skill_options[roll_result - 1]
        await self.printLearnedSkill(learned_skill)
        return learned_skill

    async def printLearnedSkill(self, learned_skill):
        await self.io_handler.output(f"You learned {learned_skill}!")

    async def promptFinalAbilityRoll(self, adv_disadv_dice, ability_name) -> int:
        advantage = adv_disadv_dice > 0
        disadvantage = adv_disadv_dice < 0
    
        prompt = f"({ability_name}) Roll "
        prompt += str(abs(adv_disadv_dice) + 1) + "d6 "
        prompt += "take the highest" if advantage else "take the lowest" if disadvantage else ""
    
        await self.io_handler.output(prompt)
        roll_result = await self.io_handler.input(min_value=1, max_value=6)
        return roll_result

    async def printCharacterToFile(self, file):
        return await self.io_handler.output("", file=file)