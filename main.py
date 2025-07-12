from stratfight.utils.data_loader import load_players, load_enemies
from stratfight.core.battle import Battle

def main():
    players = load_players("data/players.json")
    enemies = load_enemies("data/enemies.json")

    test_battle = Battle(1, enemies, players, True)


if __name__ == "__main__":
    main()