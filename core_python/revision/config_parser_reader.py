import ast
import configparser
import os.path
from configparser import ConfigParser, BasicInterpolation, ExtendedInterpolation


def reader_normal(file_name):
    """
    Reads from a cfg file and prints to console
    """

    config = configparser.RawConfigParser()

    # config_normal = ConfigParser(interpolation=ExtendedInterpolation)
    config_normal = ConfigParser()
    config_normal.read(file_name)
    config.read("example.cfg")

    curr_date = config_normal.get("Articles", "blogs")
    a_float = config.getfloat("Section1", "a_float")
    print(curr_date)
    print(type(a_float))
    print(config.get("Section1", "foo"))
    print(list(config["Section1"].values()))
    print(list(config["Section1"].keys()))

    print(config_normal.sections())
    secret = config_normal["topsecret.server.example"]
    print(list(secret.values()))


def reader_with_interpolation(file_name):
    parser = ConfigParser(interpolation=ExtendedInterpolation)
    parser.read_string(
        """
    [DEFAULT]
    hash = #

    [hashes]
    shebang =
      ${hash}!/usr/bin/env python
      ${hash} -*- coding: utf-8 -*-

    extensions =
      enabled_extension
      another_extension
      #disabled_by_comment
      yet_another_extension

    interpolation not necessary = if # is not at line start
    even in multiline values = line #1
      line #2
      line #3
    """
    )
    print(parser["hashes"]["shebang"])


def main():
    reader_normal("example.cfg")
    reader_with_interpolation("interpolated.cfg")


if __name__ == "__main__":
    main()
