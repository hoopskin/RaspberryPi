import turtle as t
import sys

def printHexagon(printSides):
	i = 0
	while (i <= 5):
		if (printSides[i] == 1):
			t.forward(12.5)
		else:
			t.penup()
			t.forward(12.5)
		t.penup()
		t.forward(12.5)
		t.pendown()
		t.right(60)
		i = i + 1

def goToNextHex():
	#Go to Middle of Current Hex
	t.penup()
	t.right(60)
	t.forward(25)
	
	#Go to next hex's middle
	t.left(90)
	#.866 for distance to edge, 2 for going to next middle
	t.forward(.866*25*2)
	
	#Set up for next Hexagon
	t.left(90)
	t.forward(25)
	t.right(90)
	t.right(30)
	t.pendown()

def goToStart():
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.left(90)
	t.forward(200)
	t.left(90)
	t.forward(250)
	t.right(180)
	t.right(30)
	t.pendown()

def goToEvenLine():
	t.penup()
	t.right(60)
	t.forward(72.5)
	t.right(90)
	#t.pendown()
	t.forward(.866*25*2*11)
	t.forward(.866*25)
	t.right(90)
	t.forward(35)
	t.right(90)
	t.right(30)
	t.pendown()
	
def goToOddLine():
	goToEvenLine()
	t.penup()
	t.forward(25)
	t.left(60)
	t.forward(25)
	t.right(60)
	t.pendown()
	
def checkText(msgToEncode):
	for letter in msgToEncode:
		#Uppercase is in ASCII range, lowercase isn't
		letter = letter.upper()
		#Space = 32, Underscore = 95: Alphabet, numbers, and symbols in-between
		#if (ord(letter) < 32 || ord(letter) > 95):
		if not (32 <= ord(letter) <= 95):
			print letter + "'s ASCII number, " + str(ord(letter)) + " is not between 32 and 95"
			sys.exit()

def encode(msgToEncode):
	binaryMsg = []
	checkText(msgToEncode)
	for letter in msgToEncode:
		asciiLetter = ord(letter.upper())-32
		correctedBinaryLetter = bin(asciiLetter)[2:]
		strBinaryLetter = str(correctedBinaryLetter)
		binaryMsg.append(strBinaryLetter.zfill(6))
	return binaryMsg
	
def printHexes(binaryMsg):
	goToStart()
	#To work with each side of the hexagon
	letterSide = 0
	#To determine number of characters this line
	charsThisLine = 0
	lastLineEven = True
	for letter in binaryMsg:
		printSides = [int(x) for x in letter]
		printHexagon(printSides)
		charsThisLine = charsThisLine + 1
		if not (charsThisLine % 11 == 0):
			goToNextHex()
		if (charsThisLine % 11 == 0):
			goToNextHex()
			if (lastLineEven):
				print "Going to Odd line"
				goToOddLine()
				lastLineEven = False
			else:
				print "Going to Even Line"
				goToEvenLine()
				lastLineEven = True
		letterSide = 0
	
def main():
	msgToEncode = raw_input("Enter message to encode: ")
	print "msgToEncode = " + msgToEncode
	binaryMsg = encode(msgToEncode)
	printHexes(binaryMsg)

	raw_input("Enter to Quit.")

main()