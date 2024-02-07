import random
class Archer:
    name = ''
    hp = 0
    damage = 0
    accuracy = 0
    agility = 0

    def __init__(self, name, hp, damage, accuracy, agility):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.accuracy = accuracy
        self.agility = agility

    def get_info(self):
        print(f"Archer\nName:{self.name}")
        print(f"Health points:{self.hp}")
        print(f"Damage:{self.damage}")
        print(f"Accuracy:{self.accuracy}")
        print(f"Agility:{self.agility}")

    def level_up(self):
        self.hp += 10
        self.damage += 6
        self.accuracy += 0.05
        if self.accuracy >= 2:
            self.accuracy = 2
            print("The archer has reached maximum level accuracy")
        self.agility += 2
        if self.agility >= 25:
            self.agility = 25
            print("The archer has reached maximum level agility")

    def damage_dealt(self, enemy):
        enemy.get_damage(self.damage * self.accuracy)

    def get_damage(self, damage):
        if self.agility/100 >= random.random():
            print(f"Archer {self.name} dodged the damage")
        else:
            self.hp -= damage