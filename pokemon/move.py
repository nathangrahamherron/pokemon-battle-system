class Move:
    def __init__(self, name: str, move_type: str, power: int):
        self.name = name
        self.type = move_type
        self.power = power

    def __repr__(self):
        return f"Move({self.name} {self.type} power={self.power})"
