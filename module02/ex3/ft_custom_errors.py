#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 10:41:19 by airandri            #+#    #+#            #
#   Updated: 2026/04/13 11:41:16 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water error") -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, temp: int, water: int = 0) -> None:
        self.name = name
        self.water = water
        self.temp = temp

    def state_checker(self) -> None:
        if self.temp <= 0 or self.temp >= 40:
            raise PlantError(f"The {self.name} plant is wilting!")

    def water_checker(self) -> None:
        if not self.water:
            raise WaterError("Not enough water in the tank!")


def error_handling(plant: Plant) -> None:
    try:
        print("Testing PlantError...")
        plant.state_checker()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\n")
    try:
        print("Testing WaterError...")
        plant.water_checker()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\n")
    try:
        print("Testing catching all garden errors...")
        plant.state_checker()
    except PlantError as e:
        print(f"Caught GardenError: {e}")
    try:
        plant.water_checker()
    except WaterError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    rose = Plant("rose", 56)
    error_handling(rose)
    print("\nAll custom error types work correctly!")
