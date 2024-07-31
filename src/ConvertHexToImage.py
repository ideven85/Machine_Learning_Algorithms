import cv2



with open("bluegill") as f:
    data = f.read()

data = bytes.fromhex(data)
with open("bluegill2.png", "wb") as f:
    f.write(data)
