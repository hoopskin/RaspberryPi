from random import randrange

def RandSign():
	x = randrange(2)
	if x == 0:
		return "*"
	if x == 1:
		return "+"
	if x == 2:
		return "-"

def getAnswer(formula):
	exec "answer = " + formula
	return answer

def checkAnswer(formula, answer):
	userAnsweredCorrectly = False
	while (userAnsweredCorrectly == False):
		print formula
		userAns = int(raw_input("What's the answer? "))
		if userAns == answer:
			userAnsweredCorrectly = True

def main():
	intA = randrange(9)
	signA = RandSign()
	intB = randrange(9)
	signB = RandSign()
	intC = randrange(9)
	formula = str(intA) + signA + str(intB) + signB + str(intC)
	answer = getAnswer(formula)
	checkAnswer(formula, answer)

main()