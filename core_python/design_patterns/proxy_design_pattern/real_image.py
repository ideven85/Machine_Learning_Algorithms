import abc


class Image(abc.ABC):

    def display(self):
        raise NotImplementedError("Must be implemented by subclass")
        # pass


class RealImage(Image):
    def __init__(self, file_name):
        self._file_name = file_name
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading Image {self._file_name}")

    def display(self):

        print(f"Displaying Image {self._file_name}")
