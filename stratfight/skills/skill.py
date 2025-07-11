from stratfight.enums.damage_types import DamageType
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
import textwrap

class Skill():
    def __init__(self, name: str, description: str, damage: int, level: int, mana_cost: int, stamina_cost: int, hp_cost: int, damage_type: DamageType, status_effect: StatusEffect, multi_target: bool, heal: bool, stat_buff: bool, buffed_stat: str, buff_percentage: float, debug_logs: bool = False):
        self.name = name
        self.description = description
        self.damage = damage
        self.level = level
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost
        self.hp_cost = hp_cost
        self.damage_type = damage_type
        self.status_effect = status_effect
        self.multi_target = multi_target
        self.debug_tools = debug_logs
        self.heal = heal
        if self.heal:
            self.heal_amount = damage
        self.stat_buff = stat_buff
        self.buffed_stat = buffed_stat
        self.buff_percentage = buff_percentage

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
