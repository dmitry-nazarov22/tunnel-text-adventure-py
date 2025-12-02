from ui import print_animated

class Room:
    def __init__(self, name, desc_full, desc_short, is_locked, exits, items=None):
        self.name = name
        self.desc_full = desc_full
        self.desc_short = desc_short
        self.is_locked = is_locked
        self.exits = exits
        self.items = items or []

    def look(self, desc_id):
        print_animated(self.name)
        if desc_id == 'full':
            print_animated(self.desc_full)
        elif desc_id == 'short':
            print_animated(self.desc_short)
        else:
            print('ERROR: world.json contains wrong format of description.')

        if self.items:
            print_animated(f'You see {self.items} laying on the floor')