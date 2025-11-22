class Room:
    def __init__(self, name, desc, exits, items=None):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items or []

    def look(self):
        print(self.name)
        print(self.desc)
        if self.items:
            print(f'You see {self.items} laying on the floor')