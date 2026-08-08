import array
import main as inference

# Representing our "Slow Memory" - Large parameter weights stored in System RAM
# Using Python's native 'array' module ensures a contiguous C-style memory layout
parameters_in_ram = array.array(
    "f", [0.1, 0.5, -0.2, 0.8] * 250000
)  # 1 Million weights

# Representing the immediate, incoming data-point
token_input = array.array("f", [1.0, 2.0, 3.0, 4.0] * 250000)

print("Starting hardware-accelerated inference pass via Cython...")

# The CPython interpreter passes raw pointers down.
# The GIL drops, and activations are computed entirely in the hardware cache.
outputs = inference.run_layer(parameters_in_ram, token_input)

print(f"Pass complete. Generated {len(outputs)} activation points safely.")
