# TODO What imports are required?
# TODO type hinting for all functions
import discord
from character_sheet import AbilityScore
from childhood_backstory import ChildhoodBackstoryEvent
from adolescence_backstory import AdolescenceBackstory, AdolescenceBackstoryEvent
from adulthood_backstory import AdulthoodBackstoryEvent
from constants import PROFESSION_NAMES
import math
import os

ABILITY_EMOJI_MAP = {
    "STR": "💪",
    "DEX": "🤸",
    "CON": "🛡️",
    "INT": "🧠",
    "WIS": "🦉",
    "CHA": "🎭"
}

PROFESSION_EMOJI_MAP = {
    "Army": "🛡️",
    "Clergy": "⛪",
    "Criminal": "🕶️",
    "Forest": "🌲",
    "Noble": "👑",
    "Rural": "🌾",
    "Town": "🏘️",
    "Wizard's Apprentice": "🧙‍♂️"
}

class CharacterGeneratorBot():
    def __init__(self, bot: discord.ext.commands.Bot, interaction: discord.Interaction):
        self._bot = bot
        self._interaction = interaction

    @property
    def bot(self) -> discord.ext.commands.Bot:
        return self._bot

    @property
    def interaction(self) -> discord.Interaction:
        return self._interaction

    async def print(self, string):
        await self.interaction.followup.send(string)

    async def printFile(self, file, message = ""):
        await self.interaction.followup.send(message, file=discord.File(file, filename=os.path.basename(file.name)))

    def isSameAuthorAndChannel(self, message):
        if hasattr(message, "author"):
            return message.author == self.interaction.user and message.channel == self.interaction.channel
        else:
            return message.user == self.interaction.user and message.channel == self.interaction.channel

    async def promptCharacterName(self):
        await self.interaction.response.send_message("What is your character's name?")
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        return message.content

    async def promptChildhoodStatRoll(self, ability: str, backstory_event_options: list[ChildhoodBackstoryEvent]):
        await self.interaction.followup.send('Roll a d12 for ' + ability + '.')

        roll_result = await self.waitForAndValidateIntInput(1, 12)
        backstory_event = backstory_event_options[roll_result - 1]
        await self.interaction.followup.send(backstory_event.lore)
        return backstory_event

    async def promptAdolescenceBackstoryGroup(self, potential_backstory_options: list[AdolescenceBackstory]):
        await self.interaction.followup.send("Now moving on to adolescence...\nRoll a d10 to determine your backstory path.")

        roll_result = await self.waitForAndValidateIntInput(1, 10)
        backstory_path = potential_backstory_options[math.floor((roll_result - 1) / 2)]
        return backstory_path

    async def promptAdolescenceBackstoryEvent(self, backstory_event: AdolescenceBackstoryEvent) -> list[AbilityScore]:
        view = AdolescenceEventAnswerSelectView(backstory_event)
        await self.interaction.followup.send(backstory_event.question, view=view)

        await view.wait()

        backstory_event.answer = view.select.backstory_event.answer

        await self.interaction.followup.send("Now roll 2d6 to determine ability increases.\nWhat was the first roll?", ephemeral=True)
        backstory_event.addRoll(await self.waitForAndValidateIntInput(1, 6))
        await self.interaction.followup.send("What was the second roll?", ephemeral=True)
        backstory_event.addRoll(await self.waitForAndValidateIntInput(1, 6))

        return backstory_event

    async def promptAdulthoodProfessionChoice(self):
        view = AdulthoodProfessionSelectView()
        await self.interaction.followup.send(view=view)

        await view.wait()

        return view.select.profession_choice

    async def promptAdulthoodEventRoll(self, potential_events) -> AdulthoodBackstoryEvent:
        await self.interaction.followup.send("Roll a d24 (d2 + d12):")
        roll_result = await self.waitForAndValidateIntInput(1, 24)
        return potential_events[roll_result - 1]

    async def promptAbilityTest(self, scenario, tested_ability, tested_ability_score):
        # Need tested_ability score from character_sheet
        await self.interaction.followup.send(f"{scenario} [{tested_ability} ({tested_ability_score})] (Roll a d12):")
        roll_result = await self.waitForAndValidateIntInput(1, 12)
        test_result = roll_result <= tested_ability_score
        if test_result:
            await self.interaction.followup.send("Success!")
        else:
            await self.interaction.followup.send("Failure!")

        return test_result

    async def promptRandomSkill(self, skill_options) -> str:
        await self.interaction.followup.send("Roll a d100:")
        roll_result = await self.waitForAndValidateIntInput(1, 100)
        learned_skill = skill_options[roll_result - 1]
        await self.printLearnedSkill(learned_skill)
        return learned_skill

    async def printLearnedSkill(self, learned_skill):
        await self.interaction.followup.send(f"You learned {learned_skill}!")

    async def promptFinalAbilityRoll(self, adv_disadv_dice, ability_name) -> int:
        advantage = adv_disadv_dice > 0
        disadvantage = adv_disadv_dice < 0
    
        prompt = f"({ability_name}) Roll "
        prompt += str(abs(adv_disadv_dice) + 1) + "d6 "
        prompt += "take the highest" if advantage else "take the lowest" if disadvantage else ""
    
        await self.interaction.followup.send(prompt)
        roll_result = await self.waitForAndValidateIntInput(1, 6)
        return roll_result

    async def waitForAndValidateIntInput(self, min_value, max_value) -> int:
        message = await self.bot.wait_for('message', check=self.isSameAuthorAndChannel)
        if message.content.isdigit():
            num = int(message.content)
            if min_value <= num <= max_value:
                return int(num)
            else:
                await self.interaction.followup.send(f'Please enter a number between {min_value} and {max_value}.')
                return await self.waitForAndValidateIntInput(min_value, max_value)
        else:
            await self.interaction.followup.send('Please enter a valid roll result.')
            return await self.waitForAndValidateIntInput(min_value, max_value)

