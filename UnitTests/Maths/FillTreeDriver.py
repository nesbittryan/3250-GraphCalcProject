#!/usr/bin/python

from Testing import *
from Modules.Maths.FillTree import *

#
#   Verify Driver
#   Verify the functions within verifier
#
printHeader("Fill Tree Driver", "Testing functions in FillTree: parseString.")

eq = "((5.25+(6*7))-(9/1))"
parseString(eq)
ans = [None, '-', '+', '/', '5.25', '*', '9', '1', None, None, '6', '7', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)
myList = [None] * 50

eq = "((2*x)+5)"
parseString(eq)
ans = [None, '+', '*', '5', '2', 'x', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)

eq = "(sin(2))"
parseString(eq)
ans = [None, 'sin', '2', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)

eq = "(((2+4)!)+2)"
parseString(eq)
ans = [None, '+', '!', '2', '+', None, None, '2', '4', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)

eq = "(((1+2)^3)*4)"
parseString(eq)
ans = [None, '*', '^', '4', '+', '3', None, None, '1', '2', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)

eq = "((5!^2)+(sin(8+2)))"
parseString(eq)
ans = [None, '+', '^', 'sin', '5!', '2', '+', None, None, None, None, None, '8', '2', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
ansList = getList()
assertEqual("The equation " + eq + " list is equal.", ans, ansList)
