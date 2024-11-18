class Character:
    def __init__(self, name, health, energy, weapon):
        self.name = name
        self.__health = health
        self.__energy = energy
        self.__weapon = weapon

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} атакует используя {self.__weapon}!")
        else:
            print("Недостаточно энергии ")

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health > 0:
            print(f"{self.name} получил {damage} урона. Текущее здоровье: {self.__health}")
        else:
            self.__health = 0
            print(f"Персонаж {self.name} погиб")

    def equip_weapon(self, weapon):
        self.__weapon = weapon
        print(f"{self.name} теперь использует {self.__weapon}")

    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self.__health}, Энергия: {self.__energy}, Оружие: {self.__weapon}"



character = Character("Hero", 100, 100, "Кинжал")


character.equip_weapon("Кинжал")
print(f"После экипировки: {character.get_status()}")


character.take_damage(60)
print(f"После получения урона: {character.get_status()}")


print("Hero снова атакует...")
character.attack()
print(f"После атаки: {character.get_status()}")



