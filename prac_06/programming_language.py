"""
CP1404/CP5632 Practical
programming_language.py
Class for representing a programming language's key attributes.
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"
