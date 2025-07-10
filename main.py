from stratfight.utils.data_loader import load_players, load_enemies

def main():
    players = load_players("data/players.json")
    enemies = load_enemies("data/enemies.json")

    for p in players:
        print(p)
    for e in enemies:
        print(e)


if __name__ == "__main__":
    main()