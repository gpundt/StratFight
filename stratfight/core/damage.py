from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy
from stratfight.skills.skill import Skill
import random


# ======= Enemy Functions ======= #
# A random player is selected to be the target of an enemy
def enemy_select_player(targets: list[Player])-> Player:
    return random.choice(targets)

# the lowest health enemy is selected to be the target of a heal
def enemy_select_enemy(targets: list[Enemy]) -> Enemy:
    lowest_hp_enemy = min(targets, key=lambda enemy: enemy.current_hp)
    return lowest_hp_enemy

# An enemy atacks a single target
def enemy_single_target_attack(attacker: Enemy, defender: Player):
    print(f"{attacker.name} attacks {defender.name}!")
    defender.take_damage(attacker.current_attack, attacker.damage_type)

# An enemy attacks all targets
def enemy_multi_target_attack(attacker: Enemy, defenders: list[Player]):
    for defender in defenders:
        enemy_single_target_attack(attacker, defender)

# an enemy attacks a single target and applies a status effect
def enemy_single_target_status_attack(attacker: Enemy, defender: Player, status_effect: StatusEffect):
    print(f"{attacker.name} attacks {defender.name} with a {status_effect.value} attack!")
    defender.take_damage(attacker.current_attack, attacker.damage_type)
    defender.gain_status_effect(status_effect)

# an enemy attacks all targets and applies each with a status effect
def enemy_multi_target_status_attack(attacker: Enemy, defenders: list[Player], status_effect: StatusEffect):
    for defender in defenders:
        enemy_multi_target_status_attack(attacker, defender, status_effect)

# An enemy uses their attack skill on a single target
def enemy_single_target_attack_skill(attacker: Enemy, defender: Player):
    print(f"{attacker.name} uses {attacker.skill.name} on {defender.name}!")
    defender.take_damage(attacker.skill.damage, attacker.skill.damage_type)
    if (attacker.skill.status_effect.value != "None"):
        defender.gain_status_effect(attacker.skill.status_effect)

# an enemy uses their heal skill on a single target
def enemy_single_target_heal_skill(user: Enemy, receiver: Enemy):
    print(f"{user.name} uses {user.skill.name} on {receiver.name}")
    receiver.gain_hp(user.skill.heal_amount)

# an enemy uses their attack skill on all targets
def enemy_multi_target_attack_skill(attacker: Enemy, defenders: list[Player]):
    for defender in defenders:
        enemy_single_target_attack_skill(attacker, defender)

# an enemy uses their heal skill on all targets
def enemy_multi_target_heal_skill(user: Enemy, receivers: list[Enemy]):
    for receiver in receivers:
        enemy_multi_target_heal_skill(user, receiver)
# ======= ============ ======= #


# ======= Player Functions ======= #
# The user is prompted to select an enemy from a list of enemies
def player_select_enemy(targets: list[Enemy]) -> Enemy:
    print(f"Select a target enemy:")
    for enemy in targets:
        print(f"{targets.index(enemy)+1})\t{enemy.name}\t({enemy.current_hp}/{enemy.max_hp})")
    choice = input(">>>\t")
    try:
        return targets[int(choice)-1]
    except:
        print("[!] Invalid Choice [!]\n")
        return player_select_enemy(targets)
    
# THe user is prompted to select a player from a list of players
def player_select_player(targets: list[Player]) -> Player:
    print(f"Select a target player:")
    for player in targets:
        print(f"{targets.index(player)+1})\t{player.name}\t({player.current_hp}/{player.max_hp})")
    choice = input(">>>\t")
    try:
        return targets[int(choice)-1]
    except:
        print("[!] Invalid Choice [!]")
        return player_select_player(targets)

# a player attacks a single target
def player_single_target_attack(attacker: Player, defender: Enemy):
    print(f"{attacker.name} attacks {defender.name}!")
    defender.take_damage(attacker.current_attack, attacker.damage_type)

# a player attacks all targets
def player_multi_target_attack(attacker: Player, defenders: list[Enemy]):
    for defender in defenders:
        player_single_target_attack(attacker, defender)

# a player attacks a single target and applies a status effect
def player_single_target_status_attack(attacker: Player, defender: Enemy, status_effect: StatusEffect):
    print(f"{attacker.name} attacks {defender.name} with a {status_effect.value} attack!")
    defender.take_damage(attacker.current_attack, attacker.damage_type)
    defender.gain_status_effect(status_effect)

# a player attacks all targets and applies a status effect to each
def player_multi_target_status_attack(attacker: Player, defenders: list[Enemy], status_effect: StatusEffect):
    for defender in defenders:
        player_multi_target_status_attack(attacker, defender, status_effect)

# a player uses their attack skill on a single target
def player_single_target_attack_skill(attacker: Player, defender: Enemy):
    print(f"{attacker.name} uses {attacker.skill.name} on {defender.name}!")
    defender.take_damage(attacker.skill.damage, attacker.skill.damage_type)
    if (attacker.skill.status_effect.value != "None"):
        defender.gain_status_effect(attacker.skill.status_effect)

# a player uses their heal skill on a single target
def player_single_target_heal_skill(user: Player, receiver: Player):
    print(f"{user.name} uses {user.skill.name} on {receiver.name}")
    receiver.gain_hp(user.skill.heal_amount)

# a player uses their attack skill on all targets
def player_multi_target_attack_skill(attacker: Player, defenders: list[Enemy]):
    for defender in defenders:
        player_single_target_attack_skill(attacker, defender)

# a player uses their heal skill on all targets
def player_multi_target_heal_skill(user: Player, receivers: list[Player]):
    for receiver in receivers:
        player_single_target_heal_skill(user, receiver)
# ======= ============ ======= #