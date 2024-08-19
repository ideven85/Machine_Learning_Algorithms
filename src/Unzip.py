import zipfile
from pathlib import Path
import os

def unzip(fileName):
    BASE_DIR = Path(__name__).resolve().parent.parent.parent
    directory_name= fileName[:fileName.find(".")]
    with zipfile.ZipFile(fileName, "r") as zip_ref:
        zip_ref.extractall(os.path.expanduser("~/")+directory_name)

unzip("../Python_Reading.zip")