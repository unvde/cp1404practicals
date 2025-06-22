FILENAME = "wimbledon.csv"

def main():
    champions = []
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            champions.append((champion, country))

    print(champions[:5])  # For quick check

main()
