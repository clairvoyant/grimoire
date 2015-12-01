#!/usr/bin/python


import glob
import unittest
import sys
import os

def create_test_suite(path):

    test_file_strings = glob.glob(os.path.join(path, 'Test*.py'))
    module_strings = [str[5:len(str)-3] for str in test_file_strings]
    print "jrv::path::", path, module_strings
    suites = [unittest.defaultTestLoader.loadTestsFromName(name) \
              for name in module_strings]

    print "jrv::suites::", suites
    testSuite = unittest.TestSuite(suites)

   
    return testSuite

if __name__ == "__main__":
   sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../src/') ))


   testSuite = create_test_suite(sys.argv[0])
   runner=unittest.TextTestRunner()
   runner.run(testSuite)
