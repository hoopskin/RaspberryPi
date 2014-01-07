def file2list(fileObj):
	dataList = []
	for line in fileObj:
		line = line.strip()
		line = line.split(',')
		dataList.append(line)
	return dataList

def main():
	preSweaterSmall = 0
	preSweaterMedium = 0
	preSweaterLarge = 0
	preSweaterXL = 0
	preSweater2XL = 0
	preHat = 0
	preMittens = 0
	preShipping = 0
	unpSweaterSmall = 0
	unpSweaterMedium = 0
	unpSweaterLarge = 0
	unpSweaterXL = 0
	unpSweater2XL = 0
	unpHat = 0
	unpMittens = 0
	unpShipping = 0

	fileObj = open('GDoc.csv', 'rU')
	
	# Read file, strip lines, split lines on commas, create list of lists or tuples, etc.
	dataList = file2list(fileObj)
	print "PREORDER Orders"
	for Name, Item, Quantity, Price, Status, OrderNum, PhoneNum, Notes, b1, b2, b3, b4, b5 in dataList:
		print "\"" + Item + "\""
		if Status == "PREORDER":
			#print Name + " | " + Item + " | " + Quantity + " | " + OrderNum + " | " + PhoneNum + " | " + Notes
			if Item == "Sweater - S":
				preSweaterSmall += int(Quantity)
			elif Item == "Sweater - M":
				preSweaterMedium += int(Quantity)
			elif Item == "Sweater - L":
				preSweaterLarge += int(Quantity)
			elif Item == "Sweater - XL":
				preSweaterXL += int(Quantity)
			elif Item == "Sweater - 2XL":
				preSweater2XL += int(Quantity)
			elif Item == "Hat":
				preHat += int(Quantity)
			elif Item == "Mittens":
				preMittens += int(Quantity)
			elif Item == "Shipping":
				preShipping += int(Quantity)
			else:
				print "ERROR: " + Item
	print "PREORDER Totals"
	print """S: %d M: %d L: %d XL: %d 2XL: %d Hat: %d Mittens: %d Shipping: %d""" % (preSweaterSmall, preSweaterMedium, preSweaterLarge, preSweaterXL, preSweater2XL, preHat, preMittens, preShipping)
	print
	print "UNPAID Orders"
	for Name, Item, Quantity, Price, Status, OrderNum, PhoneNum, Notes, b1, b2, b3, b4, b5 in dataList:
		if Status == "UNPAID":
			#print Name + " | " + Item + " | " + Quantity + " | " + OrderNum + " | " + PhoneNum + " | " + Notes
			if Item == "Sweater - S":
				unpSweaterSmall += int(Quantity)
			elif Item == "Sweater - M":
				unpSweaterMedium += int(Quantity)
			elif Item == "Sweater - L":
				unpSweaterLarge += int(Quantity)
			elif Item == "Sweater - XL":
				unpSweaterXL += int(Quantity)
			elif Item == "Sweater - 2XL":
				unpSweater2XL += int(Quantity)
			elif Item == "Hat":
				unpHat += int(Quantity)
			elif Item == "Mittens":
				unpMittens += int(Quantity)
			elif Item == "Shipping":
				unpShipping += int(Quantity)
			else:
				print "ERROR: " + Item
	print "UNPAID Totals"
	print """S: %d M: %d L: %d XL: %d 2XL: %d Hat: %d Mittens: %d Shipping: %d""" % (unpSweaterSmall, unpSweaterMedium, unpSweaterLarge, unpSweaterXL, unpSweater2XL, unpHat, unpMittens, unpShipping)
	print

main()	