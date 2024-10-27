"""
Question 4:

Consider the following two implementations of convolution:
a- Do both implementations work?
b- What's the difference between them?
c- Only one would pass the speed check for the lab — which, and why?
d- Is this always the case?
Under what conditions will each implementation run faster?

Note: some of these tests will take a LONG TIME to finish running.
Hit 'ctrl+c' on your keyboard to stop the execution of the
current test and move on to the next one!
"""


def convolve1(sound, kernel):
    samples = [0] * (len(sound["samples"]) + len(kernel) - 1)
    for i, scale in enumerate(kernel):
        if scale != 0.0:  # potential speedup
            for j, ss in enumerate(sound["samples"]):
                samples[i + j] += ss * scale
    return {"rate": sound["rate"], "samples": samples}


def convolve2(sound, kernel):
    samples = [0] * (len(sound["samples"]) + len(kernel) - 1)
    for j, ss in enumerate(sound["samples"]):
        if ss != 0.0:  # potential speedup
            for i, scale in enumerate(kernel):
                samples[i + j] += ss * scale
    return {"rate": sound["rate"], "samples": samples}


def test_convolve_tiny(convolve):
    import time

    start = time.perf_counter_ns()

    inp = {
        "rate": 7,
        "samples": [1, 2, 3],
    }
    inp2 = {
        "rate": 7,
        "samples": [1, 2, 3],
    }
    exp = {
        "rate": 7,
        "samples": [1, 0, -1, -6],
    }
    compare_sounds(convolve(inp, [1, -2]), exp)
    assert inp == inp2, "be careful not to modify the inputs!"

    inp = {"rate": 20, "samples": [3, 0, -2, 1, 0, 4]}
    inp2 = {"rate": 20, "samples": [3, 0, -2, 1, 0, 4]}
    exp = {
        "rate": 20,
        "samples": [6, 15, -4, 4, 5, 0, 24, 0, 16],
    }
    compare_sounds(convolve(inp, [2, 5, 0, 4]), exp)
    assert inp == inp2, "be careful not to modify the inputs!"
    end = time.perf_counter_ns()
    return f"correct! {(end-start)/(10**9)} s"


def test_sparse_kernel(convolve, limit=10 * 10**9):
    import time
    import os
    import pickle

    fname = os.path.join(os.path.dirname(__file__), "sparse_kernel.pickle")
    with open(fname, "rb") as f:
        test_data = pickle.load(f)
    start = time.perf_counter_ns()
    try:
        for sound, kernel, expected in test_data:
            result = convolve(sound, kernel)
            compare_sounds(result, expected)
    except KeyboardInterrupt:
        end = time.perf_counter_ns()
        return f"too slow-- execution stopped after {(end-start)/(10**9)} s"

    end = time.perf_counter_ns()
    return f"correct! {(end-start)/(10**9)} s"


def test_sparse_sound(convolve, limit=10 * 10**9):
    import time
    import os
    import pickle

    fname = os.path.join(os.path.dirname(__file__), "sparse_sound.pickle")
    with open(fname, "rb") as f:
        test_data = pickle.load(f)
    # cut out 2nd test which is too long
    test_data = [test_data[0], test_data[2], test_data[3]]
    start = time.perf_counter_ns()

    try:
        for sound, kernel, expected in test_data:
            result = convolve(sound, kernel)
            compare_sounds(result, expected)
    except KeyboardInterrupt:
        end = time.perf_counter_ns()
        return f"incorrect! execution stopped after {(end-start)/(10**9)} s"

    end = time.perf_counter_ns()
    return f"correct! {(end-start)/(10**9)} s"


def compare_sounds(result, expected, eps=1e-6):
    # well formed?
    assert isinstance(result["rate"], int), "Sampling rate should be an integer"
    if "left" in result:
        assert len(result["left"]) == len(
            result["right"]
        ), "Left and Right channels do not have the same length"

    # matches expected?
    assert result["rate"] == expected["rate"], "Sampling rates do not match"

    # compare (different for stereo vs mono)
    if "left" in result:
        assert "left" in expected, "Expected mono sound, got stereo"
        assert len(result["left"]) == len(expected["left"]), "Lengths do not match"
        for ix, ((res_l, res_r), (exp_l, exp_r)) in enumerate(
            zip(
                zip(result["left"], result["right"]),
                zip(expected["left"], expected["right"]),
            )
        ):
            assert (
                abs(res_l - exp_l) <= eps and abs(res_r - exp_r) < eps
            ), f"Values at index {ix} do not match."
    else:
        assert "samples" in expected, "Expected stereo sound, got mono"
        assert len(result["samples"]) == len(
            expected["samples"]
        ), "Lengths do not match"
        for ix, (res, exp) in enumerate(zip(result["samples"], expected["samples"])):
            assert abs(res - exp) <= eps, f"Values at index {ix} do not match."


if __name__ == "__main__":
    convolve_funcs = [convolve1, convolve2]
    for test in [test_convolve_tiny, test_sparse_kernel, test_sparse_sound]:
        print(f"\n{test.__name__} results:")
        print(f"convolve1: {test(convolve1)}")
        print(f"convolve2: {test(convolve2)}")
