import json
from pokemon.pokemon import Pokemon
from pokemon.move import Move


def load_pokemon(filepath: str = "pokemon_data.json") -> list[Pokemon]:
    with open(filepath, "r") as f:
        data = json.load(f)

    pokemon_list = []
    for entry in data:
        moves = [
            Move(m["name"], m["move_type"], m["power"])
            for m in entry["moves"]
        ]
        pokemon = Pokemon(
            name=entry["name"],
            types=entry["types"],
            hp=entry["hp"],
            attack=entry["attack"],
            defense=entry["defense"],
            speed=entry["speed"],
            moves=moves,
        )
        pokemon_list.append(pokemon)

    return pokemon_list


if __name__ == "__main__":
    pokemon_list = load_pokemon()
    for p in pokemon_list:
        print(p)
