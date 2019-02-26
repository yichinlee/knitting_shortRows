import knitout

#making shortrows side by side
def bindOff():
	return 42

def normalKnit(knitHeight):
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(knitWidth-1, 0, -1):
				k2.knit('-', ('f', i), carrier)
		else:
			for i in range(0, knitWidth):
				k2.knit('+', ('f', i), carrier)

def addBump(knitHeight,lower,upper):

	for row in range (lower, upper):
		if row == upper-1:
			for i in range(0,40):
				k.knit('+', ('f', i), carrier)
		else:
			if row % 2 == 0:
				for i in range(upper-1,lower, -1):
					k.knit('-', ('f', i), carrier)
			if row % 2 == 1:
				for i in range(lower, upper, 1):
					k.knit('+', ('f', i), carrier)
		lower += 1
		upper -= 1

def shortRowsTest():
	k = knitout.Writer('1 2 3 4')
	k.addHeader("Machine", "swg")
	carrier = '1'
	k.inhook(carrier)

	knitWidth = 40
	#castOn
	for i in range(knitWidth-1, 0, -2):
		k.tuck('-', ('f',i), carrier)
	k.releasehook(carrier)
	for i in range(0, knitWidth, 2):
		k.tuck('+', ('f',i),carrier)
	
	#normalKnit
	normalKnit(10)
	addBump(20)
	addBump(20)
	#shortRows
	knitHeight = 20
	lower = 0
	upper = knitWidth // 2
	#leftShortRows
	for row in range (lower, upper):
		if row == upper-1:
			for i in range(0,40):
				k.knit('+', ('f', i), carrier)
		else:
			if row % 2 == 0:
				for i in range(upper-1,lower, -1):
					k.knit('-', ('f', i), carrier)
			if row % 2 == 1:
				for i in range(lower, upper, 1):
					k.knit('+', ('f', i), carrier)
		lower += 1
		upper -= 1

	
	#rightShortRows
	lower = knitWidth // 2
	upper = knitWidth
	for row in range (lower, upper):
		if row % 2 == 0:
			for i in range(upper-1,lower, -1):
				k.knit('-', ('f', i), carrier)
		if row % 2 == 1:
			for i in range(lower, upper, 1):
				k.knit('+', ('f', i), carrier)
		lower += 1
		upper -= 1

	#normalKnit
	knitHeight = 10
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(knitWidth-1, 0, -1):
				k.knit('-', ('f', i), carrier)
		else:
			for i in range(0, knitWidth):
				k.knit('+', ('f', i), carrier)

	k.outhook(carrier)
	for i in range(0, knitWidth):
		k.drop(('f', i))
	k.write('doubleShortRows_4_0221'+'.k')
	
#shortRowsTest()

#inverseShortRows
k2 = knitout.Writer('1 2 3 4')
k2.addHeader("Machine", "swg")
carrier = '3'
k2.inhook(carrier)
knitWidth = 50

def addLeft(knitHeight):
	
	lower = 0
	upper = lower + 1
	for j in range(0, knitHeight):
		if j%2 == 1:
			for i in range(upper-1,lower-1, -1):
				k2.knit('-', ('f', i), carrier)
		else:
			for i in range(lower, upper):
				k2.knit('+', ('f', i), carrier)
		upper += 1

	for i in range(upper-1, -1, -1):
		k2.knit('-', ('f', i), carrier)


def addRight(knitHeight):
	
	upper = knitWidth
	lower = upper - 1
	
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(upper-1,lower-1,-1):
				k2.knit('-', ('f', i), carrier)
		else:
			for i in range(lower, upper):
				k2.knit('+', ('f', i), carrier)
		lower -= 1
	
	for i in range(lower, knitWidth, 1):
		k2.knit('+', ('f', i), carrier)

def knitToLeft():
	for i in range(knitWidth-1, -1, -1):
		k2.knit('-', ('f', i), carrier)

def knitToRight():
	
	for i in range(0, knitWidth, 1):
		k2.knit('+', ('f', i), carrier)



def rolling():
	#castOn
	for i in range(knitWidth-1, 0, -2):
		k2.tuck('-', ('f',i), carrier)
	for i in range(0, knitWidth, 2):
		k2.tuck('+', ('f',i),carrier)
	k2.releasehook(carrier)

	
	normalKnit(10)
	knitToLeft()
	addLeft(15)
	knitToRight()
	addRight(35)
	knitToLeft()
	addLeft(25)
	knitToRight()
	addRight(25)
	knitToLeft()
	addLeft(35)
	knitToRight()
	addRight(15)
	normalKnit(10)


	k2.outhook(carrier)
	for i in range(0, knitWidth):
		k2.drop(('f', i))
	k2.write('doubleShortRows_3_0221'+'.k')

rolling()








