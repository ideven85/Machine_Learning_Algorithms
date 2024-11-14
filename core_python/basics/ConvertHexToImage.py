import cv2


with open("images/bluegill.hex", "r") as f:
    data = f.read()

data = bytes.fromhex(data)
with open("images/bluegill3.png", "wb") as f:
    f.write(data)
