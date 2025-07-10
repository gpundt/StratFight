from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
import textwrap
from stratfight.utils.logger import log

class BaseCharacter:
    def __init__(self, name: str, max_hp: int, base_attack: int, base_defense: int, max_mana: int, max_stamina: int, damage_type: DamageType, character_class: CharacterClass, debug_logs: bool = False):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.base_attack = base_attack
        self.current_attack = base_attack
        self.base_defense = base_defense
        self.current_defense = base_defense
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.damage_type = damage_type
        self.character_class = character_class
        self.is_alive = (self.current_hp > 0)
        self.debug_logs = debug_logs

    def __str__(self):
        return textwrap.dedent(f"""
            Name:\t\t{self.name}
            HP:\t\t{self.current_hp}/{self.max_hp}
            Mana:\t\t{self.current_mana}/{self.max_mana}
            Stamina:\t{self.current_stamina}/{self.max_stamina}
            A/D:\t\t{self.current_attack}/{self.current_defense}
            Class:\t\t{self.character_class.value}
            Damage:\t\t{self.damage_type.value}
            """).strip()
    
    def __repr__(self):
        return (f"<{self.__class__.__name__}()"
                f"name='{self.name}', "
                f"HP={self.current_hp}/{self.max_hp}, "
                f"Mana={self.current_mana}/{self.max_mana}, "
                f"Stamina={self.current_stamina}/{self.max_stamina}, "
                f"Class={self.character_class.name}, "
                f"Damage={self.damage_type.name})>")

    def take_damage(self, damage_amount: int, damage_type: DamageType):
        ## Resistances and stuff ##
        self.current_hp -= max(0, damage_amount - self.current_defense)
        self.current_hp = max(0, self.current_hp)
        if self.debug_logs:
            log(f"{self.name} took {damage_amount} damage! HP is now {self.current_hp}/{self.max_hp}")

    def gain_hp(self, heal_amount: int):
        self.current_hp += min(self.max_hp, self.current_hp + heal_amount)
        if self.debug_logs:
            log(f"{self.name} gained {heal_amount} health! HP is now {self.current_hp}/{self.max_hp}")

    def lose_attack(self, loss_amount: int):
        self.current_attack = max(1, self.current_attack - loss_amount)
        if self.debug_logs:
            log(f"{self.name}'s attack has dropped {loss_amount} points! Attack is now {self.current_attack}")

    def gain_attack(self, gain_amount: int):
        self.current_attack += gain_amount
        if self.debug_logs:
            log(f"{self.name}'s attack has raised {gain_amount} points! Attack is now {self.current_attack}")

    def lose_defense(self, loss_amount: int):
        self.current_defense = max(0, self.current_defense - loss_amount)
        if self.debug_logs:
            log(f"{self.name}'s defense has dropped {loss_amount} points! Defense is now {self.current_defense}")

    def gain_defense(self, gain_amount: int):
        self.current_defense += gain_amount
        if self.debug_logs:
            log(f"{self.name}'s defense has raised {gain_amount} points! Defense is now {self.current_defense}")

    def spend_mana(self, cost: int):
        self.current_mana = max(0, self.current_mana - cost)
        if self.debug_logs:
            log(f"{self.name} spent {cost} mana! Mana is now {self.current_mana}/{self.max_mana}")

    def gain_mana(self, gain_amount: int):
        self.current_mana = min(self.max_mana, self.current_mana + gain_amount)
        if self.debug_logs:
            log(f"{self.name} gained {gain_amount} mana! Mana is now {self.current_mana}/{self.max_mana}")

    def spend_stamina(self, cost: int):
        self.current_stamina = max(0, self.current_stamina - cost)
        if self.debug_logs:
            log(f"{self.name} spent {cost} stamina! Stamina is now {self.current_stamina}/{self.max_stamina}")

    def gain_stamina(self, gain_amount: int):
        self.current_stamina = min(self.max_stamina, self.current_stamina + gain_amount)
        if self.debug_logs:
            log(f"{self.name} gained {gain_amount} stamina! Stamina is now {self.current_stamina}/{self.max_stamina}")

    def change_damage_type(self, new_damage_type: DamageType):
        self.damage_type = new_damage_type
        if self.debug_logs:
            log(f"{self.name}'s damage type has changed! Damage type is now {self.damage_type}")

    def change_character_class(self, new_character_class: CharacterClass):
        self.character_class = new_character_class
        if self.debug_logs:
            log(f"{self.name}'s class has changed! Class is now {self.character_class}")


def main():
    character = BaseCharacter("Test_character", 50, 10, 7, 45, 50, DamageType.EARTH, CharacterClass.BARBARIAN)
    print(character)

if __name__ == "__main__":
    main()