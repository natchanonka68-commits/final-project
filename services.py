from models import Warrior, Mage

class CharacterFactory:
    @staticmethod
    def create_character(char_type, name):
        if char_type.lower() == "warrior":
            return Warrior(name, 150, 25)
        elif char_type.lower() == "mage":
            return Mage(name, 80, 45)
        return None

class GameEngine:
    def __init__(self, logger):
        self.logger = logger
        self.players = []

    def add_player(self, character):
        if character:
            self.players.append(character)
            self.logger.info(f"Character {character._name} added to the team.")

    def run_battle_round(self):
        results = []
        for p in self.players:
            results.append(p.unique_skill())
        return results

class ConsoleLogger:
    def info(self, message):
        print(f"[LOG] {message}")
