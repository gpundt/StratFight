from stratfight.enums.damage_types import DamageType
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
import textwrap

class Skill():
    def __init__(self, name: str, description: str, damage: int, level: int, mana_cost: int, stamina_cost: int, hp_cost: int, damage_type: DamageType, status_effect: StatusEffect, multi_target: bool, heal: bool, stat_buff: bool, buffed_stat: str, buff_percentage: float, debug_logs: bool = False):
        self.name = name
        self.description = description
        self.damage = damage
        self.level_damage_increase = round(self.damage * 0.1)
        self.level = level
        self.mana_cost = mana_cost
        if (self.mana_cost > 0):
            self.level_mana_cost_increase = round(self.mana_cost * 0.02)
        else:
            self.level_mana_cost_increase = 0
        
        self.stamina_cost = stamina_cost
        if (self.stamina_cost > 0):
            self.level_stamina_cost_increase = round(self.stamina_cost * 0.02)
        else:
            self.level_stamina_cost_increase = 0

        self.hp_cost = hp_cost
        if (self.hp_cost > 0):
            self.level_hp_cost_increase = round(self.hp_cost * 0.02)
        else:
            self.level_hp_cost_increase = 0

        self.damage_type = damage_type
        self.status_effect = status_effect
        self.multi_target = multi_target
        self.debug_tools = debug_logs
        self.heal = heal
        if self.heal:
            self.heal_amount = damage
        self.stat_buff = stat_buff
        if self.stat_buff:
            self.buff_percentage = buff_percentage
        else:
            self.buff_percentage = 0.0
        self.buffed_stat = buffed_stat
        

    def __str__(self) -> str:
        return textwrap.dedent(f"""
        Name:\t\t{self.name} lvl {self.level}
        Description:\t{self.description}
        Damage:\t\t{self.damage} 
        Damage Type:\t{self.damage_type.value}
        Status Effect:\t{self.status_effect.value}
        Multi-target:\t{self.multi_target}
        """).strip()

    def __shorthand__(self) -> str:
        return (f"{self.name} lvl {self.level}\tDamage:{self.damage} {self.damage_type.value}")
    
    # Increases stats when skill levels up
    def level_increase_stats(self):
        self.increase_damage(self.level_damage_increase)
        self.increase_mana_cost(self.level_mana_cost_increase)
        self.increase_stamina_cost(self.level_stamina_cost_increase)
        self.increase_health_cost(self.level_hp_cost_increase)

    # Levels up skill and increases stats
    def level_up(self):
        self.level += 1
        print(f"Skill [{self.name}] has leveled up to {self.level}!")
        self.level_increase_stats()
        print(f"[Stats Increased]\n{self}")
    
    # increases this skill's damage, and heal amount if applicable
    def increase_damage(self, increase_amount: int):
        self.damage += increase_amount
        if self.heal:
            self.heal_amount = self.damage

    # increases this skill's mana cost
    def increase_mana_cost(self, increase_amount: int):
        self.mana_cost += increase_amount

    # decreases this skill's mana cost
    def decrease_mana_cost(self, decrease_amount: int):
        self.mana_cost = min(0, self.mana_cost - decrease_amount)

    # increases this skill's stamina cost
    def increase_stamina_cost(self, increase_amount: int):
        self.stamina_cost += increase_amount

    # decreases this skill's stamina cost
    def decrease_stamina_cost(self, decrease_amount: int):
        self.stamina_cost = min(0, self.stamina_cost - decrease_amount)

    # increases this skill's health cost
    def increase_health_cost(self, increase_amount: int):
        self.hp_cost += increase_amount

    # decreases this skill's health cost
    def decrease_health_cost(self, decrease_amount: int):
        self.hp_cost = min(0, self.hp_cost - decrease_amount)

    # increases this skill's buff percentage
    def increase_buff_percentage(self, increase_amount: float):
        self.buff_percentage += increase_amount
        if (self.buff_percentage > 0.0):
            self.stat_buff = True

    # decreases this skill's buff percentage 
    def decrease_buff_percentage(self, decrease_amount: float):
        self.buff_percentage = min(0, self.buff_percentage - decrease_amount)
        if (self.buff_percentage == 0.0):
            self.stat_buff = False


## Testing Skill creation ##   
def main():
    test_skill = Skill("Test Skill", "a skill to test with", 40, 1, 10, 10, 0, DamageType.EARTH, StatusEffect.NONE, True, False, False, "NONE", 0)

if __name__ == "__main__":
    main()
