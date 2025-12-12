from ui import print_animated

def handle_command(cmd, state):
    words = cmd.split()
    if not words:
        return

    verb = words[0].lower()

    if len(words) > 1:
        obj1 = words[1].lower()
    if len(words) > 2:
        obj2 = words[2].lower()

    match verb:
        case "look":
            state["rooms"][state["current"]].look('full', state)

        case "examine":
            if len(words) >= 2:
                if obj1 in state["items"]:
                    state["items"][obj1].examine()
                else:
                    print_animated("You don't have that.")
            else:
                print_animated("Please input: examine <item>")

        case "go":
            if len(words) < 2:
                print("Go where?")
                return
            move(obj1, state)

        case "inventory":
            state["player"].show_inventory()

        case "take":
            if len(words) >= 2:
                state["player"].add_item(state, obj1, state["rooms"][state["current"]])
            else:
                print_animated("Please input: take <item>")


        case "drop":
            if len(words) >= 2:
                state["player"].drop_item(obj1, state["rooms"][state["current"]])
            else:
                print_animated("Please input: drop <item>")

        case "use":
            if len(words) >= 2:
                if state["player"].use_item(state, obj1):
                    state["player"].score += 25
            else:
                print_animated("Please input: use <item>")

        case "combine":
            if len(words) >= 3:
                state["player"].craft_item(state, obj1, obj2)
            else:
                print_animated("Please input: combine <item1> <item2>")

            print_animated("No one with that name is here.")

        case "talk":
            if len(words) >= 2:
                target_name = obj1
                current_room = state["rooms"][state["current"]]

                if not current_room.characters:
                    print_animated("There's no one here. But I was sure...")
                    return

                for npc in current_room.characters:
                    if npc.name.lower() == target_name:
                        npc.talk(state, current_room)
                        return
            else:
                print_animated("Please input: talk <character>")

        case "quit":
            print_animated("Closing the game...")
            state["running"] = False

        case _:
            print("Unknown command.")


def move(direction, state):
    room = state["rooms"][state["current"]]
    # CHECK FOR TARGET ROOM EXISTING
    if direction in room.exits and room.exits[direction]:
        target_room = state["rooms"][room.exits[direction]]
        # CHECK FOR LOCK ON DOOR
        if target_room.is_locked != 'True' and target_room.is_keycard != 'True':
            # CHECK FOR FINAL ROOM
            if target_room.is_blowable != 'True':
                # CHECK IF ROOM IS DARK
                if target_room.is_dark != 'True':
                    state["current"] = room.exits[direction]
                    # GAME MODE ENERGY CONSUMPTION
                    if state["game_mode"] != "hard":
                        state["player"].energy -= 2
                    else:
                        state["player"].energy -= 5
                    # CHECK FOR BEING IN THE ROOM BEFORE
                    if target_room.been_here == "False":
                        target_room.been_here = "True"
                        state["rooms"][state["current"]].look("full", state)
                    else:
                        state["rooms"][state["current"]].look("short", state)
                # DARK ROOM DESCRIPTION
                else:
                    state["current"] = room.exits[direction]
                    state["rooms"][state["current"]].look("dark", state)
            # FINAL ROOM LOCKED
            elif target_room.is_blowable == 'True':
                print_animated("The door is very big. I need something big to get rid of it")
        # LOCKED ROOM LOCKED
        elif target_room.is_locked == 'True':
            print_animated("The door is blocked... Maybe I'll find something that will help me.")
        # KEYCARD ROOM LOCKED
        elif target_room.is_keycard == 'True':
            print_animated("The door has a keycard lock on it... Maybe I'll find one that will open it.")

    else:
        print_animated("Can't go that way.")
