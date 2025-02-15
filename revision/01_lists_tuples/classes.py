class Demo:
    @classmethod
    def hello(*args):
        return args

    @staticmethod
    def hello_static(*args):
        return args


def main():
    print(Demo.hello("class"))  # (<class '__main__.Demo'>, 'class')

    print(
        "static", Demo.hello_static, "class", Demo.hello
    )  # static <function Demo.hello_static at 0x1043ce520> class <bound method Demo.hello of <class '__main__.Demo'>>

    print(Demo.hello_static("class"))


if __name__ == "__main__":
    main()
