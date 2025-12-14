from ui import print_animated, print_block

class Character:
    def __init__(self, id, name, desc, location, msg1, msg2, msg3, task_msg, items, task_item, trade_offer, trade_cost):
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
        self.trade_offer = trade_offer
        self.trade_cost = trade_cost

        self.talk_counter = 0

    def talk(self, state, room):
        print("\n" + self.name)

        if self.task_item in self.items:
            print_animated(self.task_msg)
            if len(self.trade_offer) <= 0 and len(self.trade_cost) <= 0:
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

    def trade_list(self):
        if len(self.trade_offer) > 0 and len(self.trade_cost) > 0:
            print_animated("We could trade the following:")
            for i in range(len(self.trade_offer)):
                print_animated(f'{self.trade_offer[i]} for {self.trade_cost[i]}')

            print_animated("\nTo trade enter:\ntrade <character> <item>")
        else:
            print_animated("I have nothing to trade...")

    def trade_item(self, state, item):
        if len(self.trade_offer) > 0 and len(self.trade_cost) > 0:
            if item in self.trade_cost:

                count = 0
                for place in self.trade_cost:
                    if item == place:
                        break
                    else:
                        count += 1

                state["player"].score += 100
                print_animated("Thank you. It's always nice to make a good deal.")
                print_animated(f'{self.trade_offer[count]} added to your inventory.')
                state["player"].inventory.append(self.trade_offer[count])
                state["player"].inventory.remove(self.trade_cost[count])
                self.trade_offer.remove(self.trade_offer[count])
                self.trade_cost.remove(self.trade_cost[count])

            else:
                print_animated("I don't need that.\n To see trade list enter: trade <character>")
        else:
            print_animated("I have nothing to trade...")
