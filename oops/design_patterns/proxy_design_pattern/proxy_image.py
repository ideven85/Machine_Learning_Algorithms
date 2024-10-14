from oops.design_patterns.proxy_design_pattern.real_image import Image, RealImage


class ProxyImage(Image):
    def __init__(self, file_name):
        self._real_image = None
        self._file_name = file_name

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._file_name)
        self._real_image.display()