class AdolescenceEventAnswerSelect(discord.ui.Select):
    def __init__(self, backstory_event: AdolescenceBackstoryEvent):
        self.backstory_event = backstory_event # Store event

        options = []
        for i in range(len(backstory_event.answer_options)):
            emoji = ABILITY_EMOJI_MAP[backstory_event.answer_options[i]]
            ability_score_option = backstory_event.answer_options[i]
            options.append(discord.SelectOption(label=ability_score_option, emoji=emoji, description=backstory_event.question_options[ability_score_option]))

        super().__init__(placeholder="Choose an option", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        self.backstory_event.answer = self.values[0]
        after_interaction_content_edit = self.backstory_event.question
        after_interaction_content_edit += "\n - " + "\n - ".join(self.backstory_event.question_options[answer_option] for answer_option in self.backstory_event.answer_options)
        after_interaction_content_edit += "\nYou chose: " + self.backstory_event.answer

        await interaction.response.edit_message(content=after_interaction_content_edit, view=None)
        self.view.stop()

class AdolescenceEventAnswerSelectView(discord.ui.View):
    def __init__(self, backstory_event, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.select = AdolescenceEventAnswerSelect(backstory_event)
        self.add_item(self.select)

class AdulthoodProfessionSelect(discord.ui.Select):
    def __init__(self):
        self.profession_choice = ""

        options = []
        for i in range(len(PROFESSION_NAMES)):
            emoji = PROFESSION_EMOJI_MAP[PROFESSION_NAMES[i]]
            options.append(discord.SelectOption(label=PROFESSION_NAMES[i], emoji=emoji))

        super().__init__(placeholder="Choose a profession", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        self.profession_choice = self.values[0]
        await interaction.response.edit_message(content=f"Selected Profession: {self.values[0]}", view=None)
        self.view.stop()

class AdulthoodProfessionSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.select = AdulthoodProfessionSelect()
        self.add_item(self.select)