#!/usr/bin/python

import sys
sys.path.insert(0, '../')
from Testing import *

printHeader("Welcome to Graphing Calculator Unit Test","Author:(G2) Comet Allstars v1.0")
print "To call individual unit tests call the ./ApplicationDriver <NameOfUnitTest>\nNote: Omit 'Driver'... i.e. ./ApplicationDriver Input"

getAll = False
if len(sys.argv) == 1:
    getAll = True

#
#   Input Unit Tests
#

if getAll or "Input" in sys.argv:
    from UnitTests.Input.InputDriver import *

#
#   Math Unit Tests
#

if getAll or "FillTree" in sys.argv:
    from UnitTests.Maths.FillTreeDriver import *

if getAll or "TreeProcessing" in sys.argv:
    from UnitTests.Maths.TreeProcessingDriver import *

if "Help" in sys.argv:
    print ""
else:
    printSectionHeader("Overall Results:")
    printResults()
