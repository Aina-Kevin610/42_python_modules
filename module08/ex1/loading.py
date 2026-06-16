#!/usr/bin/env python3

import importlib


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    pkg = {
        "matplotlib" : "Visualization read", 
        "pandas" :  "Data manipulation ready",
        "numpy" : "Numerical computation ready",
    }

    try:
        for module, message in pkg.items():
            mod = importlib.import_module(module)
            print(f"[OK] {module} ({mod.__version__}) - {message}")

        print("\nAnalyzing Matrix data...")
        np = importlib.import_module("numpy")
        matrix = np.random.randn(1000, 2)

        print(f"Processing {len(matrix)} data points...")
        pd = importlib.import_module("pandas")
        matrix_data = pd.DataFrame(matrix, columns=["x axe", "y axe"])
        print(matrix_data)

        plt = importlib.import_module("matplotlib.pyplot")
        plt.plot(matrix)
        print("Generating visualization...")
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except ModuleNotFoundError:
        print(f"[KO] ({module}) - import error")
    except Exception:
        print("Error")
