import os
import zipfile


def unzip(file_name):
    with zipfile.ZipFile(file_name, "r") as zip_ref:
        zip_ref.extractall(".")


def main():
    for f in os.listdir("."):
        if f.endswith("zip"):
            unzip(f)


if __name__ == "__main__":
    main()
