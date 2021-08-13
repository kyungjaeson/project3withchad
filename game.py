import random

import numpy as np

catchphrases = ["Victory will never come to those who aren't prepared to face defeat",
                "Life is a serious battle, and you have to use the tools you're given. It's more important to master the cards you're holding than to complain about the ones your opponents were dealt. Let us begin",
                "It\'s one thing to enjoy leisurely battles, but real battles can be a severe trial. Truly strong Trainers sometimes must be prepared to choose Pokemon that can win rather than their favorite Pokemon",
                "The master has failed more times than the beginner has even tried.",
                "I used to be a black belt. Isn't medical science great?",
                "What’s important is to never give up even if you lose.",
                "There’s no need to panic or stress. Take it easy. There’s plenty of time.",
                "I hate shorts, so I wear Jeans now. My life has chinged since then",
                "IT'S TIME TO DUE- Oh wrong game",
                "You crossed the wrong trainer's path. Prepare for a battle!"]
class Trainer:
    #
    # cities = [{"Pallet Town":{gymleader: "Brock, pokemon = [{geodude}]"}, "Viridian City", "Pewter City", "Cerulean City", "Vermilion City", "Lavender Town", "Celadon City", "Fuchsia City", "Cinnabar Island"}]
    # gymleaders = [{}]

    def __init__(self, name, pokemon_bench):
        self.name = name
        self.pokemon_bench = pokemon_bench
        self.catchphrase = catchphrases[random.randint(0, len(catchphrases)-1)]

    def battle(self, enemy_Trainer):
        print("""
────────▄███████████▄────────
─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────
────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────
───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───
──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──
─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─
██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██
███████████░░███░░███████████
██░░░░░░░██░░███░░██░░░░░░░██
██░░░░░░░░██░░░░░██░░░░░░░░██
██░░░░░░░░░███████░░░░░░░░░██
─██░░░░░░░░░░░░░░░░░░░░░░░██─
──██░░░░░░░░░░░░░░░░░░░░░██──
───██░░░░░░░░░░░░░░░░░░░██───
────███░░░░░░░░░░░░░░░███────
─────▀███░░░░░░░░░░░███▀─────
────────▀███████████▀────────
        """)
        print(f"{enemy_Trainer.catchphrase}"
              f"\n\n\n -------------BATTLE MUSIC -----------------")
        print("yeah, no, not enough time to do an entire rpg with this :/, sorry chad ")

        while len(self.pokemon_bench)> 0 and len(enemy_Trainer.pokemon_bench) > 0:
            print(f"You have {len(self.pokemon_bench)} pokemon"
                  f"\nThe enemy trainer {enemy_Trainer.name}, has {len(enemy_Trainer.pokemon_bench)} pokemon ")
            print("\nThese are the pokemon you have")
            for j, k in enumerate(self.pokemon_bench):
                print(f"{j + 1}. ", k.name)
            pokemon_selection = int(input('Pick a pokemon'))
            your_selection = self.pokemon_bench[pokemon_selection - 1]
            print(f"Trainer {self.name} sends out {your_selection.name}")
            print(f"\n Enemy Trainer has the following")
            for j, k in enumerate(enemy_Trainer.pokemon_bench):
                print(f"{j + 1}. ", k.name)
            enemy_pokemon_selection = int(input('Pick an enemy pokemon'))
            enemy_selection = enemy_Trainer.pokemon_bench[enemy_pokemon_selection - 1]
            print(f"Trainer {enemy_Trainer.name} sends out {enemy_selection.name}")
            result = your_selection.fight(enemy_selection)
            if result in self.pokemon_bench:
                if len(self.pokemon_bench) == 1:
                    print("\n YOU LOSE ")
                self.pokemon_bench.remove(result)
            else:
                if len(self.pokemon_bench) == 1:
                    print("\n YOU WIN!!!!!!!!!!!!!!!!!!!!")
                enemy_Trainer.pokemon_bench.remove(result)


