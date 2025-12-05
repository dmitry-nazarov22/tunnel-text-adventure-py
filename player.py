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
                if current.is_dark == 'True':
                    print_animated(f'You light up your newly found flashlight. This will help you see in here...')
                    current.is_dark = 'False'
                    state["rooms"][state["current"]].look("full")
                else:
                    print_animated('I should preserve battery for a darker room.')

            case "crowbar":
                all_directions = current.exits
                for direction in all_directions:
                    if state['rooms'][state["rooms"][state['current']].exits[direction]].is_locked == 'True':
                        print_animated(f'You break the ruined door and can now enter it.')
                        state['rooms'][state["rooms"][state['current']].exits[direction]].is_locked = 'False'
                        return True

                print_animated('There are no rooms that would need this.')
                return False

            case "keycard":
                all_directions = current.exits
                for direction in all_directions:
                    if state['rooms'][state["rooms"][state['current']].exits[direction]].is_keycard == 'True':
                        print_animated(f'You try your keycard and... ... ... IT WORKS! Green light lit up and the door opened.')
                        state['rooms'][state["rooms"][state['current']].exits[direction]].is_keycard = 'False'
                        self.inventory.remove("keycard")
                        return True

                print_animated('There are no rooms that would need this.')
                return False

            case _:
                print("Error: item not found")
                return False

    def craft_item(self, item1, item2):
        if item1 not in self.inventory or item2 not in self.inventory:
            print("You don't have that.")
            return False

        if (item1 == "pump" and item2 == "fuse") or (item1 == "fuse" and item2 == "pump"):
            self.inventory.remove("pump")
            self.inventory.remove("fuse")
            self.inventory.append("booster")
            print_animated(f'Combined {item1} and {item2} into a booster!')
            return True


