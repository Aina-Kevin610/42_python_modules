#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/01 17:13:43 by airandri            #+#    #+#            #
#   Updated: 2026/04/13 09:54:11 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    try:
        value: int = input_temperature(input_data)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("\n")
    input_data = "25"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    input_data = "abc"
    print(f"Input data is '{input_data}'")
    test_temperature()
    print("\n")
    print("All tests completed - program didn't crash!")
