from zipfile import ZipFile

with ZipFile("model-checkpoint-tensorflow.zip", "r") as f:
    f.extractall(".")
