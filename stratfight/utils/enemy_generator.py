import json
from pathlib import Path
from random import randint, choice, uniform
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass


# Generates a JSON list of ranomized enemies with increasing difficulty
enemies = []
for i in range(1, 31):
    name = f"{choice(['Goblin', 'Orc', 'Bandit', 'Wraith', 'Knight', 'Demon', 'Cultist', 'Slime', 'Wolf', 'Beast'])}"
    base_attack = randint(5 + i, 10 + i)
    base_defense = randint(3 + i, 8 + i)
    max_hp = randint(30 + i * 2, 60 + i * 3)
    max_mana = randint(0, 40 if i > 10 else 10)
    max_stamina = randint(20 + i, 60 + i)
    damage_type = choice(list(DamageType))
    char_class = choice(list(CharacterClass))
    level = i
    xp_drop = randint(10 + i * 2, 20 + i * 3)

    enemies.append({
        "name": name,
        "max_hp": max_hp,
        "base_attack": base_attack,
        "base_defense": base_defense,
        "max_mana": max_mana,
        "max_stamina": max_stamina,
        "damage_type": damage_type.name,
        "character_class": char_class.name,
        "status_effects": [],
        "level": level,
        "xp_drop": xp_drop
    })
output = json.dumps({"enemies": enemies}, indent=2)  # preview small part
print(output)