class Pokemon:

    def __init__(self, name, type, moves, effort_values, health):
        self.name = name
        self.type = type
        self.moves = moves
        self.strength = effort_values['Attack']
        self.defense = effort_values['Defense']
        self.health = health
        self.phrase = ['', '']

    def fight(self, enemy_pokemon):
        # display
        print(
              f"\n{enemy_pokemon.name} is sent out to fight"
              # f"\n Go {self.name = 
              f"\n-------YOUR POKEMMON STATS--------"
              f"\nTYPE : {self.type}"
              f"\nATTACK : {self.strength}"
              f"\nDEFENSE : {self.defense}"
              f"\nLVL : {3 * (1 + np.mean([self.strength, self.defense]))}"
              f"\n \t -VS- "
              f"\n-------OTHER POKEMON STATS--------"
              f"\nTYPE : {enemy_pokemon.type}"
              f"\nATTACK : {enemy_pokemon.strength}"
              f"\nDEFENSE : {enemy_pokemon.defense}"
              f"\nLVL : {3 * (1 + np.mean([enemy_pokemon.strength, enemy_pokemon.defense]))}")

        # type mechanics in fight
        types = ['Fire', 'Water', 'Grass']
        for j, k in enumerate(types):
            if self.type == k:
                # same type
                if enemy_pokemon.type == k:
                    self.phrase[0] = "It\'s not very effective"
                    self.phrase[1] = "It\'s not very effective"
                # different type enemy advantage
                if enemy_pokemon.type == types[(j + 1) % 3]:
                    enemy_pokemon.strength *= 2
                    enemy_pokemon.defense *= 2
                    self.strength /= 2
                    self.defense /= 2
                    self.phrase[0] = "It\'s not very effective"
                    self.phrase[1] = "It\'s super effective"
                # different type your advantage
                if enemy_pokemon.type == types[(j + 2) % 3]:
                    enemy_pokemon.strength /= 2
                    enemy_pokemon.defense /= 2
                    self.strength *= 2
                    self.defense *= 2
                    self.phrase[0] = "It\'s super effective"
                    self.phrase[1] = "It\'s not very effective"
        # fight tracker
        while (self.health > 0) and (enemy_pokemon.health > 0):
            print(f"{self.name} has {self.health} health"
                  f"\n{enemy_pokemon.name} has {enemy_pokemon.health} health"
                  f"\nYour turn")
            for j, k in enumerate(self.moves):
                print(f"{j + 1}. ", k)
            move_selection = int(input('Pick a move'))
            print(f"{self.name} used {self.moves[move_selection - 1]}")
            print(f"\n {self.phrase[0]}"
                  f"\nit deals {self.strength} damage")

            # damage calculation
            enemy_pokemon.health -= self.strength
            if enemy_pokemon.health <= 0:
                print(f"\n------{enemy_pokemon.name} has fainted-----")
                return enemy_pokemon

            #enemy turn
            print(f"\n{self.name} has {self.health} health"
                  f"\n{enemy_pokemon.name} has {enemy_pokemon.health} health"
                  f"\nEnemy turn")
            for j, k in enumerate(enemy_pokemon.moves):
                print(f"{j + 1}. ", k)
            move_selection = int(input('Pick a move'))
            print(f"{enemy_pokemon.name} used {enemy_pokemon.moves[move_selection - 1]}")
            print(f"\n {self.phrase[1]}"
                  f"\nit deals {enemy_pokemon.strength} damage")

            # damage calculation
            self.health -= enemy_pokemon.strength
            if self.health <= 0:
                print(f"\n-----{self.name} has fainted-----")
                return self

if __name__ == '__main__':
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                        {'Attack': 12, 'Defense': 8}, 30)
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                        {'Attack': 10, 'Defense': 10}, 30)
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],
                       {'Attack': 8, 'Defense': 12}, 30)

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                         {'Attack': 4, 'Defense': 2}, 10)
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'Attack': 3, 'Defense': 3},
                       10)
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],
                        {'Attack': 2, 'Defense': 4}, 10)

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                         {'Attack': 6, 'Defense': 5}, 20)
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                        {'Attack': 5, 'Defense': 5}, 20)
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],
                      {'Attack': 4, 'Defense': 6}, 20)

    Mike = Trainer('Mike', [Ivysaur, Squirtle, Charizard])
    You = Trainer('Jason', [Blastoise,Charmeleon,Venusaur])

    You.battle(Mike)
