#Given a node index, returns the index of its left child
def leftChildIndex(index):
	return 2*index

#Given a node index, returns the index of its right child
def rightChildIndex(index):
	return (2*index)+1

#Given a node index, returns the index of its parent node
def parentIndex(index):
	if index%2 == 0:
		return index/2
	else:
		return (index-1)/2

#Still keeping track of this incase of an Object version later on
# #Given a node index, returns the value at this index
# def getAtIndex(index):
# 	return table[index]
#
# #Given a node index, sets the value at this index
# def setAtIndex(index, value):
# 	table[index] = value

#Given a node index, removes its children
def removeChilds(tree,index):
	tree[leftChildIndex(index)] = None
	tree[rightChildIndex(index)] = None

