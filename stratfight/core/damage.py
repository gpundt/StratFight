from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy

def enemy_single_target_attack(attacker: Enemy, defender: Player):
    print(f"{attacker.name} attacks {defender.name}!")
    defender.take_damage(attacker.current_attack)

def enemy_multi_target_attack(attacker: Enemy, defenders: list[Player]):
    for defender in defenders:
        enemy_single_target_attack(attacker, defender)

def enemy_single_target_status_attack(attacker: Enemy, defender: Player, status_effect: StatusEffect):
    print(f"{attacker.name} attacks {defender.name} with a {status_effect.value} attack!")
    defender.take_damage(attacker.current_attack)
    defender.gain_status_effect(status_effect)

def enemy_multi_target_status_attack(attacker: Enemy, defenders: list[Player], status_effect: StatusEffect):
    for defender in defenders:
        enemy_multi_target_status_attack(attacker, defender, status_effect)



def player_single_target_attack(attacker: Player, defender: Enemy):
    print(f"{attacker.name} attacks {defender.name}!")
    defender.take_damage(attacker.current_attack)

def player_multi_target_attack(attacker: Player, defenders: list[Enemy]):
    for defender in defenders:
        player_single_target_attack(attacker, defender)

def player_single_target_status_attack(attacker: Player, defender: Enemy, status_effect: StatusEffect):
    print(f"{attacker.name} attacks {defender.name} with a {status_effect.value} attack!")
    defender.take_damage(attacker.current_attack)
    defender.gain_status_effect(status_effect)

def player_multi_target_status_attack(attacker: Player, defenders: list[Enemy], status_effect: StatusEffect):
    for defender in defenders:
        player_multi_target_status_attack(attacker, defender, status_effect)