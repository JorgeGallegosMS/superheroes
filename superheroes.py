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

    def defend(self, damage):
        '''Runs `block` method on each armor.
          Returns sum of all blocks
        '''
        total = damage
        for armor in self.armors:
            total -= armor.block()

        return total

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)

    def is_alive(self):
        return not self.current_health <= 0

if __name__ == '__main__':
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
