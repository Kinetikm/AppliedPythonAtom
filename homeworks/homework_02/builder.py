import sys

def printUnderline(underlines):
	for i in range(underlines):
		sys.stdout.write('_')

def buildTSVTable(input_data, revert):
	tableSize = len(input_data[0])
	underlines = 1
	maxLen = []
	if input_data[-1] == ['']:
		input_data.pop()
	for item in input_data[0]:
		maxLen.append(len(item))
		underlines += (len(item) + 5)
	for row in input_data:
		if len(row) != tableSize:
			return False
		for i in range(len(row)):
			item = str(row[i])
			if len(item) > maxLen[i]:
				underlines += (len(item) - maxLen[i])
				maxLen[i] = len(item)
	printUnderline(underlines)
	print()
	for i in range(len(input_data[0])):
		item = str(input_data[0][i])
		sys.stdout.write('|  ')
		for k in range((maxLen[i] - len(item))//2):
			sys.stdout.write(' ')
		sys.stdout.write(item)
		for k in range((maxLen[i] - len(item))//2 + 2):
			sys.stdout.write(' ')
	print('|')
	for k in range(1, len(input_data)):
		row = input_data[k]
		for i in range(len(row)):
			try:
				revert.index(i + 1)
				sys.stdout.write('|')
				for j in range(maxLen[i] - len(row[i]) + 2):
					sys.stdout.write(' ')
				sys.stdout.write(row[i] + '  ')
			except ValueError:
				sys.stdout.write('|  ' + row[i])
				for j in range(maxLen[i] - len(row[i]) + 2):
					sys.stdout.write(' ')
		print('|')
	printUnderline(underlines)

def buildJSONTable(input_data, revert):
	tableSize = len(input_data[0])
	underlines = 1
	maxLen = {}	
	for key in input_data[0]:
		maxLen[key] = len(key)
		underlines += (maxLen[key] + 5) 
	for obj in input_data:
		if len(obj) != tableSize:
			return False
		for key in obj:
			obj[key] = str(obj[key])
			try:
				if len(obj[key]) > maxLen[key]:
					underlines += (len(obj[key]) - maxLen[key])
					maxLen[key] = len(obj[key])
			except KeyError:
				return False
	printUnderline(underlines)
	print()
	for key in input_data[0]:
		sys.stdout.write('|  ')
		for i in range((maxLen[key] - len(key))//2):
			sys.stdout.write(' ')
		sys.stdout.write(key)
		for i in range((maxLen[key] - len(key))//2 + 2):
			sys.stdout.write(' ')
	print('|')
	for row in input_data:
		for key in row:
			try:
				revert.index(key)
				sys.stdout.write('|')
				for i in range(maxLen[key] - len(row[key]) + 2):
					sys.stdout.write(' ')
				sys.stdout.write(row[key] + '  ')
			except ValueError:
				sys.stdout.write('|  ' + row[key])
				for i in range(maxLen[key] - len(row[key]) + 2):
					sys.stdout.write(' ')
		print('|')
	printUnderline(underlines)
