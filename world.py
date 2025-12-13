import json
from room import Room
from item import Item
from character import Character

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
            items = room_data["items"],
            characters = room_data["characters"],
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

def load_characters(rooms):
    with open("data/characters.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    characters = {}
    for character_id, character_data in data["characters"].items():
        characters[character_id] = Character(
            id = character_data["id"],
            name = character_data["name"],
            desc = character_data["desc"],
            location = character_data["location"],
            msg1 = character_data["msg1"],
            msg2 = character_data["msg2"],
            msg3 = character_data["msg3"],
            task_msg = character_data["task_msg"],
            items = character_data["items"],
            task_item = character_data["task_item"],
            trade_offer = character_data["trade_offer"],
            trade_cost = character_data["trade_cost"]
        )
        current_character = characters[character_id]
        rooms[current_character.location].characters.append(current_character)
    return characters