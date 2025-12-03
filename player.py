from ui import print_animated

class Player:
    def __init__(self):
        self.inventory = []
        self.energy = 100
        self.score = 0

    def add_item(self, name, room):
        if name in room.items:
            print_animated(f"You picked up {name}.")
            self.inventory.append(name)
            room.items.remove(name)
        else:
            print("No such items around.")

    def show_inventory(self):
        if self.inventory:
            print("You carry:", ", ".join(self.inventory))
        else:
            print("You carry nothing.")

    def use_item(self, state, name):
        if name not in self.inventory:
            print("You don't have that.")
            return False

        current = state["rooms"][state["current"]]

        match name:
            case "flashlight":
                if state['current'] == "junction1":
                    print('YES')
                    print_animated(f'You light up your newly found flashlight. This will help you see in the dark tunnel...')
                    print(state['rooms'][state["rooms"][state['current']].exits["west"]].is_locked)
                    state['rooms'][state["rooms"][state['current']].exits["west"]].is_locked = 'False'
                else:
                    print_animated('There are no rooms that would need this.')

            case _:
                print("Error: item not found")
                return False
