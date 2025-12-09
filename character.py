from ui import print_animated

class Character:
    def __init__(self, name, desc, location, msg1, msg2, msg3, task_msg, items, task_item):
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

        if self.task_item in room.items:
            print_animated(self.task_msg)
            room.items.remove(self.task_item)
            self.items.append(self.task_item)
            room.characters.remove(self)

            return

        if self.talk_counter == 0:
            print_animated(self.msg1)
            self.talk_counter += 1
        elif self.talk_counter < 2:
            print_animated(self.msg2)
            self.talk_counter += 1
        else:
            print_animated(self.msg3)