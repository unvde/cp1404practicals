"""
CP1404/CP5632 Practical
myguitars.py
Read guitars from file, display, sort, add, and store Guitar objects.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def load_guitars():
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(guitars, filename):
    """Save list of Guitar objects to a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def main():
    """Start the guitar program."""
    guitars = load_guitars()

    print("These are the guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")

    # Sort and display
    guitars.sort()
    print("\nThese are the guitars sorted by year:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")

    # Add new guitars
    print("\nAdd new guitars (leave name empty to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Skipping this entry.")
            continue
        guitars.append(Guitar(name, year, cost))

    # Save all guitars to file
    save_guitars(guitars, FILENAME)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}")


if __name__ == '__main__':
    main()
