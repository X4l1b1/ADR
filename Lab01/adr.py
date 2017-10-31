import csv
import sys
with open('log.csv', 'rb') as csvfile:
	with open('result.txt', 'w') as f:
		freader = csv.reader(csvfile, delimiter = ",", quotechar='|')

		array = [[row[0], int(row[15]), int(row[16]), int(row[9])] for row in freader]

# Hypothese : colonne 9 : LSB et colonne 10 : MSB --> 16 bits lumiere : [10-9]

		i = 0
		mean = 0
		max_light = 0
		max_time = 0
		max_nodeid = 0
		min_light = sys.maxint
		min_time = 0
		min_nodeid = 0
		temp = 0

		array.pop(0) # Pops first line (column name)
		for row in array:
			temp = row[2]*16*16 + row[1]
			mean += temp
			if temp > max_light:
				max_light = temp
				max_time = row[0]
				max_nodeid = row[3]
			if temp < min_light:
				min_light = temp
				min_time = row[0]
				min_nodeid = row[3]
			i+=1
		mean /= i
		print >> f,('Mean light : ' + repr(mean))
		print >> f,('Maximum light : ' + repr(max_light) + ' at ' + max_time + ' (node ' + repr(max_nodeid) + ')')
		print >> f,('Minimum light : ' + repr(min_light) + ' at ' + min_time + ' (node ' + repr(min_nodeid) + ')')
