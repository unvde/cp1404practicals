"""
CP1404/CP5632 Practical
myguitars.py
Read guitars from file and store as Guitar objects.
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

def main():
    """Start the guitar program."""
    guitars = load_guitars()

    print("These are the guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


if __name__ == '__main__':
    main()
