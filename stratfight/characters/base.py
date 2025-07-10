from enums.damage_types import DamageType
from enums.character_classes import CharacterClass
from utils.logger import *

class BaseCharacter:
    def __init__(self, name: str, max_hp: int, base_attack: int, base_defense: int, max_mana: int, max_stamina: int, damage_type: DamageType, character_class: CharacterClass):
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

    def take_damage(self, damage_amount: int, damage_type: DamageType):
        ## Resistances and stuff ##
        self.current_hp -= max(0, damage_amount - self.current_defense)
        self.current_hp = max(0, self.current_hp)
        log(f"{self.name} took {damage_amount} damage! HP is now {self.current_hp}/{self.max_hp}")

    def gain_hp(self, heal_amount: int):
        self.current_hp += min(self.max_hp, self.current_hp + heal_amount)
        log(f"{self.name} gained {heal_amount} health! HP is now {self.current_hp}/{self.max_hp}")

    def lose_attack(self, loss_amount: int):
        self.current_attack = max(1, self.current_attack - loss_amount)
        log(f"{self.name}'s attack has dropped {loss_amount} points! Attack is now {self.current_attack}")

    def gain_attack(self, gain_amount: int):
        self.current_attack += gain_amount
        log(f"{self.name}'s attack has raised {gain_amount} points! Attack is now {self.current_attack}")

    def lose_defense(self, loss_amount: int):
        self.current_attack = max(0, self.current_defense - loss_amount)
        log(f"{self.name}'s defense has dropped {loss_amount} points! Defense is now {self.current_defense}")

    def gain_defense(self, gain_amount: int):
        self.current_defense += gain_amount
        log(f"{self.name}'s defense has raised {gain_amount} points! Defense is now {self.current_defense}")

    def spend_mana(self, cost: int):
        self.current_mana = max(0, self.current_mana - cost)
        log(f"{self.name} spent {cost} mana! Mana is now {self.current_mana}/{self.max_mana}")

    def gain_mana(self, gain_amount: int):
        self.current_mana = min(self.max_mana, self.current_mana + gain_amount)
        log(f"{self.name} gained {gain_amount} mana! Mana is now {self.current_mana}/{self.max_mana}")

    def spend_stamina(self, cost: int):
        self.current_stamina = max(0, self.current_stamina - cost)
        log(f"{self.name} spent {cost} stamina! Stamina is now {self.current_stamina}/{self.max_stamina}")

    def gain_stamina(self, gain_amount: int):
        self.current_stamina = min(self.max_stamina, self.current_stamina + gain_amount)
        log(f"{self.name} gained {gain_amount} stamina! Stamina is now {self.current_stamina}/{self.max_stamina}")

    def change_damage_type(self, new_damage_type: DamageType):
        self.damage_type = new_damage_type
        log(f"{self.name}'s damage type has changed! Damage type is now {self.damage_type}")

    def change_character_class(self, new_character_class: CharacterClass):
        self.character_class = new_character_class
        log(f"{self.name}'s class has changed! Class is now {self.character_class}")