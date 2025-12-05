from ui import print_animated

def handle_command(cmd, state):
    words = cmd.split()
    if not words:
        return

    verb = words[0].lower()

    if len(words) > 1:
        body1 = words[1].lower()
    if len(words) > 2:
        body2 = words[2].lower()

    match verb:
        case "look":
            state["rooms"][state["current"]].look('short')

        case "go":
            if len(words) < 2:
                print("Go where?")
                return
            move(body1, state)

        case "inventory":
            state["player"].show_inventory()

        case "take":
            state["player"].add_item(body1, state["rooms"][state["current"]])

        case "drop":
            state["player"].drop_item(body1, state["rooms"][state["current"]])

        case "use":
            state["player"].use_item(state, body1)

        case "combine":
            state["player"].craft_item(body1, body2)

        case "quit":
            state["running"] = False

        case _:
            print("Unknown command.")


def move(direction, state):
    room = state["rooms"][state["current"]]

    if direction in room.exits and room.exits[direction]:
        target_room = state["rooms"][room.exits[direction]]

        if target_room.is_locked != 'True' and target_room.is_keycard != 'True':

            if target_room.is_dark != 'True':
                state["current"] = room.exits[direction]
                if target_room.been_here == "False":
                    target_room.been_here = "True"
                    state["rooms"][state["current"]].look("full")
                else:
                    state["rooms"][state["current"]].look("short")
            else:
                state["current"] = room.exits[direction]
                state["rooms"][state["current"]].look("dark")

        elif target_room.is_locked == 'True':
            print_animated("The door is blocked... Maybe I'll find something that will help me.")
        elif target_room.is_keycard == 'True':
            print_animated("The door has a keycard lock on it... Maybe I'll find one that will open it.")

    else:
        print_animated("Can't go that way.")
