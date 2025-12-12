from ui import print_block

class Item:
    def __init__(self, name, desc, use_msg, error_msg):
        self.name = name
        self.desc = desc
        self.use_msg = use_msg
        self.error_msg = error_msg

    def examine(self):
        print_block(self.desc)