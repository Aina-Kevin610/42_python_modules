#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 14:17:02 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 12:04:35 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    for i in range(1, harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")
