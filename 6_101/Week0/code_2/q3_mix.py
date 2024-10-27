"""
Question 3:

Larry implemented the mix function as shown below.
a)	What's good about Larry’s code?
b)	What could be improved style-wise?
c)	Are there any bugs? If so, what changes could you make to fix them.

Test function by running "pytest q3_mix.py" in the terminal (no quotes)
"""


def mix(sound1, sound2, p):
    # initialize a new sound
    new_sound = {}

    # scale the input sounds by p and 1-p
    sound1_scaled = []
    for s in sound1["samples"]:
        sound1_scaled.append(s * p)
    sound2_scaled = []
    for s in sound1["samples"]:
        sound2_scaled.append(s * 1 - p)

    # combine the scaled sounds
    if len(sound1_scaled) > len(sound2_scaled):
        new_length = len(sound2_scaled)
    else:
        new_length = len(sound1_scaled)
    new_samples = [0] * new_length
    for i in range(new_length):
        new_samples[i] = sound1_scaled[i] + sound2_scaled[i]

    # fill in the new sound with the new samples
    new_sound["rate"] = sound1["rate"]
    new_sound["samples"] = []
    for sample in new_samples:
        new_sound["samples"].append(sample)

    # return the mixed sound
    return new_sound


def test_mix_small():
    s1 = {
        "rate": 30,
        "samples": [1, 2, 3, 4, 5, 6],
    }
    s2 = {
        "rate": 20,
        "samples": [1, 2, 3, 4, 5, 6],
    }
    s3 = {
        "rate": 30,
        "samples": [7, 8, 9, 10],
    }

    s4 = {
        "rate": 30,
        "samples": [0.7 + 2.1, 1.4 + 2.4, 2.1 + 2.7, 2.8 + 3.0, 3.5 + 0, 4.2 + 0],
    }

    s5 = {
        "rate": 30,
        "samples": [0.3 + 4.9, 0.6 + 5.6, 0.9 + 6.3, 1.2 + 7.0, 1.5 + 0, 1.8 + 0],
    }

    assert mix(s1, s2, 0.5) is None
    compare_sounds(mix(s1, s3, 0.7), s4)
    compare_sounds(mix(s1, s3, 0.3), s5)
    compare_sounds(mix(s3, s1, 0.7), s5)
    compare_sounds(mix(s3, s1, 0.3), s4)


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
