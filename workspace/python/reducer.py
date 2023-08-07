#!/usr/bin/env python3
import sys

current_user = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	# Split input from Mapper into key pairs by splitting the last tab 
	user, count = line.rsplit('\t', 1) 

	try:
		count = int(count)
	except ValueError:
		continue

	if current_user == user:
		current_count += count
	else:
		if current_user:
			print("{}\t{}".format(current_user, current_count))
		current_count = count
		current_user = user

if current_user == user:
	print("{}\t{}".format(current_user, current_count))
