from constants import ABILITY_NAMES

class ChildhoodBackstory:
    def __init__(self):
        [setattr(self, ability, None) for ability in ABILITY_NAMES]

    def addEvent(self, event: 'ChildhoodBackstoryEvent'):
        if not isinstance(event, ChildhoodBackstoryEvent):
            raise ValueError("Event must be an instance of ChildhoodBackstoryEvent.")
        setattr(self, event.ability, event)

    def __str__(self):
        return "\n".join([str(getattr(self, ability)) for ability in ABILITY_NAMES if getattr(self, ability) is not None])

class ChildhoodBackstoryEvent:
    def __init__(self, ability: str = "", bonus: int = 0, lore: str = ""):
        self._ability = ability
        self._bonus = bonus
        self._lore = lore

    '''Ability name'''
    @property
    def ability(self) -> str:
        return self._ability

    '''Ability bonus'''
    @property
    def bonus(self) -> int:
        return self._bonus

    '''Lore snippet'''
    @property
    def lore(self) -> str:
        return self._lore

    @ability.setter
    def ability(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ability must be a non-empty string.")
        if value not in ABILITY_NAMES:
            raise ValueError(f"Ability must be one of the provided options {', '.join(ABILITY_NAMES)}.")
        self._ability = value

    @bonus.setter
    def bonus(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Ability bonus must be an integer greater than 0.")
        self._bonus = value

    @lore.setter
    def lore(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Lore must be a non-empty string.")
        self._lore = value

    def __str__(self):
        return f"{self.lore} (+{self.bonus} to {self.ability})"