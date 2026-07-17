#
# print(unzip("Polynomial_Regression_and_Data_Transformation.zip", "."))
import numpy as np, pandas as pd

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

from IPython.display import display


import random


def data_loader(data, batch_size=32, shuffle=False):
    """
    mimics functionality of torch DataLoader
    """
    if batch_size <= 0:
        raise ValueError("batch_size must be 1 or greater.")

    dataset = data.clone() if shuffle else data

    if shuffle:
        random.shuffle(dataset)

    for i in range(0, len(dataset), batch_size):
        yield dataset[i : i + batch_size]


def removing_statistical_outliers(df, columns, quantile=None):
    """
    A function that removes outliers in the dataframe
    @param: df -> DataFrame
    @param: columns-> Specified columns
    @param: quantile-> if not specified 75% is taken by default
    @returns: new dataframe with outliers removed
    """
    if not quantile:
        quantile = 0.75
    for col in columns:
        Q1 = df[col].quantile(quantile)
        Q3 = df[col].quantile(1 - quantile)
        IQR = Q3 - Q1
        # print(f"Original Shape: {grouped_df.shape}")
        df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]
        # print(f"After Removing Outliers: {grouped_df.shape}")
    return df


def unique_values_percentage(df, columns):
    """
    A function to calculate the summary of categorical columns of a dataframe
        @param: df -> DataFrame
        @param: columns: list of categorical columns in the dataframe
        @returns: Dataframe of summary of unique value counts and their percentages
    >>> x = pd.DataFrame({'temp':['hot','hot','cool']}).values

    """
    results = pd.DataFrame()
    for column in columns:
        # Count unique values and calculate percentages
        value_counts = df[column].value_counts()
        percentages = df[column].value_counts(normalize=True) * 100

        # Combine counts and percentages into a DataFrame
        unique_summary = pd.DataFrame(
            {"column": column, "Count": value_counts, "Percentage (%)": percentages}
        ).sort_values(by="Count", ascending=False)

        # Add the result to the dictionary
        # display(pd.concat([results,unique_summary]))
        results = pd.concat([results, unique_summary])

    return results


def goodness_of_fit(y_true, predictions):
    """
    @param: y_true: actual
    @param prediction: predicted
    @return:  a tuple of r2_score, sum of squared residuals,mean squared error,root mean squared error
    """
    accuracy = r2_score(y_true, predictions)
    # RSS
    rss = np.sum(np.square(y_true - predictions))
    # MSE
    mse = mean_squared_error(y_true=y_true, y_pred=predictions)
    # RMSE
    rmse = np.sqrt(mse)
    out = [("Accuracy:", accuracy), ("RSS:", rss), ("MSE:", mse), ("RMSE:", rmse)]

    return out


def memo(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


def variance_inflation(X_train, selected_features):
    vif = pd.DataFrame()
    vif["Features"] = X_train[selected_features].columns
    vif["VIF"] = [
        variance_inflation_factor(X_train[selected_features].values, i)
        for i in range(X_train[selected_features].shape[1])
    ]
    vif["VIF"] = round(vif["VIF"], 2)
    vif = vif.sort_values(by="VIF", ascending=False)
    return vif


def display_info(df: pd.DataFrame):
    display(df)
    print("\n\n")
    display(pd.DataFrame(df.info()))


def func_train_test_val_split(X, y):
    """
    splits into train,test,val
    @return:  X_train,y_train,X_val,y_val,X_test,y_test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=42, test_size=0.3, stratify=y
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.1, random_state=42
    )
    return X_train, y_train, X_val, y_val, X_test, y_test


from typing import List, Any
import dataclasses


@dataclasses.dataclass
class TrainResult:
    # 1. Required Parameters (Must be passed at instantiation)
    num_epochs: int
    lr: float
    model_state: dict = dataclasses.field(default_factory=dict)

    # 2. Optional Selected Parameters (Automatically initialized if omitted)
    train_loss: List[float] = dataclasses.field(default_factory=list)
    train_acc: List[float] = dataclasses.field(default_factory=list)
    val_loss: List[float] = dataclasses.field(default_factory=list)
    val_acc: List[float] = dataclasses.field(default_factory=list)

    # Simple scalar defaults
    test_loss: float = 0.0
    test_acc: float = 0.0
