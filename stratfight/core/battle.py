from stratfight.characters.base import BaseCharacter
from stratfight.enums.damage_types import DamageType
from stratfight.enums.character_classes import CharacterClass
from stratfight.utils.logger import log
from stratfight.status_effects.effects import StatusEffect
from stratfight.characters.player import Player
from stratfight.characters.enemy import Enemy
import stratfight.core.damage as damage
from stratfight.skills.skill import Skill
from stratfight.core.turn_manager import Turn
import random
import textwrap

class Battle():
    def __init__(self, battle_number: int, all_enemies: list[Enemy], players: list[Player], first_battle: bool = True):
        self.battle_number = battle_number
        
        self.all_enemies = all_enemies
        self.players = players
        self.first_battle = first_battle
        
        if self.first_battle:
            self.current_players = self.form_team()
        else:
            self.current_players = self.players
        self.current_enemies = self.load_random_enemies()
            
        self.turn = Turn(1, self.current_players, self.current_enemies)

    def __str__(self):
        string = "# ===== Players ===== #"
        for player in self.players:
            string += player.__shorthand__() + "\n"

        string += "\n# ===== Enemies ===== #"
        for enemy in self.enemies:
            string += enemy.__shorthand__() + "\n"
        return string
    
    def load_random_enemies(self) -> list[Enemy]:
        pass

    def select_team_size(self) -> int:
        team_size = input("Select your team size: (1 - 5)\n>>>\t")
        try:
            if (int(team_size) > 5 or int(team_size) < 1):
                print("[!] Invalid Choice [!]")
                return self.select_team_size()
            else:
                return team_size
        except:
            print("[!] Invalid Choice [!]")
            return self.select_team_size()
        
    def select_team_member(self) -> Player:
        print("Select a member for your team:")
        for player in self.players:
            print(f"{self.players.index(player)+1}) {player.__shorthand__()}")
        choice = input(">>>\t")
        try:
            chosen_player = self.players[choice-1]
            return chosen_player
        except:
            print("[!] Invalid Choice [!]")
            return self.select_team_member()
            
    
    def form_team(self):
        selected_team = []
        team_size = self.select_team_size()
        for _ in range(team_size):
            selected_team.append(self.select_team_member())
        
        print("Your team has been selected!")
        for player in selected_team:
            print(player.__shorthand__())


    def commence_battle(self, difficulty: int) -> int:
        enemies = self.load_random_enemies()
