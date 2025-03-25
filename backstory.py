from childhood_backstory import ChildhoodBackstory
from adolescence_backstory import AdolescenceBackstory
from adulthood_backstory import AdulthoodBackstory

class Backstory:
    def __init__(self):
        self.childhood = ChildhoodBackstory()
        self.adolescence = AdolescenceBackstory()
        self.adulthood = AdulthoodBackstory()

    # TODO Return complete backstory string printout
    def __str__(self):
        return f"Childhood Backstory:\n{self.childhood}\n\nAdolescence Backstory:\n{self.adolescence}\n\nAdulthood Backstory:\n{self.adulthood}"