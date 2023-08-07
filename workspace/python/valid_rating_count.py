#!/usr/bin/env python3
import csv
import sys


def main():
    # Dict to store output
    data = dict()

    with open(sys.argv[1], newline='', encoding='utf-8-sig') as csvfile:
        # DictReader to read csv data with header
        csvreader = csv.DictReader(csvfile)
        
        for record in csvreader:
            if (float(record['score']) - 1) <= float(record['my_score']) <= (float(record['score']) + 1) and (int(record['scored_by']) >= 1000):
                key = "{}\t{}".format(record['user_id'], record['username'])

                if key in data:
                    data[key] +=1
                else:
                    data[key] = 1
        
        for key in data:
            sys.stdout.write("{}\t{}".format(key,data[key]) + '\n')

if __name__ == "__main__":
    main()

