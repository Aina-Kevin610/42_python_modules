#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 16:24:57 by airandri            #+#    #+#            #
#   Updated: 2026/04/13 16:24:58 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str) -> None:
        self.name = name


class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'"
                         f"\n.. ending tests and returning to main")


def test_watering_system() -> None:
    try:
        for plant in plants:
            water_plant(plant.name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    plants = [
        Plant("Tomato"),
        Plant("Lettuce"),
        Plant("Carrots")
    ]
    test_watering_system()

    print("\nTesting invalid plants...")
    plants = [
        Plant("Tomato"),
        Plant("lettuce"),
        Plant("Carrots")
    ]
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
