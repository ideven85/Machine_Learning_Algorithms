import zipfile
from pathlib import Path
import os


def unzip(file_name):
    if not os.path.expanduser(file_name):
        return
    BASE_DIR = Path(__name__).resolve().parent.parent.parent
    print(BASE_DIR)
    directory_name = file_name[: file_name.find(".")]
    with zipfile.ZipFile(file_name, "r") as zip_ref:
        zip_ref.extractall(os.path.expanduser("~/") + directory_name)


unzip("../Python_Reading.zip")
