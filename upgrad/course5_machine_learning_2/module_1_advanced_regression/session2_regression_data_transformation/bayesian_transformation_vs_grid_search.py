import time

from bayes_opt import BayesianOptimization
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X, y = data.data, data.target


# todo
# Define the function to optimize
def rf_cv(n_estimators, max_depth, min_samples_split):
    model = RandomForestClassifier(
        n_estimators=int(n_estimators),
        max_depth=int(max_depth),
        min_samples_split=int(min_samples_split),
        random_state=42,
    )
    return cross_val_score(model, X, y, cv=3).mean()


def bayesian_maximizer():
    # Set up Bayesian Optimization
    optimizer = BayesianOptimization(
        f=rf_cv,
        pbounds={
            "n_estimators": (50, 200),
            "max_depth": (5, 20),
            "min_samples_split": (2, 10),
        },
        random_state=42,
    )
    optimizer.maximize(init_points=5, n_iter=25)

    # Output the best parameters
    print(optimizer.max)


def grid_search_cv():
    """
    In this example, we load the Iris dataset and split it into training and testing sets.
    We define a RandomForestClassifier and specify a grid of hyperparameters to search over,
    including the number of trees (n_estimators), maximum depth of the trees (max_depth),
     minimum number of samples required to split a node (min_samples_split), minimum number of samples required at a leaf node (min_samples_leaf)
     , and the criterion for splitting (criterion).

    We use GridSearchCV to perform an exhaustive search over the specified parameter grid, using 4-fold cross-validation (cv=4).
    The best hyperparameters and the corresponding model are then extracted and evaluated on the test set.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Instantiate a Random Forest classifier
    rf = RandomForestClassifier(random_state=42)

    # Define the parameter grid to search
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "criterion": ["gini", "entropy"],
    }

    # Instantiate the GridSearchCV object
    grid_search = GridSearchCV(
        estimator=rf, param_grid=param_grid, cv=4, n_jobs=-1, verbose=2
    )

    # Fit the grid search to the data
    grid_search.fit(X_train, y_train)

    # Get the best parameters and the best estimator
    best_params = grid_search.best_params_
    best_rf = grid_search.best_estimator_

    # Print the best parameters
    print("Best Parameters:", best_params)

    # Evaluate the best model on the test set
    test_score = best_rf.score(X_test, y_test)
    print("Test Set Score:", test_score)


# Run optimization
def main():
    s1 = time.perf_counter_ns()
    bayesian_maximizer()
    s2 = time.perf_counter_ns()
    grid_search_cv()
    s3 = time.perf_counter_ns()
    x = (s2 - s1) / (s3 - s2)
    print(f"Bayesian optimizer took: {s2-s1} time")
    print(f"Grid Search CV took: {s3 - s2} time")
    print(f"Ratio: {x}")


if __name__ == "__main__":
    main()
