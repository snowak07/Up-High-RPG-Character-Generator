class AdolescenceBackstory:
    def __init__(self):
        self.events = []

    # Use __add__ special method for all "add" functions
    def addEvent(self, event: 'AdolescenceBackstoryEvent', index: int = None) -> None:
        if not isinstance(event, AdolescenceBackstoryEvent):
            raise ValueError("Event must be an instance of AdolescenceBackstoryEvent.")
        if index != None and (index < 0 or index >= len(self.events)):
            raise IndexError("Index out of range.")
        if index is None:
            self.events.append(event)
        else:
            self.events[index] = event

    def __str__(self) -> str:
        return "\n\n".join([str(event) for event in self.events])

class AdolescenceBackstoryEvent:
    def __init__(self, question, question_options, answer_options) -> None:
        self._question = question
        self._question_options = question_options
        self._answer_options = answer_options
        self._answer = ""
        self._rolls = []

    @property
    def question(self) -> str:
        return self._question

    @property
    def question_options(self) -> dict[str, str]:
        return self._question_options

    @property
    def answer_options(self) -> list[str]:
        return self._answer_options

    @property
    def answer(self) -> str:
        return self._answer

    @property
    def rolls(self) -> list[int]:
        return self._rolls

    @question.setter
    def question(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Question must be a non-empty string.")
        self._question = value

    @question_options.setter
    def question_options(self, value: dict[str, str]) -> None:
        if not isinstance(value, dict) or not all(isinstance(option, str) for option in value.values()):
            raise ValueError("Options must be a dict of strings.")
        self._question_options = value

    @answer_options.setter
    def answer_options(self, value: list[str]) -> None:
        if not isinstance(value, list) or not all(isinstance(option, str) for option in value):
            raise ValueError("Options must be a list of strings.")
        self._answer_options = value

    @answer.setter
    def answer(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Answer must be a non-empty string.")
        if (len(self._answer_options) > 0 and value not in self._answer_options):
            raise ValueError(f"Answer must be one of the provided answer_options {' '.join(self._answer_options)}.")
        self._answer = value

    @rolls.setter
    def rolls(self, value: list[int]) -> None:
        if not isinstance(value, list) or not all(isinstance(roll, int) for roll in value):
            raise ValueError("Rolls must be a list of integers.")
        self._rolls = value

    def addRoll(self, roll: int) -> None:
        if not isinstance(roll, int) or roll < 1 or roll > 6:
            raise ValueError("The roll must be a positive integer from 1 to 6, inclusive.")
        self._rolls.append(roll)

    def __str__(self) -> str:
        return f"{self.question}\n{"\n".join(["- " + option for ability, option in self.question_options.items()])}\nYou chose the {self.answer} option."