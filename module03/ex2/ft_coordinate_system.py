#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 15:58:34 by airandri            #+#    #+#            #
#   Updated: 2026/04/14 15:58:35 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


class InvalidArgError(Exception):
    pass


def is_invalid(pos: list) -> None:
    mess: str = "Invalid syntax"
    length: int = 0
    for _ in pos:
        length += 1
    if length != 3:
        raise InvalidArgError(mess)


def get_player_pos() -> tuple:
    mess: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        pos: list = input(mess).split(',')
        try:
            is_invalid(pos)
            for element in pos:
                float(element)
            return tuple(pos)
        except InvalidArgError as e:
            print(e)
        except ValueError:
            print(f"Error on parameter '{element}': could",
                  f"not convert string to float: {element}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos_1: tuple = get_player_pos()
    a: float = float(pos_1[0])
    b: float = float(pos_1[1])
    c: float = float(pos_1[2])
    dis: float = math.sqrt(a**2 + b**2 + c**2)
    print(f"Got a first tuple: {a, b, c}")
    print(f"It includes: X={a}, Y={b}, Z={c}")
    print(f"Distance to center: {round(dis, 4)}\n")

    print("Get a second set of coordinates")
    pos_2: tuple = get_player_pos()
    x: float = float(pos_2[0])
    y: float = float(pos_2[1])
    z: float = float(pos_2[2])
    dis_1: float = math.sqrt((a - x)**2 + (b - y)**2 + (c - z)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dis_1, 4)}")


if __name__ == "__main__":
    main()
