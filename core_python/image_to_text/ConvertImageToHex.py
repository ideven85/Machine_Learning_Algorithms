from binascii import hexlify
import re

hexValNew = ""
placeHolder = "0"

file = open("bluegill.hex", "w")

with open("bluegill.png", "rb") as f:
    binVal = f.read(1)
    while len(binVal):
        hexVal = hex(ord(binVal))
        hexValNew = hexVal[2:4]
        hexString = str(hexValNew)

        if len(hexString) == 1:
            hexString = placeHolder + hexString
        file.write(hexString)
        binVal = f.read(1)
file.close()
