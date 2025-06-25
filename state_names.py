"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Dictionary of state abbreviations to full names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states and names, neatly aligned
for code, name in CODE_TO_NAME.items():
    print(f"{code:>3} is {name}")

# Input loop for user to enter state abbreviation
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        # Attempt to access dictionary value (EAFP)
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
