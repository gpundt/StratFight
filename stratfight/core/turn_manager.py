from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy
import stratfight.core.damage as damage
from stratfight.skills.skill import Skill
import random

class Turn():
    def __init__(self, turn_number: int, players: list[Player], enemies: list[Enemy]):
        self.turn_number = turn_number
        self.players = players
        self.enemies = enemies
        self.all = players + enemies
        self.combat_order = sorted(self.all, key=lambda character: character.max_stamina, reverse=True)

    # repeats fuull turns until one team is dead
    def combat(self) -> int:
        while True:
            turn_result = self.full_turn()
            match turn_result:
                case "CONTINUE":
                    pass
                case "WIN":
                    return 0
                case "LOSE":
                    return 1
        
    # checks to see if any enemies are dead, giving XP to players if applicable
    def check_enemy_team(self) -> str:
        for enemy in self.enemies:
            if enemy.current_hp == 0:
                self.enemies.remove(enemy)
                for player in self.players:
                    player.gain_xp(enemy.xp_drop)
        self.all = self.players + self.enemies
        self.combat_order = sorted(self.all, key=lambda character: character.max_stamina, reverse=True)
        if len(self.enemies) == 0:
            return "DEAD"
        return "ALIVE"
    
    # checks to see if any players are dead and removes them from the list
    def check_player_team(self) -> str:
        for player in self.players:
            if player.current_hp == 0:
                self.players.remove(player)
        self.all = self.players + self.enemies
        self.combat_order = sorted(self.all, key=lambda character: character.max_stamina, reverse=True)
        if len(self.players) == 0:
            return "DEAD"
        return "ALIVE"

    # Prompts the user to make a choice, selecting a target if applicable
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
                result = player.use_skill()
                if result == 1:
                    print("[!] Skill is Too Expensive! [!]")
                    self.player_make_choice(player)
                match player.skill.multi_target:
                    case False:
                        if player.skill.heal:
                            target_player = damage.player_select_player(self.players)
                            damage.player_single_target_heal_skill(player, target_player)
                        else:
                            target_enemy = damage.player_select_enemy(self.enemies)
                            damage.player_single_target_attack_skill(player, target_enemy)
                    case True:
                        if player.skill.heal:
                            damage.player_multi_target_heal_skill(player, self.players)
                        else:
                            damage.player_multi_target_attack_skill(player, self.enemies)

            case "4":
                print(f"{player.name} passes...")


    # An enemy makes a random choice on a random target
    def enemy_make_choice(self, enemy: Enemy):
        choice = random.randint(0, 100)
        if choice <= 35:
            target_player = damage.enemy_select_player(self.players)
            damage.enemy_single_target_attack(enemy, target_player)
        elif choice >=36 or choice <= 50:
            enemy.gain_defense(enemy.current_defense)
            print(f"{enemy.name} raises their defence to {enemy.current_defense}!")
        elif choice >= 51 or choice <= 90:
            result = enemy.use_skill()
            if result == 1:
                self.enemy_make_choice(enemy)
            else:
                match enemy.skill.multi_target:
                    case False:
                        if enemy.skill.heal:
                            target_enemy = damage.enemy_select_enemy(self.enemies)
                            damage.enemy_single_target_heal_skill(enemy, target_enemy)
                        else:
                            target_enemy = damage.enemy_select_player(self.players)
                            damage.enemy_single_target_attack_skill(enemy, target_enemy)
                    case True:
                        if enemy.skill.heal:
                            damage.enemy_multi_target_heal_skill(enemy, self.enemies)
                        else:
                            damage.enemy_multi_target_attack_skill(enemy, self.players)
        else:
            print(f"{enemy.name} passes...")

    # prints the list of attacking characters in order
    def print_combat_order(self):
        print(f"="*5 + " Combat Order " + "="*5)
        for entity in self.combat_order:
            print(f"{entity.name}:\t{entity.current_hp}/{entity.max_hp}\t{entity.max_stamina} MAX STA")

    # Iterates through combat order, then prompts each character to make a choice
    def full_turn(self)-> str:
        print(f"Turn: {self.turn_number}")
        self.print_combat_order()
        for entity in self.combat_order:
            player_status = self.check_player_team()
            enemy_status = self.check_enemy_team()
            if enemy_status == "ALIVE" and player_status == "ALIVE":
                print(f"{entity.name}'s Turn!")
                if type(entity) is Enemy:
                    self.enemy_make_choice(entity)
                elif type(entity) is Player:
                    self.player_make_choice(entity)
            elif enemy_status == "DEAD":
                print("You win! The enemies have been slain!")
                return "WIN"
            elif player_status == "DEAD":
                print(f"Game Over!\nYour team has been slain!")
                return "LOSE"
            self.turn_number += 1
        return "CONTINUE"


## Testing combat ##
def main():
    test_player_skill = Skill("Test_skill1", "a skill to test with", 30, 1, 5, 5, 5, DamageType.NORMAL, StatusEffect.NONE, True, False, False, "none", 0)
    test_enemy_skill = Skill("Test_enemy_skill", "Another skill!", 30, 2, 10, 10, 10, DamageType.DARK, StatusEffect.POISON, True, False, True, "ATK", .5)
    test_heal_skill = Skill("Heal", "Heals someone", 20, 5, 20, 0, 0, DamageType.LIGHT, StatusEffect.NONE, True, True ,False, "NONE", 0)
    test_player1 = Player("Test_player2", 50, 7, 10, 90, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 5, test_player_skill, 100, debug_logs=True)
    test_player2 = Player("Test_player1", 50, 7, 10, 0, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, test_heal_skill, 100, debug_logs=True)
    test_enemy1 = Enemy("Test_enemy1", 40, 5, 5, 5, 5, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, test_heal_skill, 10, debug_logs=True)
    test_enemy2 = Enemy("Test_enemy2", 40, 5, 5, 5, 90, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, test_enemy_skill, 10, debug_logs=True)
    turn = Turn(1, [test_player1, test_player2], [test_enemy1, test_enemy2])
    turn.combat()

if __name__ == "__main__":
    main()