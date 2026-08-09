# from utilties import unzip
#
# print(unzip("Polynomial_Regression_and_Data_Transformation.zip", "."))
import numpy as np, pandas as pd

from sklearn.metrics import mean_squared_error, r2_score
import json


# todo
def unique_values_percentage(df, columns):
    """
    A function to calculate the summary of categorical columns of a dataframe
        @param: df -> DataFrame
        @param columns: list of categorical columns in the dataframe
        @returns: dictionary of summary of unique value counts and their percentages
    >>> x = pd.DataFrame({'temp':['hot','hot','cool']})
    unique_value_percentages(x,['temp'])
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


def my_custom_function1(arg1, arg2):
    """
    This function performs a specific task.

    Args:
        arg1 (type): Description of arg1.
        arg2 (type): Description of arg2.

    Returns:
        type: Description of the return value.
    """
    # Function implementation
    return arg1 + arg2


def find_path(neighbors_function, start_state, goal_test, bfs=True):
    """
        @param neighbors_function: neighbors_function(state) is a function which returns a list of legal
            neighbor states
        @param start_state: is the starting state for the search
        @param goal_test: is a function which returns True if the given state is
            a goal state for the search, and False otherwise.
        @param bfs: is a boolean (default True) that indicates whether we should run a
    bfs or dfs
        @return: a path through a graph from a given starting state to any state that
        satisfies a given goal condition (or None if no such path exists).

            A path from start_state to a state satisfying goal_test(state) as a
            tuple of states, or None if no path exists.
        Note the state representation must be hashable in order for this function
        to work.
    """
    if goal_test(start_state):
        return (start_state,)
    agenda = [(start_state,)]
    visited = {start_state}
    while agenda:
        this_path = agenda.pop(0 if bfs else -1)
        terminal_state = this_path[-1]
        for neighbor_state in neighbors_function(terminal_state):
            if neighbor_state not in visited:
                new_path = this_path + (neighbor_state,)
                if goal_test(neighbor_state):
                    return new_path
                agenda.append(new_path)
                visited.add(neighbor_state)
