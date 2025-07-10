from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
import textwrap


class Enemy(BaseCharacter):
    def __init__(self, name, max_hp, base_attack, base_defense, max_mana, max_stamina, damage_type, character_class, status_effects, level, xp_drop, debug_logs = False):
        super().__init__(name, max_hp, base_attack, base_defense, max_mana, max_stamina, damage_type, character_class, status_effects, level, debug_logs)
        self.xp_drop = xp_drop

    def __str__(self):
        return textwrap.dedent(f"""
            Name:\t\t{self.name}
            Level:\t\t{self.level}
            XP Drop:\t{self.xp_drop}
            HP:\t\t{self.current_hp}/{self.max_hp}
            Mana:\t\t{self.current_mana}/{self.max_mana}
            Stamina:\t{self.current_stamina}/{self.max_stamina}
            A/D:\t\t{self.current_attack}/{self.current_defense}
            Class:\t\t{self.character_class.value}
            Damage:\t\t{self.damage_type.value}
            """).strip()
    
    def __repr__(self):
        return (f"<{self.__class__.__name__}("
                f"name='{self.name}', "
                f"Level={self.level}, "
                f"XP_Drop={self.xp_drop}. "
                f"HP={self.current_hp}/{self.max_hp}, "
                f"Mana={self.current_mana}/{self.max_mana}, "
                f"Stamina={self.current_stamina}/{self.max_stamina}, "
                f"Class={self.character_class.name}, "
                f"Damage={self.damage_type.name})>")
    
    def dropped_xp(self):
        return self.xp_drop