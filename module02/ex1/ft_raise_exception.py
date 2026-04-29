#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 09:04:36 by airandri            #+#    #+#            #
#   Updated: 2026/04/13 09:54:56 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class LowTemp(Exception):
    pass


class HighTemp(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    if result < 0:
        raise LowTemp(f"{result}°C is too cold for plants (min 0°C)")
    elif result > 40:
        raise HighTemp(f"{result}°C is too hot for plants (max 40°C)")
    return (result)


def test_temperature() -> None:
    try:
        value: int = input_temperature(input_data)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    except HighTemp as e:
        print("Caught input_temperature error:", e)
    except LowTemp as e:
        print("Caught input_temperature error:", e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("\n")
    input_data = "25"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    input_data = "abc"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    input_data = "100"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    input_data = "-50"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    print("All tests completed - program didn't crash!")
