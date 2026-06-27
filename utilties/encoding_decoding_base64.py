# todo

from io import BytesIO
import matplotlib.pyplot as plt
import base64

# from PIL import Image
from IPython.display import Image


def encode_image(img):
    out = None
    with open(img, "rb") as f:
        image_data = f.read()
        # encode
        out = base64.b64encode(image_data)
    return out


def savefig(b, out_file=None):
    image_data = base64.b64decode(b)
    if not out_file:
        with open("sample.png", "wb") as f:
            f.write(image_data)

    else:
        with open(out_file, "wb") as f:
            f.write(image_data)

    print("Image Saved Successfully")


# Decode the base64 string back into binary data


def main():
    encoded = encode_image("model_io.jpg").decode("utf-8")
    print(f"Encoded image in utf-8:\n{encoded}")
    # savefig(encoded,'sample1.png')


if __name__ == "__main__":
    main()
