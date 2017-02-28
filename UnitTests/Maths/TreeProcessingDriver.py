#!/usr/bin/python
from Testing import *
from Modules.DataStructures.DocumentDictionary import *
from Modules.Maths.TreeProcessing import *

#
#   Verify Driver
#   Verify the functions within verifier
#
printHeader("Math Processing Driver", "Testing functions mathematical processing functions.")

eq = "(sin(90))"
setTree([None, 'sin', '90', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 1)

eq = "(((1+2)^3)*4)"
setTree([None, '*', '^', '4', '+', '3', None, None, '1', '2', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 108)

eq = "((2+4)*2)"
setTree([None, '*', '+', '2', '2', '4', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 12)

eq = "(((2+4)!)+2)"
setTree([None, '+', '!', '2', '+', None, None, '2', '4', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 722)

eq = "(pi+e)"
setTree([None, '+', "pi", "e", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, math.e + math.pi)

eq = "sin(pi)"
setRad(True)
setTree([None, 'sin', 'pi', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, 0)

eq = "6!"
setRad(True)
setTree([None, '6!', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
go()
ans = getAnswer()
assertEqual("The equation " + eq + " yields " + str(ans)  + ".", ans, math.factorial(6))

