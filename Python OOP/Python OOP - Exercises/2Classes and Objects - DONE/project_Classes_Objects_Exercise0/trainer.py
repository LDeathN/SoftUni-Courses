from project.pokemon import Pokemon

class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []


    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"


    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"


    def trainer_data(self):
        result = []
        result.append(f"Pokemon Trainer {self.name}")
        result.append(f"Pokemon count {len(self.pokemons)}")
        for pokemon in self.pokemons:
            result.append(f"- {pokemon.name} with health {pokemon.health}")

        return "\n".join(result)
