#!/usr/bin/python 

import sys
import os
import getopt


OUTPUT="--output"
VERBOSE="--verbose"

def usage(err=0, str=""):
    print str
    print "Usage: %s [-v] %s FILENAME "  %(sys.argv[0], OUTPUT)
    print ""
    sys.exit(err)

class CLI:
      def __init__(self):
          self.output  = ""
          self.verbose = 0
      def getOutput(self):
          return self.output
      def getVerbose(self):
          return self.verbose
      def incrVerbose(self):
          self.verbose +=1
      def setOutput(self, filename):
          self.output = filename

      def __str__(self):
          return "selected verbose=%d outputfile=%s" %(self.verbose, self.output)


def getCLI(argv):
    cli = CLI()

    try:
        opts, args = getopt.getopt(argv[1:], "hvo:", ["help", "output=", "verbose"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    
    for o, a in opts:
        if o in ("-v", VERBOSE):
            cli.incrVerbose() 
        elif o in ("-h", "--help"):
            usage(-1)
        elif o in ("-o", OUTPUT):
            cli.setOutput(a)
        else:
            assert False, "unhandled option"


    return cli



if __name__ == "__main__":
   cli = getCLI(sys.argv)
   print cli




