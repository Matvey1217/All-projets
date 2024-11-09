class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Character's name is {self.name}")

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = Inventory()  

    def introduce(self):
        print(f"Player's name is {self.name}")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, block):
        self.items.append(block)
        print(f"Added '{block}' to inventory")


player = Player("Matvey")
player.introduce()
player.inventory.add_item("Block")
