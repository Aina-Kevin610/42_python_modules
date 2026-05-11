#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 22:28:57 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 07:41:41 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: "
                  f"Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age update: {self._age} days")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}: "
                  f"Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height update: {self._height} cm")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age)

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{round(self._height, 1)} cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("\n")
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-25)
    rose.set_age(-30)
    print("\n")
    print("Current state: ", end="")
    rose.show()
