import zipfile


def unzip_file(filename):
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(".")


def main():
    unzip_file("MasterCardStcokData.zip")


if __name__ == "__main__":
    main()
