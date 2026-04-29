#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 08:19:35 by airandri            #+#    #+#            #
#   Updated: 2026/04/14 08:19:36 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name: ", sys.argv[0])
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
    i: int = 1
    while i < len(sys.argv):
        print(f"Arguments {i}: {sys.argv[i]}")
        i += 1
    print("Total arguments: ", len(sys.argv))


if __name__ == "__main__":
    main()
