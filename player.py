class Player:
    def __init__(self):
        self.inventory = []
        self.energy = 100
        self.score = 0

    def add_item(self, name):
        print(f"You picked up {name}.")
        self.inventory.append(name)

    def show_inventory(self):
        if self.inventory:
            print("You carry:", ", ".join(self.inventory))
        else:
            print("You carry nothing.")

    def use_item(self, name):
        if name not in self.inventory:
            print("You don't have that.")
            return False

        self.inventory.remove(name)
        return True
