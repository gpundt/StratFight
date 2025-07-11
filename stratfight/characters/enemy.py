from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.skills.skill import Skill
import textwrap


class Enemy(BaseCharacter):
    def __init__(self, name: str, max_hp: int, base_attack: int, base_defense: int, max_mana: int, max_stamina: int, damage_type: DamageType, character_class: CharacterClass, status_effects: list[StatusEffect], level: int, skill: Skill, xp_drop: int, debug_logs = False):
        super().__init__(name, max_hp, base_attack, base_defense, max_mana, max_stamina, damage_type, character_class, status_effects, level, skill, debug_logs)
        self.xp_drop = xp_drop

    def __str__(self) -> str:
        return textwrap.dedent(f"""
            Name:\t\t{self.name}
            Level:\t\t{self.level}
            Skill:\t\t{self.skill.name}
            XP Drop:\t{self.xp_drop}
            HP:\t\t{self.current_hp}/{self.max_hp}
            Mana:\t\t{self.current_mana}/{self.max_mana}
            Stamina:\t{self.current_stamina}/{self.max_stamina}
            A/D:\t\t{self.current_attack}/{self.current_defense}
            Class:\t\t{self.character_class.value}
            Damage:\t\t{self.damage_type.value}
            """).strip()
    
    def __repr__(self) -> int:
        return (f"<{self.__class__.__name__}("
                f"name='{self.name}', "
                f"Level={self.level}, "
                f"skill={self.skill.name}, "
                f"XP_Drop={self.xp_drop}. "
                f"HP={self.current_hp}/{self.max_hp}, "
                f"Mana={self.current_mana}/{self.max_mana}, "
                f"Stamina={self.current_stamina}/{self.max_stamina}, "
                f"Class={self.character_class.name}, "
                f"Damage={self.damage_type.name})>")
    
    def dropped_xp(self) -> int:
        return self.xp_drop
    
def main():
    test_enemy1 = Enemy("Test_enemy1", 40, 5, 5, 5, 5, DamageType.DARK, CharacterClass.BARBARIAN, [], 5, 10)

if __name__ == "__main__":
    main()