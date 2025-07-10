from stratfight.utils.data_loader import load_players, load_enemies

def main():
    players = load_players("data/players.json")
    enemies = load_enemies("data/enemies.json")

    for player in players:
        print(player.__shorthand__())
    for enemy in enemies:
        print(enemy.__shorthand__())



if __name__ == "__main__":
    main()