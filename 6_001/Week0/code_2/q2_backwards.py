"""
Question 2:
For each version of backwards below, circle T if it is correctly implemented
and F if it is incorrect.

Note for each:
 - what's good about this solution to backwards()?
 - what could be improved?
 - what might be buggy? (/ what could you do to fix it?)
"""

def backwardsA(sound):
    # version a:     correct? T   F
    new_samples = sound["samples"]
    new_samples.reverse()
    return {
        "rate": sound["rate"],
        "samples": new_samples,
    }


def backwardsB(sound):
    # version b:     correct? T   F
    samples = []
    slen = len(sound["samples"])
    for i in range(slen, 0, -1):
        samples.append(sound["samples"][i])

    return {
        "rate": sound["rate"],
        "samples": samples
    }


def backwardsC(sound):
    # version c:     correct? T   F
    new_sound = sound.copy()
    new_sound["samples"].reversed()
    return new_sound


def backwardsD(sound):
    # version d:     correct? T   F
    return {
        "rate": sound["rate"],
        "samples": sound["samples"][::-1],
    }


def backwardsE(sound):
    # version e:     correct? T   F
    return {
     "rate": sound["rate"],
     "samples":
       reversed(sound["samples"]),
    }


def backwardsF(sound):
    # version f:     correct? T   F
    return {
        "rate": sound["rate"],
        "samples": sound["samples"].reverse(),
    }


def test_backwards(backwards_func):
    inp = {
        'rate': 20,
        'samples': [1,2,3,4,5,6],
    }
    inp2 = {
        'rate': 20,
        'samples': [1,2,3,4,5,6],
    }
    expected = {
        'rate': 20,
        'samples': [6,5,4,3,2,1],
    }
    try:
        result = backwards_func(inp)
        assert result == expected, f'{result=} but {expected=}'
        assert inp == inp2, 'be careful not to modify the input!'
    except Exception as e:
        return e
    return "is correct!"

if __name__ == "__main__":
    functions = [backwardsA, backwardsB, backwardsC,
                 backwardsD, backwardsE, backwardsF]
    for func in functions:
        print(f'{func.__name__}: {test_backwards(func)}')