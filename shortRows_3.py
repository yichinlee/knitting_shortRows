import string
import numpy as np

#short rows curving opposit side
file = open("/Users/mac/Desktop/knitting_project/knitting/shortRows_3.k", "w")	
#file = open("shortRows.k", "w")	


Carriers = "6"
knitWidth = 30

#10 going up
#10 going down

def castOn(totalWidth):
	for i in range (totalWidth,-1,-2):
		file.write("tuck -" + " f" + str(i) + " " + Carriers + "\n")
	for i in range(1,totalWidth,2):
		file.write("tuck +" + " f" + str(i) + " " + Carriers + "\n")


def knit(totalWidth):
	for i in range(totalWidth,-1,-1):
		file.write("knit -" + " f" + str(i) + " " + Carriers + "\n")
	for i in range(totalWidth+1):
		file.write("knit +" + " f" + str(i) + " " + Carriers + "\n")



def shortRows(totalWidth,numShortRow):
	upper = totalWidth
	lower = 0

	for row in range(numShortRow):
		
			if row % 2 == 0:
				for i in range(upper,lower-1,-1):
					file.write("knit -" + " f" + str(i) + " " + Carriers + "\n")
			if row % 2 == 1:
				for i in range(lower,upper):
					file.write("knit +" + " f" + str(i) + " " + Carriers + "\n")
			
			if row <= numShortRow/2:
				upper -= 1
				lower += 1
				print(upper, lower)
			else:
				upper += 1
				lower -= 1
				print(upper, lower)




#execute the function
#header
file.write(";!knitout-2\n")
file.write(";;Carriers: 6\n")
file.write("inhook 6\n")
#file.write("x-stitch-number 96\r\n")	
#control the stitch tension

castOn(knitWidth)
file.write("releasehook " + Carriers + "\n")

#normal knit
knitRows = 10
for r in range(knitRows):
	knit(knitWidth)
#style knit - short rows
numShortRow = 20
shortRows(knitWidth,numShortRow)

knitRows = 10
for r in range(knitRows):
	knit(knitWidth)

numShortRow = 30
shortRows(knitWidth,numShortRow)

knitRows = 10
for r in range(knitRows):
	knit(knitWidth)

numShortRow = 20
shortRows(knitWidth,numShortRow)

knitRows = 10
for r in range(knitRows):
	knit(knitWidth)
	
#end
file.write("outhook " + Carriers + "\n")

