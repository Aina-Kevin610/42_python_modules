#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/01 10:25:41 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 15:25:08 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = height

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 2.1

    def age_(self) -> None:
        self._age += 1

'''
class neste:
    def __init__(self):
        pass
'''<F11>


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str, blooming: bool):
        super().__init__(name, height, age)
        self._color = color
        self._blooming = blooming

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self) -> None:
        if self._blooming:
            print(f"{self._name.capitalize()} is blooming beautiffully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

    def produce_shade(self) -> None:
        if self._height >= 0:
            print(f"Tree {self._name.capitalize()} now produces a shade of "
                  f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        else:
            print("Can't produce shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 nutri_val: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._nutri_val = nutri_val
        self._harvest_season = harvest_season

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}\n"
              f" Nutritional Value: {self._nutri_val}")

    def grow_and_age(self, evo: int) -> None:
        i = 0
        while i < evo:
            super().grow()
            super().age_()
            self._nutri_val += 1
            i += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n=== Flower")
    rose = Flower("rose", 15.0, 10, "red", False)
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose._blooming = True
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, 0, "april")
    tomato.show()
    print("[make tomato grow and age for 20  days]")
    evo = 20
    tomato.grow_and_age(evo)
    tomato.show()
