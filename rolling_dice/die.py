from random import randint

class Die:
    """A class representing a single Die"""

    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a randon value between 1 and number of sides"""
        return randint(1, self.num_sides)

        