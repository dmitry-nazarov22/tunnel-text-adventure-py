from world import load_world, load_items, load_characters
from player import Player
from commands import handle_command
from ui import print_game_over, print_start, print_animated

def main():

    print_start()

    start_input = input('Press enter to start the game.\nEnter "hard" for hard mode.\nEnter "quit" to exit the game.\n> ')

    if  start_input != "quit":

        rooms = load_world()
        items = load_items()
        characters = load_characters(rooms)

        state = {
            "game_mode": "normal",
            "rooms": rooms,
            "items": items,
            "characters": characters,
            "current": "entrance",
            "player": Player(),
            "running": True,
            "mechanist_quest": False,
            "lost_worker_quest": False,
            "archivist_quest": False,
        }

        if start_input == "hard":
            print_animated("\nHard mode enabled.\n")
            state["game_mode"] = start_input

        rooms[state["current"]].look('full', state)

        rooms[state["current"]].been_here = "True"

        while state["running"] and state["player"].energy > 0 and state["current"] != "escape_tunnel":
            command = input("\n> ").strip()
            handle_command(command, state)

        print_game_over(state)

if __name__ == "__main__":
    main()