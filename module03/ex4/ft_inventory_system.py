#!/usr/bin/env python3

import sys


class InvalidParams(Exception):
    pass


def total(inventory: list) -> int:
    sum = 0
    for item in inventory:
        item = int(item)
        sum += item
    return (sum)


def percentage(unit: int, total: int) -> float:
    return (round((unit * 100) / total, 2))


def maximum(inventory: dict) -> tuple:
    max_key = list(inventory.keys())[0]
    max_value = inventory[max_key]
    for key in inventory:
        if inventory[key] > max_value:
            max_value = inventory[key]
            max_key = key
    return (max_value, max_key)


def minimum(inventory: dict) -> tuple:
    max_key = list(inventory.keys())[0]
    max_value = inventory[max_key]
    for key in inventory:
        if inventory[key] < max_value:
            max_value = inventory[key]
            max_key = key
    return (max_value, max_key)


def uptade_inventory(inventory: dict, new_key: str,  new_value: int) -> dict:
    inventory.update({new_key: new_value})
    return inventory


def main() -> None:
    try:
        if len(sys.argv) == 1:
            raise InvalidParams("No argument found!")
        items = list(item for item in sys.argv if item != sys.argv[0])
        item_dict = dict()
        for item in items:
            try:
                unit = item.split(":")
                if len(unit) != 2:
                    raise InvalidParams(f" invalid parameter '{unit[0]}'")
                int(unit[1])
                if unit[0] in item_dict:
                    print(f"Redundant item '{unit[0]}' - discarding")
                    pass
                else:
                    item_dict[unit[0]] = int(unit[1])
            except InvalidParams as e:
                print(f"Error - {e}")
            except ValueError as e:
                print(f"Quantity error for '{unit[0]}':{e}")
        print(f"Got inventory: {item_dict}")
        inventory_key = list(item_dict.keys())
        inventory_value = list(item_dict.values())
        totals = total(inventory_value)
        print(f"Item list: {inventory_key}")
        print(f"Total qantity of the {len(inventory_key)} items: {totals}")
        i = 0
        while i < len(inventory_key):
            print(f"Item {inventory_key[i]} "
                  f"represents {percentage(int(inventory_value[i]), totals)}%")
            i += 1
        max_value = maximum(item_dict)
        min_value = minimum(item_dict)
        print(f"Item most abundant: {max_value[1]} "
              f"with quantity {max_value[0]}")
        print(f"Item least abundant: {min_value[1]} "
              f"with quantity {min_value[0]}")
        item_dict = uptade_inventory(item_dict, "magic_item", 1)
        print("Updated inventory: ", item_dict)
    except InvalidParams as e:
        print("Error - ", e)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    try:
        main()
    except Exception:
        print("Unknown error happened!")
