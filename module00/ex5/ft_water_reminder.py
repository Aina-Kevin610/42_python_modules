#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 14:08:49 by airandri            #+#    #+#            #
#   Updated: 2026/03/31 08:40:48 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    water = int(input("Days since last watering: "))
    if water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
