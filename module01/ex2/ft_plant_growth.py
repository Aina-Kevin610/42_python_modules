#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 21:52:24 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 07:43:06 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{round(self.height, 1)} cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age_(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant("rose", 24.2, 29)
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_()
        rose.show()
    print("Growth this week: 6cm")
