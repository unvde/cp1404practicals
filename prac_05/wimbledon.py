FILENAME = "wimbledon.csv"

def main():
    champions = []
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            champions.append((champion, country))

    champion_to_count = {}
    for champion, _ in champions:
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

main()
