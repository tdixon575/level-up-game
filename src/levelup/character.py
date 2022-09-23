from dataclasses import dataclass

class Warrior:
    name: str
    total_health: int
    attack_power: int
    inventory: dict = {}


@dataclass
class Character:
    name: str
    persona: str
    total_health: int = 5
    attack_power: int = 2
    speed: int = 1
    alive: bool = True


class Weapons:
    name: str
    attack_power: int
    # axe, sword, bow, wand, club, spear
