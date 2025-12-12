from ui import print_animated, print_block

class Room:
    def __init__(self, name, been_here, desc_full, desc_short, desc_dark, is_keycard, is_blowable, is_locked, is_dark, exits, items, characters):
        self.name = name
        self.been_here = been_here
        self.desc_full = desc_full
        self.desc_short = desc_short
        self.desc_dark = desc_dark
        self.is_locked = is_locked
        self.is_dark = is_dark
        self.is_keycard = is_keycard
        self.is_blowable = is_blowable
        self.exits = exits
        self.items = items or []
        self.characters = characters

    def look(self, desc_id, state):
        print("\n" + self.name + "\n")
        if desc_id == 'full':
            print_block(self.desc_full)
        elif desc_id == 'short':
            print_block(self.desc_short)
        elif desc_id == 'dark':
            print_block(self.desc_dark)
        else:
            print('ERROR: world.json contains wrong format of description.')

        if self.is_dark == "False":
            if self.characters:
                for character in self.characters:
                    print(f"You notice someone here...")
                    print(f'\n{character.name}\n')
                    print_block(character.desc)
            if self.items:
                items = "", ", ".join(self.items)
                print_animated("You see some items lying around:")
                print_animated(items)
                print()

        print(f'Energy: {state["player"].energy}')