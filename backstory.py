from adolescence_backstory import AdolescenceBackstory
from adulthood_backstory import AdulthoodBackstory
from childhood_backstory import ChildhoodBackstory
from gpt_provider import getGPTSummary

class Backstory:
    def __init__(self) -> None:
        self.childhood = ChildhoodBackstory()
        self.adolescence = AdolescenceBackstory()
        self.adulthood = AdulthoodBackstory()
        self._summary = ""

    @property
    def summary(self) -> str:
        return self._summary

    @summary.setter
    def summary(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Summary must be a non-empty string.")
        self._summary = value

    def __str__(self) -> str:
        return f"Childhood Backstory:\n{self.childhood}\n\nAdolescence Backstory:\n{self.adolescence}\n\nAdulthood Backstory:\n{self.adulthood}\n\nSummary:\n{self.summary}"

    async def summarize(self) -> None:
        self.summary = await getGPTSummary(str(self))