# cython: boundscheck=False, wraparound=False, cdivision=True
from libc.stdlib cimport malloc, free

# A mock function simulating an intensive matrix dot product or attention step.
# By declaring it 'cdef', it compiles into pure machine code (no Python object overhead).
cdef void hardware_kernel(float* weights, float* inputs, float* activations, int size) noexcept nogil:
    cdef int i
    # The CPU/NPU detects this tight loop and holds the 'activations' memory array
    # directly inside the ultra-fast L1/L2/L3 Hardware Cache or local SRAM registers.
    for i in range(size):
        activations[i] = inputs[i] * weights[i]

# The high-level function exposed to CPython
def run_layer(float[::1] parameters_ram, float[::1] current_input):
    """
    parameters_ram: Lives in main System RAM / VRAM (Slow Memory).
    current_input:  The immediate token or pixel data.
    """
    cdef int size = parameters_ram.shape[0]

    # 1. Allocate a local, transient scratchpad for our Activations.
    # This represents the "Fast Memory" or "Statistic of a datapoint".
    cdef float* activations_cache = <float*>malloc(size * sizeof(float))

    if not activations_cache:
        raise MemoryError("Failed to allocate activation memory.")

    # 2. Extract raw pointers from the Python memoryviews to feed the hardware
    cdef float* p_weights = &parameters_ram[0]
    cdef float* p_inputs = &current_input[0]

    # 3. RELEASE THE GIL: CPython drops its lock entirely.
    # The math executes at maximum hardware speed on native threads.
    with nogil:
        hardware_kernel(p_weights, p_inputs, activations_cache, size)

    # 4. Safely package the transient activation results back into a Python object
    # right before freeing the transient cache memory.
    cdef list result = []
    cdef int i
    for i in range(size):
        result.append(activations_cache[i])

    # Clean up the fast activation memory workspace
    free(activations_cache)

    return result
