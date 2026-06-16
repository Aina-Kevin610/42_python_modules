#!/usr/bin/env python3

import importlib


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

        print("\nAnalyzing Matrix data...")
        np = importlib.import_module("numpy")
        data = np.random.randn(1000, 1)

        pd = importlib.import_module("pandas")
        data = pd.DataFrame(data)
        print(data)

        plt = importlib.import_module("matplotlib.pyplot")
        plt.plot(data)
        plt.show()
    except ModuleNotFoundError:
        print(f"[KO] ({module}) - import error")
