def create_file(file_name):
    f = open(file_name, "w")
    text = "Hi my name is deven"
    f.write(text)
    # Not closing file
    f.close()


def main():
    create_file("test.txt")


if __name__ == "__main__":
    main()
