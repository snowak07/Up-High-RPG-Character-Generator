# TODO: Handle loading already generated characters (from file?)
# TODO: Add GPT backstroy summary option to character generation
# TODO: Print to file
# TODO: db class that handles retrieving of database data (constants file right now) (like BackstoryEvent lists)
import constants
import character_generator_bot
import discord
import math
import sys
from backstory_event_provider import BackstoryEventProvider
from childhood_backstory import ChildhoodBackstoryEvent
from adolescence_backstory import AdolescenceBackstory, AdolescenceBackstoryEvent
from adulthood_backstory import AdulthoodBackstoryEvent
from character_sheet import CharacterSheet
from character_generator_bot import CharacterGeneratorBot

gpt_provider_enabled = True
try:
    import gpt_provider
except ImportError:
    gpt_provider_enabled = False

class CharacterGeneratorController:
    def __init__(self, bot: discord.ext.commands.Bot, interaction: discord.Interaction):
        self._character_generator_bot = CharacterGeneratorBot(bot, interaction)

    @property
    def character_generator_bot(self) -> CharacterGeneratorBot:
        return self._character_generator_bot

    async def start(self):
        character_sheet = CharacterSheet(await self.character_generator_bot.promptCharacterName())

        character_sheet = await self.establishChildhood(character_sheet)
        character_sheet = await self.establishAdolescence(character_sheet)
        character_sheet = await self.establishAdulthood(character_sheet)

        # await self.character_generator_bot.print(str(character_sheet))
        await self.printCharacterToFile(character_sheet)

    async def establishChildhood(self, character_sheet):
        for ability in constants.ABILITY_NAMES:
            character_sheet.addChildhoodEvent(await self.establishChildhoodEvent(ability))

        return character_sheet

    async def establishChildhoodEvent(self, ability: str) -> ChildhoodBackstoryEvent:
        '''Prompt user for childhood event roll and return the event'''
        backstory_event_options = BackstoryEventProvider.getChildhoodBackstoryEventList(ability)
        backstory_event = await self.character_generator_bot.promptChildhoodStatRoll(ability, backstory_event_options)

        return backstory_event

    async def establishAdolescence(self, character_sheet):
        potential_backstory_options = BackstoryEventProvider.getAdolescenceEventGroups()
        unresolved_backstory = await self.character_generator_bot.promptAdolescenceBackstoryGroup(potential_backstory_options)

        for event in unresolved_backstory.events:
            character_sheet.addAdolescenceEvent(await self.character_generator_bot.promptAdolescenceBackstoryEvent(event))

        return character_sheet

    async def establishAdulthood(self, character_sheet):
        await self.character_generator_bot.print("\nNow finishing up with adulthood...")

        for i in range(1, constants.NUM_ADULTHOOD_BACKSTORY_EVENTS + 1):
            profession = await self.character_generator_bot.promptAdulthoodProfessionChoice()

            potential_events = BackstoryEventProvider.getAdulthoodProfessionEventList(profession)
            current_event = await self.character_generator_bot.promptAdulthoodEventRoll(potential_events)

            if current_event.isAbilityTest():
                # Resolve Ability Test
                current_event.passed_test = await self.character_generator_bot.promptAbilityTest(current_event.scenario, current_event.tested_ability, getattr(character_sheet, current_event.tested_ability).value)
            elif current_event.isRandomSkill():
                # Determine Random Skill from roll
                current_event.learned_skill = await self.character_generator_bot.promptRandomSkill(constants.RANDOM_SKILLS)
            elif current_event.isLearnedSkill():
                # Print out learned skill
                await self.character_generator_bot.printLearnedSkill(current_event.learned_skill)

            character_sheet.addAdulthoodEvent(current_event)

        character_sheet = await self.handleFinalAbilityRolls(character_sheet)

        return character_sheet

    async def handleFinalAbilityRolls(self, character_sheet):
        for ability in constants.ABILITY_NAMES:
                ability_score: AbilityScore = getattr(character_sheet, ability)
                additive = await self.character_generator_bot.promptFinalAbilityRoll(ability_score.dice.value, ability_score.name)
                ability_score.add(additive)

        return character_sheet

    async def printCharacterToFile(self, character_sheet):
        # Save to server
        write_file = open("generated_characters/" + character_sheet.name + ".txt", "w")
        print(str(character_sheet), file=write_file)
        write_file.close()

        # Send to user over discord
        read_file = open("generated_characters/" + character_sheet.name + ".txt", "r")
        await self.character_generator_bot.printFile(read_file)
        read_file.close()