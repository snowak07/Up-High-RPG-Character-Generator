class AbilityScore:
    def __init__(self, name: str, value: int = 0, dice: 'AdvDisadvDice' = None) -> None:
        self.name = name
        self.value = value
        self.dice = dice if dice is not None else AdvDisadvDice()

    def __get__(self, instance, owner) -> 'AbilityScore':
        return self

    def __set__(self, instance, value: int) -> None:
        if value < 0 or value > 18:
            raise ValueError(f"{self.name} must be between 0 and 18.")
        self.value = value

    def add(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self.value += value

    def __add__(self, value: 'AbilityScore') -> 'AbilityScore':
        if not isinstance(value, AbilityScore):
            raise TypeError("Value must be an instance of AbilityScore.")
        return AbilityScore(self.name, self.value + value.value, self.dice)

    def __iadd__(self, value: 'AbilityScore') -> None:
        if not isinstance(value, AbilityScore):
            raise TypeError("Value must be an instance of AbilityScore.")
        self.value += value.value

    def __str__(self) -> str:
        return f"{self.name} ({self.value})"

class AdvDisadvDice:
    '''Class for keeping track of the advantage and disadvantage dice accrued based on Adulthood ability tests'''
    def __init__(self) -> None:
        self.value = 0

    def add_adv(self) -> None:
        self.value += 1

    def add_disadv(self) -> None:
        self.value = self.value - 1

    def get_dice_modifier(self) -> int:
        return self.value