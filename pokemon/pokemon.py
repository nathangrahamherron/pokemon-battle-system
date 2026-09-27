from pokemon.move import Move


class Pokemon:
    def __init__(self, name, types, hp, attack, defense, speed, moves: list[Move]):
        self.name = name
        self.types = types
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves

    @property
    def is_fainted(self) -> bool:
        return self.hp <= 0

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)

    def __repr__(self):
        return f"{self.name} | {'/'.join(self.types)} | HP:{self.hp}/{self.max_hp} | Atk:{self.attack} Def:{self.defense} Spd:{self.speed} | Moves: {', '.join([move.name for move in self.moves])}"
