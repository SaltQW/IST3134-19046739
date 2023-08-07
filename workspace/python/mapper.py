#!/usr/bin/env python3
import sys

for line in sys.stdin:

	line = line.strip()
	record = line.split(',')

	try:
		if (float(record[8]) - 1) <= float(record[2]) <= (float(record[8])+1) and (int(record[9]) >= 1000):
			print('{}\t{}\t{}'.format(record[3], record[0], 1))
	except ValueError:
		continue
