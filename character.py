from ui import print_animated

class Character:
    def __init__(self, id, name, desc, location, msg1, msg2, msg3, task_msg, items, task_item):
        self.id = id
        self.name = name
        self.desc = desc
        self.location = location
        self.msg1 = msg1
        self.msg2 = msg2
        self.msg3 = msg3
        self.task_msg = task_msg
        self.items = items
        self.task_item = task_item

        self.talk_counter = 0

    def talk(self, state, room):
        print("\n" + self.name)

        if self.task_item in self.items:
            print_animated(self.task_msg)
            room.characters.remove(self)

            state["player"].score += 100
            state[self.id + "_quest"] = True

            if "radio" in self.items:
                state["player"].inventory.append("radio")
                self.items.remove("radio")
            return

        if self.talk_counter == 0:
            print_animated(self.msg1)
            self.talk_counter += 1
        elif self.talk_counter < 2:
            print_animated(self.msg2)
            self.talk_counter += 1
        else:
            print_animated(self.msg3)

    def give(self, player, room, item):
        if item in player.inventory:
            if item == self.task_item:
                player.inventory.remove(self.task_item)
                self.items.append(self.task_item)
                print_animated("Oh, you found it!  Talk to me when you have time.")
            else:
                print_animated("Thank you. But I don't need that... You should have it.")
        else:
            print_animated("You don't have that.")