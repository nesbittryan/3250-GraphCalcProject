# File responsible for managing calculations at the finest (i.e bottom of the tree)
from __future__ import division
from Modules.DataStructures import Tree
from Modules.DataStructures import DocumentDictionary

import math


# process one node that is parent of operands nodes
def process(tree, nodeIndex):
	# security layer and domain out of bound handling
	try:
		if tree[Tree.leftChildIndex(nodeIndex)] != None:
			left = float(tree[Tree.leftChildIndex(nodeIndex)])
		else:
			left = None
		if tree[Tree.rightChildIndex(nodeIndex)] != None:
			right = float(tree[Tree.rightChildIndex(nodeIndex)])
		else:
			right = None

		parent = tree[nodeIndex]
		result = calculate(parent, left, right)
		tree[nodeIndex] = result
		Tree.removeChilds(tree, nodeIndex)

	except ValueError, e:
		if (e.message == "math domain error"):
			DocumentDictionary.setProcessError(False)


# calculate parent value given two operands child nodes
def calculate(parent, left, right):
	result = operators[parent](left, right)
	return result

# define the different function blocks
def addition(left, right):
	return left + right


def multiplication(left, right):
	return left * right


def substraction(left, right):
	return left - right


def div(left, right):
	# TODO: division by zero to be tested
	try:
		result = left / right
		return result
	except ZeroDivisionError:
		DocumentDictionary.setProcessError(False)
		return None


def sinus(left, right):
	if DocumentDictionary.isRad():
		return math.sin(left)
	else:
		return math.sin(math.radians(left))


def cosinus(left, right):
	if DocumentDictionary.isRad():
		return math.cos(left)
	else:
		return math.cos(math.radians(left))


def tangente(left, right):
	if DocumentDictionary.isRad():
		return math.tan(left)
	else:
		return math.tan(math.radians(left))


def arcsinus(left, right):
	if DocumentDictionary.isRad():
		return math.asin(left)
	else:
		return math.asin(math.radians(left))


def arccosinus(left, right):
	if DocumentDictionary.isRad():
		return math.acos(left)
	else:
		return math.acos(math.radians(left))


def arctangente(left, right):
	if DocumentDictionary.isRad():
		return math.atan(left)
	else:
		return math.atan(math.radians(left))


def sinhyp(left, right):
	if DocumentDictionary.isRad():
		return math.sinh(left)
	else:
		return math.sinh(math.radians(left))


def coshyp(left, right):
	if DocumentDictionary.isRad():
		return math.cosh(left)
	else:
		return math.cosh(math.radians(left))


def tanhyp(left, right):
	if DocumentDictionary.isRad():
		return math.tanh(left)
	else:
		return math.tanh(math.radians(left))


def arcsinhyp(left, right):
	if DocumentDictionary.isRad():
		return math.asinh(left)
	else:
		return math.asinh(math.radians(left))


def arccoshyp(left, right):
	if DocumentDictionary.isRad():
		return math.acosh(left)
	else:
		return math.acosh(math.radians(left))


def arctanhyp(left, right):
	if DocumentDictionary.isRad():
		return math.atanh(left)
	else:
		return math.atanh(math.radians(left))


def squareroot(left, right):
	return math.sqrt(left)


def power(left, right):
	return math.pow(left, right)


def log(left, right):
	return math.log10(left)


def ln(left, right):
	return math.log(left)


def exp(left, right):
	# Handling both case left or right just in case, it's a "security" layer
	if right == None:
		return math.exp(left)
	elif left == None:
		return math.exp(right)


# map the inputs to the function blocks
operators = {
	"+": addition,
	"*": multiplication,
	"-": substraction,
	"/": div,
	"sin": sinus,
	"cos": cosinus,
	"tan": tangente,
	"arcsin": arcsinus,
	"arccos": arccosinus,
	"arctan": arctangente,
	"sinh": sinhyp,
	"cosh": coshyp,
	"tanh": tanhyp,
	"arcsinh": arcsinhyp,
	"arccosh": arccoshyp,
	"arctanh": arctanhyp,
	"sqrt": squareroot,
	"^": power,
	"log": log,
	"ln": ln,
	"e^": exp,
}
