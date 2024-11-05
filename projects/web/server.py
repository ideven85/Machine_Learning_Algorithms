import os
import sys
import json
import time
import pickle
import mimetypes

import importlib

from wsgiref.handlers import read_environ
from wsgiref.simple_server import make_server


def main():
    with make_server("0.0.0.0",8008,None) as httpd:
