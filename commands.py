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

        case "quit":
            state["running"] = False

        case _:
            print("Unknown command.")


def move(direction, state):
    room = state["rooms"][state["current"]]
    if direction in room.exits and room.exits[direction]:
        if state["rooms"][room.exits[direction]].is_locked != 'True':
            state["current"] = room.exits[direction]
            state["rooms"][state["current"]].look("full")
        else:
            print("Can't go there yet. Maybe I'll find something that will help me.")
    else:
        print("Can't go that way.")
