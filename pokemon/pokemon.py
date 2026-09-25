class Move:
    def __init__(self, name: str, move_type: str, power: int):
        self.name = name
        self.type = move_type
        self.power = power

    def __repr__(self):
        return f"Move({self.name}, {self.type}, power={self.power})"


class Pokemon:
    def __init__(self, name: str, types: list[str], hp: int, attack: int,
                 defense: int, speed: int, moves: list[Move]):
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
        return f"{self.name} ({'/'.join(self.types)}) HP:{self.hp}/{self.max_hp}"


# --- 3 starting Pokemon ---

charmander = Pokemon(
    name="Charmander",
    types=["Fire"],
    hp=39, attack=52, defense=43, speed=65,
    moves=[Move("Ember", "Fire", 40)],
)

squirtle = Pokemon(
    name="Squirtle",
    types=["Water"],
    hp=44, attack=48, defense=65, speed=43,
    moves=[Move("Water Gun", "Water", 40)],
)

bulbasaur = Pokemon(
    name="Bulbasaur",
    types=["Grass"],
    hp=45, attack=49, defense=49, speed=45,
    moves=[Move("Vine Whip", "Grass", 45)],
)

STARTER_POKEMON = [charmander, squirtle, bulbasaur]


if __name__ == "__main__":
    for p in STARTER_POKEMON:
        print(p)
