from enum import Enum

## List of status effects available to characters ##
class StatusEffect(Enum):
    POISON = "Poison"
    BURN = "Burn"
    IMMUNE = "Immune"
    FROZEN = "Frozen"
    PARALYZED = "Paralyzed"
    FEAR = "Fear"
    BLIND = "Blind"
    MUTE = "Mute"
    NONE = "None"