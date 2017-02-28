from Modules.DataStructures.DocumentDictionary import *
from Modules.DataStructures.Tree import *
from Modules.Maths.Calculation import *

tree = []

# Processing the tree and make calculations of the bottom values of the tree
def postOrderProcess(tree, root):
	# stands for not a number
	nAn = not isOperand(tree[root])
	if nAn:
		# verifying there's something to deal with at the left child
		if not tree[leftChildIndex(root)] == None:
			postOrderProcess(tree, leftChildIndex(root))
		# same for right child
		if not tree[rightChildIndex(root)] == None:
			postOrderProcess(tree, rightChildIndex(root))
	else:
		if not process(tree, parentIndex(root)):
			return False


# Loop to process over and over again until there's a final result
def processLoop(main):
	tree = main
	# changing stuff in order to be numbers and no constants or factorials anymore
	while ((getProcessError()) and (not isOperand(tree[1]))):
		postOrderProcess(tree, 1)
	if getProcessError():
		return tree[1]
	else:
		return None


# Prepare the tree for the process
def prepareTree(tree):
	tree = replaceVariables("pi", math.pi, tree)
	tree = replaceVariables("e", math.e, tree)
	tree = replaceFacto(tree)
	return tree


# Replaces character variables with defined values
def replaceVariables(variable, value, table):
	result = list(table)
	for i in range(len(table)):
		if table[i] == variable:
			result[i] = value
	return result


# Factorials handling
def replaceFacto(table):
	result = list(table)
	for i in range(len(table)):
		try:
			if '!' in table[i]:
				tmp = table[i].replace('!', '')
				try:
					result[i] = math.factorial(float(tmp))
				except ValueError:
					useless = None
		except TypeError:
			useless = None
	return result


# Iterates and create a table from the low boundary to the up boundary, given the variable as a string ("x" or "y" or ..)
def iteratesDomain(tree):
	# Initialise and recovers data from the dictionnary
	domainLowBound = float(getLowerBound())
	domainUpBound = float(getUpperBound())
	interval = float(getScale())
	table = tree

	# Initiating the future loop
	preimage = []
	image = []
	j = domainLowBound

	# Cause of int rounding inside "range", we need to set the last value, that's why the + 1 is there
	for i in range(int((domainUpBound - domainLowBound) / interval) + 1):
		# Reinitialising the domain out of bound error "detector"
		setProcessError(True)
		preimage.append(j)
		# Creates a temporary copy of the table representation of the tree so we keep untouched the "main" tree with variables
		temp = replaceVariables("x", j, table)
		image.append(processLoop(temp))
		j += interval
		i += 1

	tableOfValues = {
		"xValues": preimage,
		"yValues": image
	}

	# Writing the table of values inside the global dictionary
	setTableOfValues(tableOfValues)
	return tableOfValues


# Check if this a number or not from a string
def isOperand(item):
	try:
		float(item)
		return True
	except ValueError:
		return False


# GOOOOOOO LET'S RANCH IT UP, triggers the calculation process
def go():
	try:
		docTree = getTree()
		# If we have a variable in the tree, it means we have to iterate on a domain
		if "x" in docTree:
			docTree = prepareTree(docTree)
			iteratesDomain(docTree)
		# If not we just expect a single number as an answer
		else:
			docTree = prepareTree(docTree)
			result = processLoop(docTree)
			setAnswer(result)
	except TypeError:
		setAnswer(None)
		setTableOfValues(None)
