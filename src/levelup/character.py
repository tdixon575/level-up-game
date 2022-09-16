from dataclasses import dataclass

@dataclass
class Character:
    name: str

    def move(self, direction) -> None:
        print(f"Moving {direction}")
        
        self.status.character.move(direction)
