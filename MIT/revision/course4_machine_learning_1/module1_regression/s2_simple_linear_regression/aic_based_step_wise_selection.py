import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS


def stepwise_selection(X, y, direction="forward", max_features=None):
    """
    Performs stepwise feature selection using AIC.

    Args:
        X (pd.DataFrame): The input features.
        y (pd.Series): The target variable.
        direction (str, optional): 'forward' or 'backward'. Defaults to 'forward'.
        max_features (int, optional): Maximum number of features to select.
                                     Defaults to None.

    Returns:
        list: The selected feature names.
    """
    if direction == "forward":
        sfs = SFS(
            LinearRegression(),
            k_features=max_features,
            forward=True,
            floating=False,
            scoring="neg_mean_squared_error",
            cv=0,
        )
    elif direction == "backward":
        sfs = SFS(
            LinearRegression(),
            k_features=1,
            forward=False,
            floating=False,
            scoring="neg_mean_squared_error",
            cv=0,
        )
    else:
        raise ValueError("direction must be 'forward' or 'backward'")

    sfs.fit(X, y)
    return list(sfs.k_feature_names_)


# Example usage:
# Assuming you have a DataFrame 'df' with features and a target variable 'target'
# X = df.drop('target', axis=1)
# y = df['target']

# Forward selection with a maximum of 5 features
selected_features_forward = stepwise_selection(
    X, y, direction="forward", max_features=5
)
print("Selected features (forward):", selected_features_forward)

# Backward elimination
# selected_features_backward = stepwise_selection(X, y, direction='backward')
# print("Selected features (backward):", selected_features_backward)
