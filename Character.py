class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, enemy):
        pass

class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}, используя {self.weapon}!")

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self, hero):
        print(f"{self.name} атакует {hero.name}, нанося целых {self.damage} урона!")


hero = Hero("Cat", 150, "gun")
enemy = Enemy("Fish", 80, 20)

hero.attack(enemy)
enemy.attack(hero)

