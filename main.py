from world import load_world
from player import Player
from commands import handle_command
from ui import print_animated

def main():
    rooms = load_world()

    state = {
    "rooms": rooms,
    "current": "entrance",
    "player": Player(),
    "running": True
    }

    rooms[state["current"]].look('full')

    while state["running"]:
        command = input("> ").strip()
        handle_command(command, state)

    print_animated("Closing the game...")

if __name__ == "__main__":
    main()