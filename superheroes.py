import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer'''

        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        max_damage = self.attack_strength
        damage = random.randint(0, max_damage)
        return damage

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        max_block = self.max_block
        block = random.randint(0, max_block)
        return block

class Weapon(Ability):
    def attack(self):
        max_damage = self.attack_strength
        damage = random.randint(max_damage//2, max_damage)
        return damage

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        '''Add ability to list of abilities'''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        total = 0
        for ability in self.abilities:
            total += ability.attack()

        return total

    def defend(self):
        '''Runs `block` method on each armor.
          Returns sum of all blocks
        '''
        total = 0
        for armor in self.armors:
            total += armor.block()

        return total

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def is_alive(self):
        return not self.current_health <= 0

    def fight(self, opponent):
        alive = self.is_alive()
        opp_alive = opponent.is_alive()
        while alive and opp_alive:
            my_abilities = len(self.abilities)
            opp_abilities = len(opponent.abilities)

            if my_abilities == 0 and opp_abilities == 0:
                print("Draw")
            else:
                damage = self.attack()
                opponent.take_damage(damage)
                if opponent.is_alive():
                    opp_damage = opponent.attack()
                    self.take_damage(opp_damage)
                    if self.is_alive():
                        continue
                    else:
                        print(f"{opponent.name} has won the match")
                        self.add_death(1)
                        opponent.add_kill(1)
                        break
                else:
                    print(f"{self.name} has won the match")
                    self.add_kill(1)
                    opponent.add_death(1)
                    break

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        heroes = self.heroes
        for index,hero in enumerate(heroes):
            if name == hero.name:
                heroes.pop(index)
                print(f"{hero.name} has been removed from the team")

        return 0

    def view_all_heroes(self):
        heroes = self.heroes
        if len(heroes) != 0:
            for hero in heroes:
                print(hero.name)
        else:
            print("Could not find any heroes")

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, enemy_team):
        my_hero = self.heroes[random.randint(0, len(self.heroes) - 1)]
        enemy_hero = enemy_team.heroes[random.randint(0, len(enemy_team.heroes) - 1)]

        my_hero.fight(enemy_hero)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} has {hero.kills} kills and {hero.deaths} deaths")


if __name__ == '__main__':
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    # ability1 = Weapon("Super Speed", 300)
    # ability2 = Weapon("Super Eyes", 130)
    # ability3 = Weapon("Wizard Wand", 80)
    # ability4 = Weapon("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    team1 = Team("Best team ever")
    team1.view_all_heroes()
