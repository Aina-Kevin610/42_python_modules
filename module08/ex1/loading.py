#!/usr/bin/env python3

import importlib
import sys


def check_dependencies(pkg: dict[str, str]) -> bool:
    module = ""
    try:
        for module, message in pkg.items():
            mod = importlib.import_module(module)
            print(f"[OK] {module} ({mod.__version__}) - {message}")
        return False
    except ModuleNotFoundError:
        print(f"[KO] ({module}) - import error")
        return True


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    pkg = {
        "matplotlib": "Visualization read",
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }
    missing = False
    try:
        missing = check_dependencies(pkg)
        if missing:
            raise ValueError()
        print("\nAnalyzing Matrix data...")
        np = importlib.import_module("numpy")
        matrix = np.random.randn(1000, 2)

        print(f"Processing {len(matrix)} data points...")
        pd = importlib.import_module("pandas")
        matrix_data = pd.DataFrame(matrix, columns=["x axe", "y axe"])

        plt = importlib.import_module("matplotlib.pyplot")
        plt.plot(matrix_data)
        print("Generating visualization...")
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception:
        pass

    if missing:
        print("\n[ERROR] Missing dependencies detected.")
        print("To load programs, use one of the following commands:")
        print("  pip install -r requirements.txt")
        print("  OR")
        print("  poetry install")
        sys.exit(1)
