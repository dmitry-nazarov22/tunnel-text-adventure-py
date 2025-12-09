from ui import print_animated

class Player:
    def __init__(self):
        self.inventory = []
        self.energy = 100
        self.score = 0

    def add_item(self, state, name, room):
        if name in room.items:
            print_animated(f"You picked up {name}.")
            print_animated(state["items"][name].desc)
            self.inventory.append(name)
            room.items.remove(name)
        else:
            print("No such items around.")

    def drop_item(self, name, room):
        if name in self.inventory:
            print_animated(f"You dropped {name}.")
            self.inventory.remove(name)
            room.items.append(name)
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
                    print_animated(state["items"][name].use_msg)
                    current.is_dark = 'False'
                    state["rooms"][state["current"]].look("full")
                else:
                    print_animated(state["items"][name].error_msg)

            case "crowbar":
                all_directions = current.exits
                for direction in all_directions:
                    if state['rooms'][state["rooms"][state['current']].exits[direction]].is_locked == 'True':
                        print_animated(state["items"][name].use_msg)
                        state['rooms'][state["rooms"][state['current']].exits[direction]].is_locked = 'False'
                        return True

                print_animated(state["items"][name].error_msg)
                return False

            case "keycard":
                all_directions = current.exits
                for direction in all_directions:
                    if state['rooms'][state["rooms"][state['current']].exits[direction]].is_keycard == 'True':
                        print_animated(state["items"][name].use_msg)
                        state['rooms'][state["rooms"][state['current']].exits[direction]].is_keycard = 'False'
                        self.inventory.remove("keycard")
                        return True

                print_animated(state["items"][name].error_msg)
                return False

            case "c4":
                all_directions = current.exits
                for direction in all_directions:
                    if state['rooms'][state["rooms"][state['current']].exits[direction]].is_blowable == 'True':
                        print_animated(state["items"][name].use_msg)
                        self.inventory.remove("c4")
                        self.inventory.append("remote")
                        return True

                print_animated(state["items"][name].error_msg)
                return False

            case "remote":
                if state["current"] == 'sealed_door':
                    print_animated("... ... ... ... does it work?? ... BOOOOOOOM!!!")
                    state['running'] = False
                    return True
                else:
                    print_animated(state["items"][name].use_msg)
                    state['rooms']['escape_tunnel'].is_blowable = 'False'
                    return True

            case "detonator":
                print_animated(state["items"][name].error_msg)
                return True

            case "dynamite":
                print_animated(state["items"][name].error_msg)
                return True

            case _:
                print("Error: item not found")
                return False

    def craft_item(self, item1, item2):
        if item1 not in self.inventory or item2 not in self.inventory:
            print("You don't have that.")
            return False

        if (item1 == "detonator" and item2 == "dynamite") or (item1 == "dynamite" and item2 == "detonator"):
            self.inventory.remove("detonator")
            self.inventory.remove("dynamite")
            self.inventory.append("c4")
            print_animated(f'Combined {item1} and {item2} into a c4!')
            return True


