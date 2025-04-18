from ability_score import AbilityScore
from backstory import Backstory
from constants import ABILITY_NAMES

class CharacterSheet:
    def __init__(self, name: str) -> None:
        self._name = name
        self._HP = 0
        self._skills = []
        self._summary = ""
        [setattr(self, ability, AbilityScore(ability)) for ability in ABILITY_NAMES]
        self.backstory = Backstory()

    async def summarizeBackstory(self) -> None:
        await self.backstory.summarize()

    @property
    def name(self) -> str:
        return self._name

    @property
    def HP(self) -> int:
        return self._HP

    @property
    def skills(self) -> list[str]:
        return self._skills

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @HP.setter
    def HP(self, value: int) -> None:
        if value < 0:
            raise ValueError("HP must be a non-negative integer.")
        self._HP = value

    @skills.setter
    def skills(self, value: list[str]) -> None:
        if not isinstance(value, list) or not all(isinstance(skill, str) for skill in value):
            raise ValueError("Skills must be a list of strings.")
        self._skills = value

    def addChildhoodBackstory(self, backstory) -> None:
        self.backstory.childhood = backstory
        for ability in ABILITY_NAMES:
            event = getattr(backstory, ability)
            self.addChildhoodEvent(event)

    def addChildhoodEvent(self, event) -> None:
        getattr(self, event.ability).add(event.bonus)

    def addAdolescenceBackstory(self, backstory) -> None:
        self.backstory.adolescence = backstory
        for event in backstory.events:
            self.addAdolescenceEvent(event)

    def addAdolescenceEvent(self, event) -> None:
        ability_chosen = event.answer
        ability_not_chosen = [ability for ability in event.answer_options if ability != ability_chosen][0]
        higher_roll = max(event.rolls)
        lower_roll = min(event.rolls)
        getattr(self, ability_chosen).add(higher_roll)
        getattr(self, ability_not_chosen).add(lower_roll)

    def addAdulthoodBackstory(self, backstory) -> None:
        self.backstory.adulthood = backstory
        for event in backstory.events:
            self.addAdulthoodEvent(event)

    def addAdulthoodEvent(self, event) -> None:
        if event.isAbilityTest():
            # Add Advantage or Disadvantage to influenced ability score
            ability_score = getattr(self, event.influenced_ability)
            if event.passed_test:
                ability_score.dice.add_adv()
            else:
                ability_score.dice.add_disadv()
        elif event.learned_skill != "":
            # Add skill
            self.skills.append(event.learned_skill)

    def getAbilityScores(self) -> dict['AbilityScore']:
        return {ability_name: getattr(self, ability_name) for ability_name in ABILITY_NAMES}

    def __str__(self) -> str:
        return f'''
{self.backstory}

-----------------------------------------------------------------
Final Results:
| {" | ".join([str(getattr(self, ability_name)) for ability_name in ABILITY_NAMES])} |

Skills: {self.skills}
-----------------------------------------------------------------
    '''