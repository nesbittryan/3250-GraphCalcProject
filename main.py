#!/usr/bin/python
import sys
from Modules.Output.UI import *
from Modules.DataStructures.DocumentDictionary import *
from Modules.Input.Verifier import *

if len(sys.argv) == 2:
    with open(sys.argv[1],'r') as myFile:
        for line in myFile:
            status = goRunAll(line.rstrip())
            if not status:
                print line.rstrip() + " = " + str(getAnswer())
else:
    UI()
