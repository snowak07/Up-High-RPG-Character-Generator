from adulthood_backstory import AdulthoodBackstory, AdulthoodBackstoryEvent
from ability_score import AbilityScore
from constants import ABILITY_NAMES, NUM_ADULTHOOD_BACKSTORY_EVENTS, PROFESSIONS, PROFESSION_NAMES, RANDOM_SKILLS
from io_handler import IOHandler

class AdulthoodBackstoryBuilder():
    @property
    def io_handler(self) -> IOHandler:
        return self._io_handler

    def __init__(self, io_handler) -> None:
        self._io_handler = io_handler

    async def build(self, ability_scores) -> AdulthoodBackstory:
        backstory = AdulthoodBackstory()

        await self.presentAdulthoodIntroduction()

        for i in range(1, NUM_ADULTHOOD_BACKSTORY_EVENTS + 1):
            profession = await self.promptAdulthoodProfessionChoice()

            potential_events = self.getAdulthoodProfessionEventList(profession)
            current_event = await self.promptAdulthoodEventRoll(potential_events)

            if current_event.isAbilityTest():
                # Resolve Ability Test
                current_event.passed_test = await self.promptAbilityTest(current_event.scenario, current_event.tested_ability, ability_scores[current_event.tested_ability].value)
            elif current_event.isRandomSkill():
                # Determine Random Skill from roll
                current_event.learned_skill = await self.promptRandomSkill(RANDOM_SKILLS)
            elif current_event.isLearnedSkill():
                # Print out learned skill
                await self.printLearnedSkill(current_event.learned_skill)

            backstory.addEvent(current_event)

        ability_score_dice = {ability_name: ability_score.dice for ability_name, ability_score in ability_scores.items()}
        backstory = await self.handleFinalAbilityRolls(backstory, ability_score_dice)

        return backstory

    def getAdulthoodProfessionEventList(self, profession) -> list[AdulthoodBackstoryEvent]:
        '''Construct list of potential backstory events for chosen profession'''
        potential_events: list[AdulthoodBackstoryEvent] = []
        for potential_event_data in PROFESSIONS[profession]['scenarios']:
            potential_events.append(AdulthoodBackstoryEvent(
                profession,
                potential_event_data['scenario'],
                potential_event_data['tested_ability'] if potential_event_data.get('tested_ability') != None else '',
                potential_event_data['influenced_ability'] if potential_event_data.get('influenced_ability') != None else '',
                potential_event_data['learned_skill'] if potential_event_data.get('learned_skill') != None else ''
            ))

        return potential_events

    async def presentAdulthoodIntroduction(self) -> None:
        await self.io_handler.output("\nNow finishing up with adulthood...")

    async def handleFinalAbilityRolls(self, backstory, ability_score_dice) -> AdulthoodBackstory:
        for ability_name, ability_score_die in ability_score_dice.items():
                additive = await self.promptFinalAbilityRoll(ability_score_die.value, ability_name)
                backstory.addAbilityBonus(ability_name, AbilityScore(ability_name, additive))

        return backstory

    async def promptAdulthoodProfessionChoice(self) -> str:
        return await self.io_handler.input(accepted_values=PROFESSION_NAMES)

    async def promptAdulthoodEventRoll(self, potential_events) -> AdulthoodBackstoryEvent:
        await self.io_handler.output("Roll a d24 (d2 + d12):")
        roll_result = await self.io_handler.input(min_value=1, max_value=24)
        return potential_events[roll_result - 1]

    async def promptAbilityTest(self, scenario, tested_ability, tested_ability_score) -> bool:
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

    async def printLearnedSkill(self, learned_skill) -> None:
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