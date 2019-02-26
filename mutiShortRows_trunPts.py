import knitout
knitWidth = 30
knitHeight = 50
trunningPts = []

def normalKnit(knitHeight):
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(knitWidth-1, 0, -1):
				k2.knit('-', ('f', i), carrier)
		else:
			for i in range(0, knitWidth):
				k2.knit('+', ('f', i), carrier)

def bump(leftMost,rightMost,bumpHeight):
	
	for i in range (bumpHeight):
		if i < bumpHeight/2:
			trunningPts.append((leftMost,rightMost))
			trunningPts.append((rightMost,leftMost))
			leftMost += 1
			rightMost -= 1
		else:
			leftMost -= 1
			rightMost += 1
			trunningPts.append((leftMost,rightMost))
			trunningPts.append((rightMost,leftMost))
			

def turnningPts():
	bump(10,30,16)
	bump(10,20,10)	
	bump(20,30,10)
	bump(10,30,16)
	print(trunningPts)
	return 42

def shortRows():
	print(len(trunningPts))
	#for row in range 




turnningPts()
shortRows()
		






