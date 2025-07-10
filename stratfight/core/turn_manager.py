from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy
import stratfight.core.damage as damage
import random

class Turn():
    def __init__(self, turn_number: int, players: list[Player], enemies: list[Enemy]):
        self.turn_number = turn_number
        self.players = players
        self.enemies = enemies
        self.all = players + enemies
        self.combat_order = sorted(self.all, key=lambda character: character.max_stamina, reverse=True)

    def player_make_choice(self, player: Player):
        choice = input(f"{player.name}... Make a choice\n"\
            f"1)\tAttack\t({player.current_attack} ATK)\n"\
            f"2)\tBlock\t({player.current_defense * 1.5} DEF)\n"\
            f"3)\tSkill\n"\
            f"4)\tPass\n>>>\t")
        match choice:
            case "1":
                target_enemy = damage.player_select_enemy(self.enemies)
                damage.player_single_target_attack(player, target_enemy)
            case "2":
                player.gain_defense(player.current_defense*.5)
            case "3":
                pass
            case "4":
                print(f"{player.name} passes...")

    def enemy_make_choice(self, enemy: Enemy):
        choice = random.randint(0, 50)
        if choice <= 25:
            target_player = damage.enemy_select_player(self.players)
            damage.enemy_single_target_attack(enemy, target_player)
        elif choice >= 26 or choice <= 45:
            enemy.gain_defense(enemy.current_defense)
            print(f"{enemy.name} raises their defence to {enemy.current_defense}!")
        else:
            print(f"{enemy.name} passes...")

    def print_combat_order(self):
        print(f"="*5 + " Combat Order " + "="*5)
        for entity in self.combat_order:
            print(entity.__shorthand__())

    def full_turn(self):
        print(f"Turn: {self.turn_number}")
        self.print_combat_order()
        for entity in self.combat_order:
            print(f"{entity.name}'s Turn!")
            if type(entity) is Enemy:
                self.enemy_make_choice(entity)
            elif type(entity) is Player:
                self.player_make_choice(entity)
    
        self.turn_number += 1


def main():
    test_player1 = Player("Test_player2", 50, 7, 10, 90, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, 100, debug_logs=True)
    test_player2 = Player("Test_player1", 50, 7, 10, 0, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, 100, debug_logs=True)
    test_enemy1 = Enemy("Test_enemy1", 40, 5, 5, 5, 5, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, 10, debug_logs=True)
    test_enemy2 = Enemy("Test_enemy2", 40, 5, 5, 5, 90, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, 10, debug_logs=True)
    turn = Turn(1, [test_player1, test_player2], [test_enemy1, test_enemy2])
    turn.full_turn()

if __name__ == "__main__":
    main()