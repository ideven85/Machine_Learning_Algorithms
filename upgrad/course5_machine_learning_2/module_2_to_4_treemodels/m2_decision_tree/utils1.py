# from utilties import unzip
#
# print(unzip("Polynomial_Regression_and_Data_Transformation.zip", "."))
import numpy as np, pandas as pd

from sklearn.metrics import mean_squared_error, r2_score


def unique_values_percentage3(df, columns):
    """
    adfsfsd
    """
    results = {}
    for column in columns:

        # Count unique values and calculate percentages
        value_counts = df[column].value_counts()
        percentages = df[column].value_counts(normalize=True) * 100

        # Combine counts and percentages into a DataFrame
        unique_summary = pd.DataFrame(
            {"Count": value_counts, "Percentage (%)": percentages}
        )

        # Add the result to the dictionary
        results[column] = unique_summary
    print(results)
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
    return accuracy, rss, mse, rmse
