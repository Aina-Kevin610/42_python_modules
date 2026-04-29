#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 09:56:21 by airandri            #+#    #+#            #
#   Updated: 2026/04/13 10:40:55 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        print("this is str" + 1)
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    try:
        garden_operations(operation_number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    while operation_number < 5:
        print(f"Testing operation {operation_number}...")
        test_error_types()
        operation_number += 1
    print("\nAll error types tested successfully!")
