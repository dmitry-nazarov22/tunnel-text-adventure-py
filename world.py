import json
from room import Room

def load_world():
    with open("data/world.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    rooms = {}
    for room_id, room_data in data["rooms"].items():
        rooms[room_id] = Room(
            name = room_data["name"],
            desc_full = room_data["desc_full"],
            desc_short = room_data["desc_short"],
            desc_dark = room_data["desc_dark"],
            is_locked = room_data["is_locked"],
            is_dark = room_data["is_dark"],
            is_keycard = room_data["is_keycard"],
            exits = room_data["exits"],
            items = room_data["items"]
        )
    return rooms