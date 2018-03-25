import random


answerlist = ["A","B","C","D", "Correct"]


i = 0 
while i < 15:
	f = (random.choice(list(open('test.txt'))))
	lines = f.split('[')
	question = lines[0]
	answers = lines[1].strip("\n").split(',')

	print question
	print 'A: ' + answers[0]
	print 'B: ' + answers[1]
	print 'C: ' + answers[2]
	print 'D: ' + answers[3]

	#assigning values to answers

	answerdict = {
	'A' : answers[0],
	'B' : answers[1],
	'C' : answers[2],
	'D' : answers[3],

	}
	print answers[4]
	select = raw_input("Select your answer:\n")
	select = select.upper()

	if select in answerdict:
		if answerdict[select] == answers[4]:
			print 'Correct' 
		else:
			print 'Hard luck, Game over'
			break
	i = i + 1
