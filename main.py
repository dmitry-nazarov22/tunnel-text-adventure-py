from world import load_world, load_items
from player import Player
from commands import handle_command
from ui import print_animated

def main():
    rooms = load_world()
    items = load_items()

    state = {
    "rooms": rooms,
    "items": items,
    "current": "entrance",
    "player": Player(),
    "running": True
    }

    rooms[state["current"]].look('full')

    rooms[state["current"]].been_here = "True"

    while state["running"]:
        command = input("> ").strip()
        handle_command(command, state)

    print_animated("Closing the game...")

if __name__ == "__main__":
    main()