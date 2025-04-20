from constants import ABILITY_NAMES, PROFESSION_NAMES
from ability_score import AbilityScore

class AdulthoodBackstory:
    def __init__(self) -> None:
        self.events = []
        self.ability_bonuses = {}

    def addEvent(self, event: 'AdulthoodBackstoryEvent', index: int = None) -> None:
        if not isinstance(event, AdulthoodBackstoryEvent):
            raise ValueError("Event must be an instance of AdulthoodBackstoryEvent.")
        elif index is None:
            self.events.append(event)
        elif index < 0 or index >= len(self.events):
            raise IndexError("Index out of range.")
        else:
            self.events[index] = event

    def addAbilityBonus(self, ability_name, ability_score: 'AbilityScore') -> None:
        if not isinstance(ability_score, AbilityScore):
            raise ValueError("Ability score must be an instance of AbilityScore.")
        elif ability_name not in ABILITY_NAMES:
            raise ValueError(f"Ability name must be one of the following: {ABILITY_NAMES}")
        else:
            self.ability_bonuses[ability_name] = ability_score

    def __str__(self) -> str:
        return "\n\n".join([(f"For period {index+1} of {len(self.events)} your background was {event.profession}. You faced the following scenario:\n{event}") for index, event in enumerate(self.events)]) # FIXME key, value work?

class AdulthoodBackstoryEvent:
    def __init__(self, profession = "", scenario = "", tested_ability = "", influenced_ability = "", learned_skill = "") -> None:
        self._profession = profession
        self._scenario = scenario
        self._tested_ability = tested_ability
        self._influenced_ability = influenced_ability
        self._passed_test = None
        self._learned_skill = learned_skill

    @property
    def profession(self) -> str:
        return self._profession

    @property
    def scenario(self) -> str:
        return self._scenario

    @property
    def tested_ability(self) -> str:
        return self._tested_ability

    @property
    def influenced_ability(self) -> str:
        return self._influenced_ability

    @property
    def passed_test(self) -> bool:
        return self._passed_test

    @property
    def learned_skill(self) -> str:
        return self._learned_skill

    @profession.setter
    def profession(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Profession must be a non-empty string.")
        if value not in PROFESSION_NAMES:
            raise ValueError(f"Profession must be one of the provided options {', '.join(PROFESSION_NAMES)}.")
        self._profession = value

    @scenario.setter
    def scenario(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Scenario must be a non-empty string.")
        self._scenario = value

    @tested_ability.setter
    def tested_ability(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tested ability must be a non-empty string.")
        if value not in ABILITY_NAMES:
            raise ValueError(f"Tested ability must be one of the provided options {', '.join(ABILITY_NAMES)}.")
        self._tested_ability = value

    @influenced_ability.setter
    def influenced_ability(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Influenced ability must be a non-empty string.")
        if value not in ABILITY_NAMES:
            raise ValueError(f"Influenced ability must be one of the provided options {', '.join(ABILITY_NAMES)}.")
        self._influenced_ability = value

    @passed_test.setter
    def passed_test(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Passed test must be a bool")
        self._passed_test = value

    @learned_skill.setter
    def learned_skill(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Learned skill must be a non-empty string.")
        self._learned_skill = value

    def isAbilityTest(self) -> bool:
        return self.tested_ability != ""

    def isRandomSkill(self) -> bool:
        return self.learned_skill and self.learned_skill == "Random"

    def isLearnedSkill(self) -> bool:
        return self.learned_skill and self.learned_skill != "Random"

    def __str__(self) -> str:
        string = self.scenario + "\n"
        if self.isAbilityTest():
            string += "You succeeded on the test." if self.passed_test else "You failed the test."
        else:
            string += f"You learned the skill: {self.learned_skill}."
        
        return string