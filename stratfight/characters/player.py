from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
import textwrap

class Player(BaseCharacter):
    def __init__(self, name, max_hp, base_attack, base_defense, max_mana, max_stamina, damage_type, character_class, status_effects, level, max_xp, debug_logs = False):
        super().__init__(name, max_hp, base_attack, base_defense, max_mana, max_stamina, damage_type, character_class, status_effects, level, debug_logs)
        self.current_xp = 0
        self.max_xp = max_xp

    def __str__(self):
        return textwrap.dedent(f"""
            Name:\t\t{self.name}
            Level:\t\t{self.level}
            XP:\t\t{self.current_xp}/{self.max_xp}
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
                f"XP={self.current_xp}/{self.max_xp}, "
                f"HP={self.current_hp}/{self.max_hp}, "
                f"Mana={self.current_mana}/{self.max_mana}, "
                f"Stamina={self.current_stamina}/{self.max_stamina}, "
                f"Class={self.character_class.name}, "
                f"Damage={self.damage_type.name})>")

    def increase_max_xp(self, increase_amount: int):
        self.max_xp += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s max XP has increased to {self.max_xp}")

    def level_increase_stats(self):
        self.increase_max_hp(5)
        self.increase_max_mana(5)
        self.increase_max_stamina(5)
        self.increase_base_attack(2)
        self.increase_base_defense(2)

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to {self.level}!")
        self.increase_max_xp(20)
        self.level_increase_stats()
        self.full_restore_all()
        print(f"[Stats Increased]\n{self}")

    def gain_xp(self, gain_amount: int):
        print(f"{self.name} has gained {gain_amount} XP!")
        self.current_xp += gain_amount
        while (self.current_xp >= self.max_xp):
            self.current_xp -= self.max_xp
            self.level_up()


def main():
    test_player = Player("Test_player", 50, 7, 10, 50, 20, DamageType.DARK, CharacterClass.WARLOCK, [], 43, 100, debug_logs=True)
    print(test_player)
    test_player.gain_xp(500)

if __name__ == "__main__":
    main()
