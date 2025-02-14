import configparser
from datetime import datetime

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config = configparser.RawConfigParser()
config.add_section("Articles")
config.set("Articles", "blogs", "f{datetime.day}")
config.add_section("Section1")
config.set("Section1", "an_int", "15")
config.set("Section1", "a_bool", "true")
config.set("Section1", "a_float", "3.1415")
config.set("Section1", "baz", "fun")
config.set("Section1", "bar", "Python")
config.set("Section1", "foo", "%(bar)s is %(baz)s!")

with open("data/example.cfg", "w") as f:
    config.write(f)
