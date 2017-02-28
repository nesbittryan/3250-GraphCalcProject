#!/usr/bin/python

#
#   Dictionary Structure
#
dictionary = {
    'name' : "",
    'type' : "",
    'answer' : None,
    'radians': False,
    'scale' : 0.1,
    'lowerBound' : -10,
    'upperBound' : 10,
    'range' : "",
    'tableOfValues' : {
        "xValues": None,
        "yValues": None
    },
    'tree' : None,
    'isError' : "",
    'processError' : True
}

def setProcessError(whatever):
    dictionary['processError'] = whatever

def getProcessError():
    return dictionary['processError']
#
#   getName
#   Get the value of name in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getName():
    return dictionary['name']

#
#   getType
#   Get the value of type in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getType():
    return dictionary['type']

#
#   getAnswer
#   Get the value of answer in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getAnswer():
    return dictionary['answer']

#
#   isRad
#   Get the value of radian in the document dictionary.
#   IN: NONE.
#   OUT: (Bool) name.
#
def isRad():
    return dictionary['radians']

#
#   getScale
#   Get the value of scale in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getScale():
    return dictionary['scale']

#
#   getLowerBound
#   Get the value of lower bound in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getLowerBound():
    return dictionary['lowerBound']

#
#   getUpperBound
#   Get the value of upper bound in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getUpperBound():
    return dictionary['upperBound']

#
#   getRange
#   Get the value of range in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getRange():
    return dictionary['range']

#
#   getTableOfValues
#   Get the value of tableOfValues in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getTableOfValues():
    return dictionary['tableOfValues']

#
#   getTree
#   Get the value of tree in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getTree():
    return dictionary['tree']

#
#   getIsError
#   Get the value of isError in the document dictionary.
#   IN: NONE.
#   OUT: (String) name.
#
def getIsError():
    return dictionary['isError']

#
#   setName
#   Sets the name value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setName(val):
    dictionary['name'] = val

#
#   setType
#   Sets the type value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setType(val):
    dictionary['type'] = val

#
#   setAnswer
#   Sets the answer value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setAnswer(val):
    dictionary['answer'] = val

#
#   setRad
#   Sets the radian value of the document dicitionary.
#   IN: (Bool) the value to update.
#   OUT: NONE.
#
def setRad(val):
    dictionary['radians'] = val

#
#   setScale
#   Sets the scale value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setScale(val):
    dictionary['scale'] = val

#
#   setLowerBound
#   Sets the lower domain bound value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setLowerBound(val):
    dictionary['lowerBound'] = val

#
#   setUpperBound
#   Sets the upper domain bound value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setUpperBound(val):
    dictionary['upperBound'] = val

#
#   setRange
#   Sets the range value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setRange(val):
    dictionary['range'] = val

#
#   setTableOfValues
#   Sets the table of values value of the document dicitionary.
#   IN: (Dictionary) the document object, (String) the value to update.
#   OUT: NONE.
#
def setTableOfValues(val):
    dictionary['tableOfValues'] = val

#
#   setTree
#   Sets the tree value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setTree(val):
    dictionary['tree'] = val

#
#   setIsError
#   Sets the isError value of the document dicitionary.
#   IN: (String) the value to update.
#   OUT: NONE.
#
def setIsError(val):
    dictionary['isError'] = val
