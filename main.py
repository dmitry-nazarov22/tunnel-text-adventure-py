from world import load_world, load_items, load_characters
from player import Player
from commands import handle_command
from ui import print_animated

def main():
    rooms = load_world()
    items = load_items()
    characters = load_characters(rooms)

    state = {
    "rooms": rooms,
    "items": items,
    "characters": characters,
    "current": "entrance",
    "player": Player(),
    "running": True
    }

    rooms[state["current"]].look('full')

    rooms[state["current"]].been_here = "True"

    while state["running"] and state["player"].energy > 0:
        print(f'Energy: {state["player"].energy}\n')
        command = input("> ").strip()
        handle_command(command, state)

    print_animated("Closing the game...")

if __name__ == "__main__":
    main()