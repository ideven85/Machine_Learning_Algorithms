import zipfile

fileName = "../MIT_6_001.zip"
# with zipfile.ZipFile("../MIT_Readings.zip", "r") as zip_ref:
#     zip_ref.extractall(".")

with zipfile.ZipFile(fileName, "r") as zip_test:
    zip_test.testzip()
