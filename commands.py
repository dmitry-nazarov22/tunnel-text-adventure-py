from ui import print_animated

def handle_command(cmd, state):
    words = cmd.split()
    if not words:
        return

    verb = words[0]

    if len(words) > 1:
        body = words[1]

    match verb:
        case "look":
            state["rooms"][state["current"]].look('short')

        case "go":
            if len(words) < 2:
                print("Go where?")
                return
            move(body, state)

        case "inventory":
            state["player"].show_inventory()

        case "take":
            state["player"].add_item(body, state["rooms"][state["current"]])

        case "use":
            state["player"].use_item(state, body)

        case "quit":
            state["running"] = False

        case _:
            print("Unknown command.")


def move(direction, state):
    room = state["rooms"][state["current"]]
    target_room = state["rooms"][room.exits[direction]]

    if direction in room.exits and room.exits[direction]:
        if target_room.is_locked != 'True':
            state["current"] = room.exits[direction]
            state["rooms"][state["current"]].look("full")
        else:
            print_animated("Can't go there yet. Maybe I'll find something that will help me.")
    else:
        print_animated("Can't go that way.")
