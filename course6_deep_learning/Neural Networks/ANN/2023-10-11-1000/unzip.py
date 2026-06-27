import zipfile

with zipfile.ZipFile("archive.zip") as ref:
    ref.extractall()
