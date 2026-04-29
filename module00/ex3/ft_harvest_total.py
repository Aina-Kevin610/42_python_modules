#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 12:32:59 by airandri            #+#    #+#            #
#   Updated: 2026/03/31 08:41:06 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("Day 2 harvest: "))
    d3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {d1 + d2 + d3}")
