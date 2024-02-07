# Archer Class

This Python class represents an Archer character in a game. The Archer has attributes such as name, health points (hp), damage, accuracy, and agility. The class includes methods for initializing the Archer, getting information about the Archer, leveling up the Archer, dealing damage to an enemy, and receiving damage.

## Attributes:
- name: Name of the Archer
- hp: Health points of the Archer
- damage: Damage dealt by the Archer
- accuracy: Accuracy level of the Archer
- agility: Agility level of the Archer

## Methods:
- init(self, name, hp, damage, accuracy, agility): Initialize the Archer with specified attributes.
- get_info(self): Print information about the Archer.
- level_up(self): Increase the Archer's stats when leveling up.
- damage_dealt(self, enemy): Deal damage to an enemy based on the Archer's damage and accuracy.
- get_damage(self, damage): Receive damage from an enemy attack.

### Example Usage:
    python
    import random

    class Archer:
        name = ''
        hp = 0
        damage = 0
        accuracy = 0
        agility = 0
    
    def init(self, name, hp, damage, accuracy, agility):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.accuracy = accuracy
        self.agility = agility

    def get_info(self):
        print(f"Archer\\nName:{self.name}")
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
