#!/usr/bin/env python3

try:
    import importlib
    import requests as rq
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except Exception as e:
    print("Error - ", e)


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    pkg = {
        "matplotlib" : "Visualization read", 
        "pandas" :  "Data manipulation ready",
        "numpy" : "Numerical computation ready",
        "requests" : "Network access ready",
    }
    try:
        for module, message in pkg.items():
            mod = importlib.import_module(module)
            print(f"[OK] {module} ({mod.__version__}) - {message}")
    except ModuleNotFoundError as e:
        print(f"[KO] {mod}) - import error")

    print("\nAnalyzing Matrix data...")
    data = np.random.randn(1000, 2)
    data = pd.DataFrame(data)
    print(data)
    plt.plot(data)
    plt.show()


    