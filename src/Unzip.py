import zipfile
from pathlib import Path
import os

fileName = "../6_001.zip"
BASE_DIR = Path(__name__).resolve().parent
with zipfile.ZipFile(fileName, "r") as zip_ref:
    zip_ref.extractall(Path)
