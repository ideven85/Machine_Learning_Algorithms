"""
6.101 Lab:
LISP Interpreter Part 2
"""

#!/usr/bin/env python3
import sys

sys.setrecursionlimit(20_000)

# KEEP THE ABOVE LINES INTACT, BUT REPLACE THIS COMMENT WITH YOUR lab.py FROM
# THE PREVIOUS LAB, WHICH SHOULD BE THE STARTING POINT FOR THIS LAB.


if __name__ == "__main__":
    # NOTE THERE HAVE BEEN CHANGES TO THE REPL, KEEP THIS CODE BLOCK AS WELL
    # code in this block will only be executed if lab.py is the main file being
    # run (not when this module is imported)

    import os

    sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
    import schemerepl

    schemerepl.SchemeREPL(
        sys.modules[__name__], use_frames=True, verbose=False, global_frame=None
    ).cmdloop()
