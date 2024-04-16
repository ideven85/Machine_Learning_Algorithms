import zipfile

with zipfile.ZipFile("../MIT_Readings.zip", "r") as zip_ref:
    zip_ref.extractall(".")
