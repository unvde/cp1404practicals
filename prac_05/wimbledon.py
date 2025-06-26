"""
CP1404/CP5632 Practical
wimbledon.py
Read Wimbledon results and display champion counts and countries.
"""

FILENAME = "wimbledon.csv"

def main():
    """Read Wimbledon data and display champion stats and countries."""
    champions = read_data(FILENAME)
    champion_to_count = count_champions(champions)
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    countries = get_countries(champions)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def read_data(filename):
    """Read data from CSV file and return a list of (champion, country)."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            champions.append((champion, country))
    return champions

def count_champions(champions):
    """Count the number of wins for each champion."""
    champion_to_count = {}
    for champion, _ in champions:
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count

def get_countries(champions):
    """Extract a sorted list of unique countries from data."""
    return sorted({country for _, country in champions})

if __name__ == '__main__':
    main()
