import numpy as np
import matplotlib.pyplot as plt

# --- 1. Activation Functions ---
# We group these so they can be easily looked up
# todo make a full neural network yourself


def sigmoid(x):
    """Sigmoid activation function. Outputs between 0 and 1."""
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """Derivative of the sigmoid function."""
    s = sigmoid(x)
    return s * (1 - s)


def relu(x):
    """Rectified Linear Unit (ReLU) activation function. Outputs 0 or positive."""
    return np.maximum(0, x)


def relu_derivative(x):
    """Derivative of the ReLU function."""
    return np.where(x > 0, 1, 0)


def tan_h(x):
    h = np.exp(x)
    numerator = (h - 1 / h) / (h + 1 / h)


# This "factory" dictionary is a clean coding practice.
# It maps a string name to the actual functions.
ACTIVATION_FUNCTIONS = {
    "sigmoid": (sigmoid, sigmoid_derivative),
    "relu": (relu, relu_derivative),
}


# --- 2. Neural Network Class ---
class SimpleNeuralNetwork:
    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        learning_rate=0.1,
        hidden_activation="relu",
    ):
        """
        Initializes the neural network.

        Args:
            input_size (int): Number of input features.
            hidden_size (int): Number of neurons in the hidden layer.
            output_size (int): Number of neurons in the output layer.
            learning_rate (float): The step size for gradient descent.
            hidden_activation (str): "relu" or "sigmoid" for the hidden layer.
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # --- Clean Activation Assignment ---
        if hidden_activation not in ACTIVATION_FUNCTIONS:
            raise ValueError(f"Unsupported activation: {hidden_activation}")

        # Set the hidden layer activation functions
        self.hidden_activation, self.hidden_activation_derivative = (
            ACTIVATION_FUNCTIONS[hidden_activation]
        )

        # The output layer is hard-coded to sigmoid for binary classification
        self.output_activation = sigmoid
        self.output_activation_derivative = sigmoid_derivative
        # ------------------------------------

        # Initialize weights and biases
        self.W_ih = np.random.randn(self.input_size, self.hidden_size) * 0.01
        self.b_h = np.zeros((1, self.hidden_size))
        self.W_ho = np.random.randn(self.hidden_size, self.output_size) * 0.01
        self.b_o = np.zeros((1, self.output_size))

        # Cached values for backpropagation
        self.hidden_layer_input = None
        self.hidden_layer_output = None
        self.output_layer_input = None

        self.counter = 0

    def forward(self, X):
        """Performs the forward pass."""
        self.counter += 1

        # Input to hidden layer
        self.hidden_layer_input = np.dot(X, self.W_ih) + self.b_h
        self.hidden_layer_output = self.hidden_activation(self.hidden_layer_input)

        # Hidden to output layer
        self.output_layer_input = np.dot(self.hidden_layer_output, self.W_ho) + self.b_o
        predictions = self.output_activation(self.output_layer_input)

        return predictions

    def backward(self, X, y, predictions):
        """Performs the backward pass (backpropagation)."""

        # --- Output Layer Gradients ---
        # Error: how far off was the prediction?
        output_error = predictions - y  # Note: (pred - true) or (true - pred) works
        # as long as you are consistent. (pred - true)
        # pairs perfectly with the -= update rule.

        # Delta: error weighted by the gradient of the output activation
        output_delta = output_error * self.output_activation_derivative(
            self.output_layer_input
        )

        # --- Hidden Layer Gradients ---
        # Error: how much did the hidden layer contribute to the output error?
        # (Propagate error backward through output weights)
        hidden_error = np.dot(output_delta, self.W_ho.T)

        # Delta: hidden error weighted by the gradient of the hidden activation
        hidden_delta = hidden_error * self.hidden_activation_derivative(
            self.hidden_layer_input
        )

        # --- Calculate Gradients for Weights and Biases ---
        # Gradient = (Input to that layer).T dot (Delta of that layer)
        self.dW_ho = np.dot(self.hidden_layer_output.T, output_delta)
        self.db_o = np.sum(output_delta, axis=0, keepdims=True)

        self.dW_ih = np.dot(X.T, hidden_delta)
        self.db_h = np.sum(hidden_delta, axis=0, keepdims=True)

    def update_weights(self):
        """Updates weights and biases using gradient descent."""
        # --- FIX 1: Use -= for Gradient DESCENT ---
        self.W_ho -= self.learning_rate * self.dW_ho
        self.b_o -= self.learning_rate * self.db_o

        self.W_ih -= self.learning_rate * self.dW_ih
        self.b_h -= self.learning_rate * self.db_h

    def train(self, X, y, epochs):
        """Trains the neural network."""
        losses = []  # To store loss for plotting

        for epoch in range(epochs):
            predictions = self.forward(X)
            loss = np.mean(np.square(y - predictions))
            losses.append(loss)
            self.backward(X, y, predictions)
            self.update_weights()

            if (epoch + 1) % 1000 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.6f}")

        # Plot the loss curve
        plt.plot(losses)
        plt.title("Training Loss Curve")
        plt.xlabel("Epoch")
        plt.ylabel("Mean Squared Error")
        plt.show()

    def predict(self, X):
        """
        Makes predictions on new input data.

        Args:
            X (np.ndarray): New input data.

        Returns:
            np.ndarray: Predicted outputs.
        """
        return self.forward(X)


# --- 3. Example Usage ---
def main():
    # --- FIX 2: Use a solvable dataset (XOR) ---
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])  # XOR
    # -------------------------------------------

    input_size = X.shape[1]
    hidden_size = 4
    output_size = y.shape[1]
    learning_rate = 0.1  # This rate works well for XOR
    epochs = 20000

    print("--- Training a Simple Neural Network with NumPy ---")

    # Use 'relu' for the hidden layer, as it often learns faster
    nn = SimpleNeuralNetwork(
        input_size, hidden_size, output_size, learning_rate, hidden_activation="relu"
    )

    # Train the network
    nn.train(X, y, epochs)

    print(f"\nTraining complete. Total forward passes: {nn.counter}")

    # --- 4. Test the Trained Network ---
    print("\n--- Testing the Trained Network on All Inputs ---")

    predictions = nn.predict(X)
    rounded_predictions = np.round(predictions)

    print("Input (X) \t|\t True (y) \t|\t Predicted (raw) \t|\t Predicted (rounded)")
    print("-" * 75)
    for i in range(len(X)):
        print(
            f"{X[i]} \t\t|\t {y[i][0]} \t\t|\t {predictions[i][0]:.4f} \t\t\t|\t {rounded_predictions[i][0]}"
        )

    # --- FIX 3: Correct Accuracy Calculation ---
    accuracy = np.mean(rounded_predictions == y)
    print(f"\nFinal Training Accuracy: {accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()
