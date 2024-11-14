class FileManager:
    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self._file_name, self._mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def main():
    with FileManager("../data/test.txt", "w") as f:
        f.write("Writing using own with open method of file..\n Pretty Basic")


if __name__ == "__main__":
    main()
