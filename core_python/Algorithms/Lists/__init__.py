import os
from os import *
import sys

for key, value in os.environ.items():
    print(f"{key}: {value}")
