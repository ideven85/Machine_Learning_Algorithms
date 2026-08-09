#!/usr/bin/env python

import requests


def concept_net():
    response = requests.get("http://api.conceptnet.io/c/en/example")

    return response


def main():
    """
    Trying for now
    """
    print(concept_net())


if __name__ == "__main__":
    main()
