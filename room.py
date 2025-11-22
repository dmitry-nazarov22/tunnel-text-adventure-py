from ui import print_animated

class Room:
    def __init__(self, name, desc, exits, items=None):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items or []

    def look(self):
        print_animated(self.name)
        print_animated(self.desc)
        if self.items:
            print_animated(f'You see {self.items} laying on the floor')