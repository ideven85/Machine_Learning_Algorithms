import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import accuracy_score, make_scorer

# --- 0. Our Base Neural Network Code (from last time) ---
# (No changes here, this is our "engine")
# Gemini Code
# todo


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return np.where(x > 0, 1, 0)


ACTIVATION_FUNCTIONS = {
    "sigmoid": (sigmoid, sigmoid_derivative),
    "relu": (relu, relu_derivative),
}


class SimpleNeuralNetwork:
    """Our internal 'from-scratch' neural network."""

    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        learning_rate=0.1,
        hidden_activation="relu",
    ):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        self.hidden_activation, self.hidden_activation_derivative = (
            ACTIVATION_FUNCTIONS[hidden_activation]
        )
        self.output_activation = sigmoid
        self.output_activation_derivative = sigmoid_derivative

        # Initialize weights and biases
        self.W_ih = np.random.randn(self.input_size, self.hidden_size) * 0.01
        self.b_h = np.zeros((1, self.hidden_size))
        self.W_ho = np.random.randn(self.hidden_size, self.output_size) * 0.01
        self.b_o = np.zeros((1, self.output_size))

    def forward(self, X):
        self.hidden_layer_input = np.dot(X, self.W_ih) + self.b_h
        self.hidden_layer_output = self.hidden_activation(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.W_ho) + self.b_o
        predictions = self.output_activation(self.output_layer_input)
        return predictions

    def backward(self, X, y, predictions):
        output_error = predictions - y
        output_delta = output_error * self.output_activation_derivative(
            self.output_layer_input
        )
        hidden_error = np.dot(output_delta, self.W_ho.T)
        hidden_delta = hidden_error * self.hidden_activation_derivative(
            self.hidden_layer_input
        )
        self.dW_ho = np.dot(self.hidden_layer_output.T, output_delta)
        self.db_o = np.sum(output_delta, axis=0, keepdims=True)
        self.dW_ih = np.dot(X.T, hidden_delta)
        self.db_h = np.sum(hidden_delta, axis=0, keepdims=True)

    def update_weights(self):
        self.W_ho -= self.learning_rate * self.dW_ho
        self.b_o -= self.learning_rate * self.db_o
        self.W_ih -= self.learning_rate * self.dW_ih
        self.b_h -= self.learning_rate * self.db_h

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            predictions = self.forward(X)
            self.backward(X, y, predictions)
            self.update_weights()
            # Optional: Add loss calculation if needed for debugging
            # if (epoch + 1) % 1000 == 0:
            #    loss = np.mean(np.square(y - predictions))
            #    print(f"Epoch {epoch + 1}, Loss: {loss:.6f}")


# --- 1. The Sklearn Wrapper Class (NEW CODE) ---
# This class "translates" our NN into an sklearn-compatible model


class NNWrapper(BaseEstimator, ClassifierMixin):
    """
    A scikit-learn compatible wrapper for our SimpleNeuralNetwork.

    This allows us to use tools like GridSearchCV.
    """

    # The __init__ MUST list all hyperparameters we want to tune
    # as arguments with default values.
    def __init__(
        self,
        hidden_size=4,
        learning_rate=0.1,
        epochs=10000,
        hidden_activation="relu",
    ):
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.hidden_activation = hidden_activation

        # This will hold our trained model
        self.model_ = None

    def fit(self, X, y):
        """
        Trains the model. This is called by GridSearchCV.
        """
        # Ensure y is a 2D-array
        if y.ndim == 1:
            y = y.reshape(-1, 1)

        input_size = X.shape[1]
        output_size = y.shape[1]

        # 1. Create our actual NN instance
        self.model_ = SimpleNeuralNetwork(
            input_size=input_size,
            hidden_size=self.hidden_size,
            output_size=output_size,
            learning_rate=self.learning_rate,
            hidden_activation=self.hidden_activation,
        )

        # 2. Train it
        self.model_.train(X, y, epochs=self.epochs)

        # 3. Store the learned classes (required by ClassifierMixin)
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        """
        Makes predictions. This is called by GridSearchCV to score the model.
        """
        if self.model_ is None:
            raise ValueError("Model has not been trained yet. Call .fit() first.")

        raw_predictions = self.model_.forward(X)

        # Return rounded classes (0 or 1)
        return np.round(raw_predictions)

    def predict_proba(self, X):
        """
        Returns the raw probabilities (optional but good practice).
        """
        if self.model_ is None:
            raise ValueError("Model has not been trained yet. Call .fit() first.")

        # Return the raw sigmoid output
        return self.model_.forward(X)

    # get_params and set_params are required by BaseEstimator
    # for GridSearchCV to work.

    def get_params(self, deep=True):
        # Returns a dict of the hyperparameters
        return {
            "hidden_size": self.hidden_size,
            "learning_rate": self.learning_rate,
            "epochs": self.epochs,
            "hidden_activation": self.hidden_activation,
        }

    def set_params(self, **parameters):
        # Sets the hyperparameters
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self


# --- 2. Using GridSearchCV (NEW CODE) ---


def main():
    # Define the XOR dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])  # GridSearchCV works well with 1D y

    print("--- Starting GridSearchCV for SimpleNeuralNetwork ---")

    # 1. Define the "grid" of hyperparameters to test
    param_grid = {
        "hidden_size": [3, 4, 5],
        "learning_rate": [0.1, 0.05, 0.01],
        "epochs": [10000, 20000],
        "hidden_activation": ["relu", "sigmoid"],
    }

    # This will test 3 * 3 * 2 * 2 = 36 different combinations

    # 2. Create an instance of our wrapper
    wrapped_nn = NNWrapper()

    # 3. Set up GridSearchCV
    # 'cv=3' means 3-fold cross-validation
    # 'scoring='accuracy'' will use accuracy to find the best model
    grid_search = GridSearchCV(
        estimator=wrapped_nn,
        param_grid=param_grid,
        cv=3,
        scoring="accuracy",
        verbose=1,  # Shows progress
    )

    # 4. Run the grid search!
    # This will take some time as it's training 36 * 3 = 108 models
    grid_search.fit(X, y)

    # 5. Print the results
    print("\n--- GridSearchCV Complete ---")
    print(f"Best parameters found: {grid_search.best_params_}")
    print(f"Best cross-validation accuracy: {grid_search.best_score_ * 100:.2f}%")

    # You can now access the best, retrained model
    best_model = grid_search.best_estimator_

    # Test it
    predictions = best_model.predict(X)
    print("\n--- Predictions from Best Model ---")
    print(f"Input (X): {X.T[0]}")
    print(f"Input (X): {X.T[1]}")
    print(f"True (y): {y}")
    print(f"Predicted: {predictions.T.flatten()}")


if __name__ == "__main__":
    main()
