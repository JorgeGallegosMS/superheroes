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

if __name__ == '__main__':
    ability = Ability("Toss", 20)
    print(ability.name)
    print(ability.attack())
