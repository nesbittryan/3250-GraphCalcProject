#!/usr/bin/python
import Tkinter
import tkMessageBox
from Modules.DataStructures import DocumentDictionary
from Modules.Input.Parse import *

colours = ["black", "red", "green", "blue", "cyan", "yellow","magenta"]
currentColour = 0

#printing points
def drawPoints(x, y, canvas):
	hTable = readConfig()
	width = int(hTable['width'])
	height = int(hTable['height'])
	scale = width / (float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound())))
	X = []
	Y = []
	for i in range(len(x)):
		if isinstance(y[i], (int, float)):
			X.append(x[i] * scale + width/2)
			Y.append(-y[i] * scale + height/2)
			#draws points, uncomment to enable
			#canvas.create_oval(X[i], Y[i], X[i], Y[i])

	global currentColour

	for i in range(len(X) - 1):
		canvas.create_line(X[i], Y[i], X[i+1], Y[i+1], fill=colours[currentColour], width=2)
	if Y[0] <= 0:
		Y[0] = 40
	if Y[0] >= float(height):
		Y[0] = height - 40
	canvas.create_text(X[0] + 30,Y[0] - 10, text= (DocumentDictionary.getType()),fill=colours[currentColour])

	if currentColour == 6:
		currentColour = 0;
	else:
		currentColour = currentColour + 1

def drawLines(canvas):
	hTable = readConfig()
	width = int(hTable['width'])
	height = int(hTable['height'])
	scale = width / ((float(DocumentDictionary.getUpperBound()) - (float(DocumentDictionary.getLowerBound()))) / float(DocumentDictionary.getScale()))
	horLine= canvas.create_line(0, height/2, width, height/2, fill="black")
	vertLine = canvas.create_line(width/2, 0, width/2, height, fill="black")

	for x in range(0, width, int(scale)):
		canvas.create_line(x,height/2 + 4,x,height/2 -4, fill="black")

	canvas.create_text(10 ,height / 2 + 10, text= DocumentDictionary.getLowerBound(), tag = "cunt")
	canvas.create_text(width - 10 ,height / 2 + 10, text= DocumentDictionary.getUpperBound(), tag = "cunt")

	for y in range(0, height, int(scale)):
		canvas.create_line(width/2 + 4, y, width/2 -4,y, fill="black")
	canvas.create_text(width/2 + 10, 10, text= DocumentDictionary.getUpperBound(), tag = "cunt")
	canvas.create_text(width/2 + 10, height - 10, text= DocumentDictionary.getLowerBound(), tag = "cunt")


def graph(canvas):
	canvas.delete("cunt")
	x = DocumentDictionary.getTableOfValues()['xValues']
	y = DocumentDictionary.getTableOfValues()['yValues']
	drawLines(canvas)
	drawPoints(x, y, canvas)
