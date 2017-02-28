#!/usr/bin/python
from Modules.DataStructures.DocumentDictionary import *
import re
MathFunctions = ['arcsinh', 'arccosh', 'arctanh', 'sinh', 'cosh', 'tanh', 'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sqrt', 'log', 'ln']

myList = [None] * 50

#
#	getList
#	Return the list representation of a tree.
#	NOTE: Left is (2 * i), Right is (2 * i) + 1
#
def getList():
	return myList

def initList():
	global myList
	myList = [None] * 50

def split(equation):
	parentheses = 0
	count = -1
	for i in equation:
		count += 1
		if i == '(':
			parentheses += 1
		elif i == ')':
			parentheses -= 1
		if(parentheses == 1 and isOperator(i)):
			return count
	return -1

def isOperator(c):
	if(c == '+' or c == '-' or c == '*' or c =='/' or c == '^'):
		return 1
	return 0

#
#	parseString
#	Calculates the list representation of a list.
#	IN: (String) the equation.
#	NOTE: Left is (2 * i), Right is (2 * i) + 1. (See getList() to access the list)
#
def parseString(equation, index=1):
	if index is 1:
		initList()
	length = len(equation)
	for i,function in enumerate(MathFunctions):
		size = len(function)
		if function in equation[1:size+1]:
			myList[index] = function
			parseString(equation[size+1:length], index*2)
			return
	position = split(equation)
	if(position != -1):
		parent = equation[position]
		myList[index] = parent
	else:
		myList[index] = equation.strip('()')
	if(position != -1):
		parseString(equation[1:position], index * 2)
		parseString(equation[position+1:length-1], index * 2 + 1)
	return

def replace():
	for index,item in enumerate(myList):
		if item is '':
			myList[index] = '0'

def goFill(eq):
	initList()
	parseString(eq)
	replace()
	setTree(myList)
