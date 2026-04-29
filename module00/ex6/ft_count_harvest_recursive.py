#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 14:50:44 by airandri            #+#    #+#            #
#   Updated: 2026/04/01 12:04:59 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    i = 1
    harvest = int(input("Days until harvest: "))

    def helper_function(i):
        if (i <= harvest):
            print(f"Day {i}")
        else:
            return
        helper_function(i + 1)
    helper_function(i)
    print("Harvest time!")
