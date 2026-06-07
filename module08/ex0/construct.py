#!/usr/bin/env python3

import os


try:
    import flask
        
except ModuleNotFoundError as e:
    print("Curent Python: ", os.fspath("/usr/bin/python3.11"))

    print ("Virtual Environement: None detected")
    print("WARNING: You're in a global environement!")
    print("The machine can see everything you install.")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\activate # On Windows")
    print("Then run this program again.")