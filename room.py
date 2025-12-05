from ui import print_animated

class Room:
    def __init__(self, name, been_here, desc_full, desc_short, desc_dark, is_keycard, is_locked, is_dark, exits, items=None):
        self.name = name
        self.been_here = been_here
        self.desc_full = desc_full
        self.desc_short = desc_short
        self.desc_dark = desc_dark
        self.is_locked = is_locked
        self.is_dark = is_dark
        self.is_keycard = is_keycard
        self.exits = exits
        self.items = items or []

    def look(self, desc_id):
        print_animated(self.name)
        if desc_id == 'full':
            print_animated(self.desc_full)
        elif desc_id == 'short':
            print_animated(self.desc_short)
        elif desc_id == 'dark':
            print_animated(self.desc_dark)
        else:
            print('ERROR: world.json contains wrong format of description.')

        if self.items:
            print_animated(f'You see {self.items} laying on the floor')