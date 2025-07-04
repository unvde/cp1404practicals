"""
CP1404/CP5632 Practical
guitar_test.py
Tests for Guitar class methods: get_age and is_vintage.
"""

from guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2013, 1000.00)

print(f"{guitar_1.name} get_age() - Expected 102. Got {guitar_1.get_age()}")
print(f"{guitar_2.name} get_age() - Expected 11. Got {guitar_2.get_age()}")

print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")
