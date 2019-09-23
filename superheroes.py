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
                        break
                else:
                    print(f"{self.name} has won the match")
                    break


if __name__ == '__main__':
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Weapon("Super Speed", 300)
    ability2 = Weapon("Super Eyes", 130)
    ability3 = Weapon("Wizard Wand", 80)
    ability4 = Weapon("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
