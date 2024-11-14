from tqdm import tqdm

from time_elapsed import clock
from debug_recursion import show_recursive_structure


@clock
@show_recursive_structure
def power_mod(base, exponent=2, modulus=1000007):
    if exponent == 0:
        result = 1
    elif exponent == 1:
        result = base
    elif exponent % 2 == 0:
        result = power_mod(base, exponent // 2, modulus)
        result *= result
    else:
        result = base * power_mod(base, exponent - 1, modulus)
    return result


def tqdm_usage():
    for i in tqdm(range(10)):
        print(i)


def main():
    base = 190000
    exponent = 29
    print(power_mod(base, exponent))


if __name__ == "__main__":
    tqdm_usage()
    main()
