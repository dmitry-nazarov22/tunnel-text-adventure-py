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

            case "adrenaline":
                if self.energy <= 90:
                    self.inventory.remove("adrenaline")
                    print_animated(state["items"][name].use_msg)
                    self.energy += 10
                    return True

                print_animated(state["items"][name].error_msg)
                return False

            case "soda":
                if self.energy <= 95:
                    self.inventory.remove("adrenaline")
                    print_animated(state["items"][name].use_msg)
                    self.energy += 5
                    return True

                print_animated(state["items"][name].error_msg)
                return False

            case "detonator":
                print_animated(state["items"][name].error_msg)
                return False

            case "dynamite":
                print_animated(state["items"][name].error_msg)
                return False

            case "box":
                print_animated(state["items"][name].error_msg)
                return False

            case "tools":
                print_animated(state["items"][name].error_msg)
                return False

            case "folder":
                print_animated(state["items"][name].error_msg)
                return False

            case "notes":
                print_animated(state["items"][name].error_msg)
                return False

            case "toolbox":
                print_animated(state["items"][name].error_msg)
                return False

            case "logbook":
                print_animated(state["items"][name].error_msg)
                return False

            case _:
                print("Error: item not found")
                return False

    def craft_item(self, state, item1, item2):
        if item1 not in self.inventory or item2 not in self.inventory:
            print("You don't have that.")
            return False

        if (item1 == "detonator" and item2 == "dynamite") or (item1 == "dynamite" and item2 == "detonator"):
            result = "c4"
            self.inventory.remove("detonator")
            self.inventory.remove("dynamite")
            self.inventory.append(result)
            print_animated(f'Combined {item1} and {item2} into a {result}!')
            print_animated(state["items"][result].desc)
            return True

        if (item1 == "box" and item2 == "tools") or (item1 == "tools" and item2 == "box"):
            result = "toolbox"
            self.inventory.remove("tools")
            self.inventory.remove("box")
            self.inventory.append("toolbox")
            print_animated(f'Combined {item1} and {item2} into a {result}!')
            print_animated(state["items"][result].desc)
            return True

        if (item1 == "notes" and item2 == "folder") or (item1 == "folder" and item2 == "notes"):
            result = "logbook"
            self.inventory.remove("notes")
            self.inventory.remove("folder")
            self.inventory.append("logbook")
            print_animated(f'Combined {item1} and {item2} into a {result}!')
            print_animated(state["items"][result].desc)
            return True


