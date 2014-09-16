#!/usr/bin/python


import json
import os
import sys



if __name__ == "__main__":

    for filename in sys.argv[1:]:

      if os.path.exists(filename):
        f   = open(filename)
        obj = json.load(f)

        print obj


