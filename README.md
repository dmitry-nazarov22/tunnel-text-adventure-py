# Tunnel Text Adventure

An atmospheric, data-driven text-adventure built in Python. You wake up at a collapsed subway entrance in an abandoned underground metro network built for evacuation — but something went wrong. The stations were sealed, personnel disappeared or remained transformed into something no longer quite human. You have one resource: energy. Each movement drains it. Your goal is to explore, help survivors, collect and craft items, and find a way out.

**Quick Start**

- **Run:** From the project root run:

```bash
python3 main.py
```

- **Options at start:** Press Enter to begin, type `hard` to enable hard mode, or `quit` to exit.

**Project Structure**

- **`main.py`**: Game entry point and main loop. Loads world, items, characters, and handles the command loop.
- **`world.py`**: Loads `map.txt` and JSON files from `data/` to build `Room`, `Item`, and `Character` objects.
- **`player.py`**: The `Player` class with attributes like `energy` and `inventory`.
- **`room.py`**: `Room` class and room-related behaviors (descriptions, `look()` method).
- **`item.py`**: `Item` class and item logic (properties, combination behavior).
- **`character.py`**: NPC definitions and dialogue/interaction behaviors.
- **`commands.py`**: Command parsing and execution (`handle_command(command, state)`).
- **`ui.py`**: Terminal output helpers such as `print_start`, `print_animated`, and `print_game_over`.
- **`map.txt`** and **`data/`**: Game data files. `data/` contains `world.json`, `items.json`, `characters.json`, and `help.txt`.

**Game Atmosphere (Story Intro — translated and expanded)**
The game's world is set in a future-era underground metro network that was built to evacuate government leadership. After an accident, parts of the caretaking staff disappeared while others remained in the tunnels — but not in human form anymore. They hear but cannot see. It is unclear whether they are alive; they simply continue their duty to the end. Stations were sealed and isolated, documents destroyed, but scattered notes, logs, and torn records remain. You awaken unconscious at a collapsed entrance — dazed, you now find yourself at the threshold.

The game greets the player with this scene and immediately shows the first room description and an energy counter starting at 100. Energy is the player's resource and decreases each time you move between locations. The implication is clear — you must escape.

As you explore, you will find items that help you survive and flee the hostile environment. Room descriptions hint that you are not alone, but nothing is visible... as if someone watches from the dark.

**Gameplay Summary**

- **Commands:** The game supports a set of text commands to interact with the world (see the full command list below).
- **Items:** There are 12 discoverable items placed in the world, plus three craftable items (assembled from other items), two items attainable via trade, and one item given by an NPC after helping them.
- **Quests & Characters:** Multiple NPCs offer interactions and quests. Helping characters may yield items, unlock dialogue, or influence endings.

**Commands**
The following commands are available in-game (type `help` to view this list):

- `look` – show full room description
- `examine <item>` – show item description
- `go <direction>` – move to an adjacent room (`north`, `east`, `south`, `west`)
- `inventory` – show all items in your inventory
- `take <item>` – take an item from the room into your inventory
- `drop <item>` – drop an item from your inventory into the current room
- `give <character> <item>` – give an item to a character (used for quests)
- `use <item>` – use an item's ability (some items are consumable)
- `combine <item1> <item2>` – combine two items (crafting mechanic)
- `talk <character>` – talk to a character (repeat to cycle dialogue)
- `trade <character>` – show items a character will trade
- `trade <character> <item>` – offer an item to trade with a character
- `help` – display help instructions (shows the command list)
- `quit` – quit the game

**Goals and Endings**

- There are five possible endings.
- You can lose by letting your energy drop to zero.
- You can also lose by detonating yourself with the C4 you craft.
- There are three ways to win:
  - Minimal win: Gather enough points and escape.
  - Neutral win: Help the Mechanist NPC and reach a score threshold.
  - Best win: Assist all NPCs and achieve the highest score.

Hint: One critical puzzle requires crafting a C4 charge to blow open a final large door.

**Hard Mode**

- Enable by typing `hard` at the start screen. Hard mode makes movement cost more energy, increasing the difficulty. It does not grant additional endings or rewards — it just demands tighter decision-making.

**Game State & Data-Driven Design**

- The game uses a `state` dictionary to hold runtime state: `game_mode`, `rooms`, `items`, `characters`, `current` (current room id), `player` (Player instance), `running` (loop flag), and quest booleans (e.g. `mechanist_quest`).
- World layout, items, and characters are defined in the `data/` JSON files. Changing these files alters the game's content without touching code.
