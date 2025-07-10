from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
import textwrap

class BaseCharacter:
    def __init__(self, name: str, max_hp: int, base_attack: int, base_defense: int, max_mana: int, max_stamina: int, damage_type: DamageType, character_class: CharacterClass, status_effects: list[StatusEffect], level: int, debug_logs: bool = False):
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
        self.status_effects = status_effects
        self.level = level
        self.is_alive = (self.current_hp > 0)
        self.debug_logs = debug_logs

    def __str__(self):
        return textwrap.dedent(f"""
            Name:\t\t{self.name}
            Level:\t\t{self.level}
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
    
    def full_restore_hp(self):
        self.current_hp = self.max_hp
        if self.debug_logs:
            log(f"{self.name} has fully restored their Health! HP is now {self.current_hp}/{self.max_hp}")

    def full_restore_mana(self):
        self.current_mana = self.max_mana
        if self.debug_logs:
            log(f"{self.name} has fully restored their Mana! Mana is now {self.current_mana}/{self.max_mana}")

    def full_restore_stamina(self):
        self.current_stamina = self.max_stamina
        if self.debug_logs:
            log(f"{self.name} has fully restored their Stamina! Stamina is now {self.current_stamina}/{self.max_stamina}")

    def full_restore_all(self):
        self.full_restore_hp()
        self.full_restore_mana()
        self.full_restore_stamina()

    def lose_attack(self, loss_amount: int):
        self.current_attack = max(1, self.current_attack - loss_amount)
        if self.debug_logs:
            log(f"{self.name}'s attack has dropped {loss_amount} points! Attack is now {self.current_attack}")

    def gain_attack(self, gain_amount: int):
        self.current_attack += gain_amount
        if self.debug_logs:
            log(f"{self.name}'s attack has raised {gain_amount} points! Attack is now {self.current_attack}")

    def restore_attack(self):
        if (self.current_attack > self.base_attack):
            if self.debug_logs:
                log(f"{self.name}'s attack is buffed! Remaining at {self.current_attack}")
        elif (self.current_attack < self.base_attack):
            self.current_attack = self.base_attack
            if self.debug_logs:
                log(f"{self.name}'s attack has been restored to base! Attack: {self.current_attack}")

    def lose_defense(self, loss_amount: int):
        self.current_defense = max(0, self.current_defense - loss_amount)
        if self.debug_logs:
            log(f"{self.name}'s defense has dropped {loss_amount} points! Defense is now {self.current_defense}")

    def gain_defense(self, gain_amount: int):
        self.current_defense += gain_amount
        if self.debug_logs:
            log(f"{self.name}'s defense has raised {gain_amount} points! Defense is now {self.current_defense}")

    def restore_defense(self):
        if (self.current_defense > self.base_defense):
            if self.debug_logs:
                log(f"{self.name}'s defense is buffed! Remaining at {self.current_defense}")
        elif (self.current_defense < self.base_defense):
            self.current_defense = self.base_defense
            if self.debug_logs:
                log(f"{self.name}'s defense has been restored to base! Defense: {self.current_defense}")

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

    def full_restore_all(self):
        self.full_restore_hp()
        self.full_restore_mana()
        self.full_restore_stamina()
        self.restore_attack()
        self.restore_defense()
        self.wipe_all_status_effects()

    def gain_status_effect(self, new_status_effect: StatusEffect):
        if (new_status_effect not in self.status_effects):
            self.status_effects.append(new_status_effect)
            if self.debug_logs:
                log(f"{self.name} gained a new status effect: {new_status_effect.name}")
        
    def remove_status_effect(self, removed_status_effect: StatusEffect):
        if (removed_status_effect in self.status_effects):
            self.status_effects.remove(removed_status_effect)
            if self.debug_logs:
                log(f"{self.name} lost a status effect: {removed_status_effect}")

    def wipe_all_status_effects(self):
        self.status_effects = []

    def change_damage_type(self, new_damage_type: DamageType):
        self.damage_type = new_damage_type
        if self.debug_logs:
            log(f"{self.name}'s damage type has changed! Damage type is now {self.damage_type}")

    def change_character_class(self, new_character_class: CharacterClass):
        self.character_class = new_character_class
        if self.debug_logs:
            log(f"{self.name}'s class has changed! Class is now {self.character_class}")

    def increase_max_hp(self, increase_amount: int):
        self.max_hp += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s max HP has increased to {self.max_hp}!")

    def decrease_max_hp(self, decrease_amount: int):
        self.max_hp = max(0, self.max_hp - decrease_amount)
        self.current_hp = min(self.current_hp, self.max_hp)
        if self.debug_logs:
            log(f"{self.name}'s max HP has decreased to {self.max_hp}!")

    def increase_base_attack(self, increase_amount: int):
        self.base_attack += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s base attack has increased to {self.base_attack}!")

    def increase_base_defense(self, increase_amount: int):
        self.base_defense += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s base defense has increased to {self.base_defense}!")

    def increase_max_mana(self, increase_amount: int):
        self.max_mana += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s max Mana has increased to {self.max_mana}!")

    def increase_max_stamina(self, increase_amount: int):
        self.max_stamina += increase_amount
        if self.debug_logs:
            log(f"{self.name}'s max Stamina has increased to {self.max_stamina}!")


def main():
    character = BaseCharacter("Test_character", 50, 10, 7, 45, 50, DamageType.EARTH, CharacterClass.BARBARIAN, status_effects=[], level=4)
    print(character)

if __name__ == "__main__":
    main()
