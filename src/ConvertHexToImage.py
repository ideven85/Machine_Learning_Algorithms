import cv2


with open("bluegill.hex",'r') as f:
    data = f.read()

data = bytes.fromhex(data)
with open("bluegill3.png", "wb") as f:
    f.write(data)
