from dataclasses import dataclass


@dataclass
class Character:
    name: str

    def getPosition(self):
        return self.status.current_position
