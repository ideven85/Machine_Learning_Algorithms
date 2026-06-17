import numpy as np
import pandas as pd
import sys


def gini_calculation_split(data):
    pass


def main(args=None, kwargs=None):
    age_no_disease = np.array([50, 10])
    age_disease = np.array([20, 20])
    age_data = pd.DataFrame({"No_Disease": age_no_disease, "Disease": age_disease})

    print(age_data)


if __name__ == "__main__":
    args, kwargs = sys.argv, sys.argv
    main(args, kwargs)
