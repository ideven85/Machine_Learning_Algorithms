from dataclasses import dataclass


@dataclass
class Apple:
    color: str
    weight: int


def apple_inventory():
    return [
        Apple("Green", 160),
        Apple("BLUE", 80),
        Apple("RED", 70),
        Apple("RED", 180),
        Apple("GREEN", 140),
    ]


def filtering_apples_by_client_criteria(predicate):
    return [apple for apple in apple_inventory() if predicate(apple)]


def filtering_apples():
    """ """
    # print(apple_inventory())
    heavy_apples = [x for x in apple_inventory() if x.weight >= 150]
    green_apples = [x for x in apple_inventory() if x.color.lower() == "green"]
    green_and_heavy_apples = [
        x for x in apple_inventory() if x in heavy_apples and x in green_apples
    ]
    red_apples = list(filter(lambda x: x.color.lower() == "red", apple_inventory()))

    return heavy_apples, green_apples, green_and_heavy_apples, red_apples


def main():
    heavy_apples, green_apples, green_and_heavy_apples, red_apples = filtering_apples()
    print("Apples with weight greater than 150", heavy_apples)
    print("Green Apples", green_apples)
    print("Apples with weight greater than 150 and color green", green_and_heavy_apples)
    print("Red Apples using filter", red_apples)


if __name__ == "__main__":
    main()
