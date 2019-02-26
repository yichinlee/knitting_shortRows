import knitout
k = knitout.writer('1 2 3 4')
k.addHeadder("Machine", "swg")
carrier = '1'
k.inhook(carrier)


def shortRowsTest():

	knitWidth = 40
	#castOn
	for i in range(knitWidth-1, 0, -2):
		k.tuck('-', ('f',i), carrier)
	writer.releasehook(carrier)
	for i in range(0, knitWidth, 2):
		k.tuck('+', ('f',i),carrier)
	
	#normalKnit
	knitHeight = 10
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(knitWidth-1, 0, -1):
				writer.knit('-', ('f', i), carrier)
		else:
			for i in range(0, knitWidth):
				writer.knit('+', ('f', i), carrier)
	#shortRows
	knitHeight = 15
	lower = 0
	upper = knitWidth / 2
	#leftShortRows
	for i in range (lower, upper):
		if row % 2 == 0:
			for i in range(upper-1,lower, -1):
				file.write("knit -" + " f" + str(i) + " " + Carriers + "\n")
		if row % 2 == 1:
			for i in range(lower, upper, 1):
				file.write("knit +" + " f" + str(i) + " " + Carriers + "\n")
		lower += 1
		upper -+ 1
	
	#rightShortRows
	lower = knitWidth / 2
	upper = knitWidth
	for i in range (lower, upper):
		if row % 2 == 0:
			for i in range(upper-1,lower, -1):
				file.write("knit -" + " f" + str(i) + " " + Carriers + "\n")
		if row % 2 == 1:
			for i in range(lower, upper, 1):
				file.write("knit +" + " f" + str(i) + " " + Carriers + "\n")
		lower += 1
		upper -+ 1

	#normalKnit
	knitHeight = 10
	for j in range(0, knitHeight):
		if j%2 == 0:
			for i in range(knitWidth-1, 0, -1):
				writer.knit('-', ('f', i), carrier)
			else:
				for i in range(0, knitWidth):
					writer.knit('+', ('f', i), carrier)

	writer.outhook(carrier)
	for i in range(0, knitWidth):
		writer.drop(('f', i))
	
	writer.write('shortRowsTest-'+'.k')
	
shortRowsTest()









