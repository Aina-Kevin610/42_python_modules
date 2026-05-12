#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 14:51:23 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 14:44:20 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seed: {quantity} packets avalaible")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seed: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} "
              f"seed: covers {quantity} square meters")
    else:
        print("Unknown unit type")
