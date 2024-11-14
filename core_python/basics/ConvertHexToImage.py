import cv2


with open("data/images/bluegill.hex", "r") as f:
    data = f.read()

data = bytes.fromhex(data)
with open("data/images/bluegill3.png", "wb") as f:
    f.write(data)
