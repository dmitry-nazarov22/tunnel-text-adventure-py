import json
from room import Room
from item import Item

def load_world():
    with open("data/world.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    rooms = {}
    for room_id, room_data in data["rooms"].items():
        rooms[room_id] = Room(
            name = room_data["name"],
            been_here = room_data["been_here"],
            desc_full = room_data["desc_full"],
            desc_short = room_data["desc_short"],
            desc_dark = room_data["desc_dark"],
            is_locked = room_data["is_locked"],
            is_dark = room_data["is_dark"],
            is_keycard = room_data["is_keycard"],
            is_blowable = room_data["is_blowable"],
            exits = room_data["exits"],
            items = room_data["items"]
        )
    return rooms

def load_items():
    with open("data/items.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    items = {}
    for item_id, item_data in data["items"].items():
        items[item_id] = Item(
            name = item_data["name"],
            desc = item_data["desc"],
            use_msg = item_data["use_msg"],
            error_msg = item_data["error_msg"],
        )
    return items