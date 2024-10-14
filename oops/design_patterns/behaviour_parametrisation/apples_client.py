from filtering_apples import apple_inventory

#Sample Client
def red_and_light_apples(color,weight):
    """
    Client wants only red colored apples with weight less than 120
    Sure Can be made more elegant
    """
    return [
        apple
        for apple in apple_inventory()
        if apple.color.lower() ==color and apple.weight <= weight
    ]


def main():
    print(red_and_light_apples("red",120))


if __name__ == "__main__":
    main()
