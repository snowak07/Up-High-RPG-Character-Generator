from constants import ABILITY_NAMES
from backstory import Backstory

class CharacterSheet:
    def __init__(self, name: str):
        self._name = name
        self._HP = 0
        self._skills = []
        self._summary = ""
        [setattr(self, ability, AbilityScore(ability)) for ability in ABILITY_NAMES]
        self.backstory = Backstory()

    def summarizeBackstory(self):
        self.backstory.summarize()

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
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @HP.setter
    def HP(self, value: int):
        if value < 0:
            raise ValueError("HP must be a non-negative integer.")
        self._HP = value

    @skills.setter
    def skills(self, value: list[str]):
        if not isinstance(value, list) or not all(isinstance(skill, str) for skill in value):
            raise ValueError("Skills must be a list of strings.")
        self._skills = value

    def addChildhoodEvent(self, event):
        self.backstory.childhood.addEvent(event)
        getattr(self, event.ability).add(event.bonus) # Add to ability score

    def addAdolescenceEvent(self, event):
        self.backstory.adolescence.addEvent(event)
        ability_chosen = event.answer
        ability_not_chosen = [ability for ability in event.answer_options if ability != ability_chosen][0]
        higher_roll = max(event.rolls)
        lower_roll = min(event.rolls)
        getattr(self, ability_chosen).add(higher_roll)
        getattr(self, ability_not_chosen).add(lower_roll)

    def addAdulthoodEvent(self, event):
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

        self.backstory.adulthood.addEvent(event)

    def __str__(self):
        return f'''
{self.backstory}

------------------------------------------------------
Final Results:
| {" | ".join([str(getattr(self, ability_name)) for ability_name in ABILITY_NAMES])} |

Skills: {self.skills}
------------------------------------------------------
    '''

class AbilityScore:
    def __init__(self, name: str, value: int = 0, dice: 'AdvDisadvDice' = None):
        self.name = name
        self.value = value
        self.dice = dice if dice is not None else AdvDisadvDice()

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value: int):
        if value < 0 or value > 18:
            raise ValueError(f"{self.name} must be between 0 and 18.")
        self.value = value

    def add(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self.value += value

    def __add__(self, value: 'AbilityScore'):
        if not isinstance(value, AbilityScore):
            raise TypeError("Value must be an instance of AbilityScore.")
        return AbilityScore(self.name, self.value + value.value, self.dice)

    def __iadd__(self, value: 'AbilityScore'):
        if not isinstance(value, AbilityScore):
            raise TypeError("Value must be an instance of AbilityScore.")
        self.value += value.value

    def __str__(self):
        return f"{self.name} ({self.value})"

class AdvDisadvDice:
    '''Class for keeping track of the advantage and disadvantage dice accrued based on Adulthood ability tests'''
    def __init__(self):
        self.value = 0

    def add_adv(self):
        self.value += 1

    def add_disadv(self):
        self.value = self.value - 1

    def get_dice_modifier(self) -> int:
        return self.value