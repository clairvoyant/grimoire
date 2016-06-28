#!/usr/bin/python 

import sys
import os
import argparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

OUTPUT="--output"
VERBOSE="--verbose"

def usage(err=0, str=""):
    print str
    print "Usage: %s [-v] %s FILENAME "  %(sys.argv[0], OUTPUT)
    print ""
    sys.exit(err)


def getCLI(argv):



    parser = argparse.ArgumentParser(description='process some files.')

    parser.add_argument('--infile',  type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--outfile', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()
    return args


def operation(fd):
    return os.fstat(fd.fileno()).st_size

if __name__ == "__main__":
   cli = getCLI(sys.argv)
   print "the input file size is ", bcolors.WARNING, operation(cli.infile), bcolors.ENDC

