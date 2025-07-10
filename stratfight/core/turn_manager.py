from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy

class Turn():
    def __init__(self, turn_number: int, players: list[Player], enemies: list[Enemy]):
        self.turn_number = turn_number
        self.players = players
        self.enemies = enemies
        self.all = players + enemies
        self.combat_order = sorted(self.all, key=lambda character: character.max_stamina, reverse=True)

    def player_make_choice(self, player: Player):
        pass

    def enemy_make_choice(self, enemy: Enemy):
        pass

    def print_combat_order(self):
        print(f"="*5 + " Combat Order " + "="*5)
        for entity in self.combat_order:
            print(entity.__shorthand__())

    def full_turn(self):
        print(f"Turn: {self.turn_number}")
        self.print_combat_order()

        self.turn_number += 1


def main():
    test_player1 = Player("Test_player2", 50, 7, 10, 90, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, 100, debug_logs=True)
    test_player2 = Player("Test_player1", 50, 7, 10, 0, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, 100, debug_logs=True)
    test_enemy1 = Enemy("Test_enemy1", 40, 5, 5, 5, 5, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, 10)
    test_enemy2 = Enemy("Test_enemy2", 40, 5, 5, 5, 90, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, 10)
    turn = Turn(1, [test_player1, test_player2], [test_enemy1, test_enemy2])
    turn.print_combat_order()

if __name__ == "__main__":
    main()