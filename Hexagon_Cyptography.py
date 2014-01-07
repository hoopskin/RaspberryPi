def file2list(fileObj):
	dataList = []
	line = line.split(',')
	return dataList

def main():
	fileObj = open('HexagonNumbers.txt', 'rU')
	# Read file, strip lines, split lines on commas, create list of lists or tuples, etc.
	dataList = file2list(fileObj)
	for rawNum in dataList:
		

main()