"""
CP1404/CP5632 Practical
guitar.py
Class for representing a guitar and its properties.
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost
