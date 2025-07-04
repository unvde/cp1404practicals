"""
CP1404/CP5632 Practical
languages.py
Client code to test the ProgrammingLanguage class.
"""

from programming_language import ProgrammingLanguage


def main():
    """Test creation and string output of ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]

    print("All languages:")
    for language in languages:
        print(language)


main()
