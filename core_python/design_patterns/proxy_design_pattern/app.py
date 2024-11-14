"""
Client Will call the proxy object and the image will be created only once
"""

from core_python.design_patterns.proxy_design_pattern.proxy_image import ProxyImage


def client():
    image = ProxyImage("example.jpg")
    image.display()  # Real Image Called And It's object created

    image.display()  # Now the image is cached and will not be loaded again from disk


if __name__ == "__main__":
    client()
