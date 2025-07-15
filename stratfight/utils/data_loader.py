import json
from pathlib import Path
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.skills.skill import Skill

# Loads a json file into a varaible
def load_json(path: str) -> list[dict]:
    with open(Path(path), 'r') as f:
        return json.load(f)

# loads json file and outputs a list of Player structs
def load_players(json_path: str) -> list[Player]:
    players_data = load_json(json_path)
    players = []
    for pdata in players_data:
        player = Player(
            name=pdata["name"],
            max_hp=pdata["max_hp"],
            base_attack=pdata["base_attack"],
            base_defense=pdata["base_defense"],
            max_mana=pdata["max_mana"],
            max_stamina=pdata["max_stamina"],
            damage_type=DamageType[pdata["damage_type"]],
            character_class=CharacterClass[pdata["character_class"]],
            status_effects=[],  # Fill if needed
            level=pdata["level"],
            max_xp=pdata["max_xp"]
        )
        players.append(player)
    return players

# loads json file and outputs a list of Enemy structs
def load_enemies(json_path: str) -> list[Enemy]:
    enemies_data = load_json(json_path)
    enemies = []
    for edata in enemies_data:
        enemy = Enemy(
            name=edata["name"],
            max_hp=edata["max_hp"],
            base_attack=edata["base_attack"],
            base_defense=edata["base_defense"],
            max_mana=edata["max_mana"],
            max_stamina=edata["max_stamina"],
            damage_type=DamageType[edata["damage_type"]],
            character_class=CharacterClass[edata["character_class"]],
            status_effects=[],
            level=edata["level"],
            xp_drop=edata["xp_drop"]
        )
        enemies.append(enemy)
    return enemies

# loads json file and outputs a list of Skill structs
def load_skills(json_path: str) -> list[Skill]:
    skills_data = load_json(json_path)
    pass