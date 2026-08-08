import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


class BinomialGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Binomial Distribution - Coin Flips")

        # Parameters frame
        param_frame = ttk.Frame(root, padding="10")
        param_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Number of flips
        ttk.Label(param_frame, text="Number of flips:").grid(row=0, column=0)
        self.n_var = tk.StringVar(value="10")
        self.n_entry = ttk.Entry(param_frame, textvariable=self.n_var, width=10)
        self.n_entry.grid(row=0, column=1)

        # Probability of heads
        ttk.Label(param_frame, text="Probability of heads:").grid(row=1, column=0)
        self.p_var = tk.StringVar(value="0.5")
        self.p_entry = ttk.Entry(param_frame, textvariable=self.p_var, width=10)
        self.p_entry.grid(row=1, column=1)

        # Plot button
        ttk.Button(param_frame, text="Plot", command=self.plot_distribution).grid(
            row=2, column=0, columnspan=2
        )

    def plot_distribution(self):
        try:
            n = int(self.n_var.get())
            p = float(self.p_var.get())

            k = np.arange(0, n + 1)
            pmf = binom.pmf(k, n, p)

            plt.figure(figsize=(10, 6))
            plt.bar(k, pmf, alpha=0.8, color="skyblue", label=f"n={n}, p={p}")
            plt.title("Binomial Distribution of Coin Flips")
            plt.xlabel("Number of Heads")
            plt.ylabel("Probability")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()

        except ValueError:
            print("Please enter valid numbers")


class BinomialGUITendingToNormal:
    def __init__(self, root):
        self.root = root
        self.root.title("Normal Distribution Simulation")

        # Parameters frame
        param_frame = ttk.Frame(root, padding="10")
        param_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Number of samples
        ttk.Label(param_frame, text="Number of samples:").grid(row=0, column=0)
        self.n_var = tk.StringVar(value="1000")
        self.n_entry = ttk.Entry(param_frame, textvariable=self.n_var, width=10)
        self.n_entry.grid(row=0, column=1)

        # Mean
        ttk.Label(param_frame, text="Mean:").grid(row=1, column=0)
        self.mean_var = tk.StringVar(value="0")
        self.mean_entry = ttk.Entry(param_frame, textvariable=self.mean_var, width=10)
        self.mean_entry.grid(row=1, column=1)

        # Standard deviation
        ttk.Label(param_frame, text="Standard deviation:").grid(row=2, column=0)
        self.std_var = tk.StringVar(value="1")
        self.std_entry = ttk.Entry(param_frame, textvariable=self.std_var, width=10)
        self.std_entry.grid(row=2, column=1)

        # Plot button
        ttk.Button(param_frame, text="Plot", command=self.plot_distribution).grid(
            row=3, column=0, columnspan=2
        )

    def plot_distribution(self):
        try:
            n = int(self.n_var.get())
            mean = float(self.mean_var.get())
            std = float(self.std_var.get())

            # Generate normal distribution samples
            samples = np.random.normal(mean, std, n)

            plt.figure(figsize=(10, 6))
            plt.hist(
                samples,
                bins=50,
                density=True,
                alpha=0.8,
                color="skyblue",
                label=f"μ={mean}, σ={std}",
            )

            # Add the theoretical normal distribution curve
            x = np.linspace(mean - 4 * std, mean + 4 * std, 100)
            plt.plot(
                x,
                1
                / (std * np.sqrt(2 * np.pi))
                * np.exp(-((x - mean) ** 2) / (2 * std**2)),
                "r-",
                lw=2,
                label="Normal PDF",
            )

            plt.title("Normal Distribution Simulation")
            plt.xlabel("Value")
            plt.ylabel("Density")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()

        except ValueError:
            print("Please enter valid numbers")


def main():
    root = tk.Tk()
    app = BinomialGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
