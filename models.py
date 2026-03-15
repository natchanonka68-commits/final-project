from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp, attack_power):
        self._name = name
        self._hp = hp
        self._attack_power = attack_power

    @abstractmethod
    def unique_skill(self):
        pass

    def take_damage(self, damage):
        self._hp -= damage
        return f"{self._name} received {damage} damage. HP: {self._hp}"

class Warrior(Character):
    def unique_skill(self):
        damage = self._attack_power * 1.5
        return f"{self._name} uses Shield Bash! Deals {damage} damage."

class Mage(Character):
    def unique_skill(self):
        damage = self._attack_power * 2.2
        return f"{self._name} casts Fireball! Deals {damage} magic damage."
