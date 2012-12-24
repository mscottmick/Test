#!/usr/bin/env python
import itertools
import csv
afile = open('password.csv', 'r')
csvReader1 = csv.reader(afile)


#for row in itertools.islice(csvReader1, 2):
   # print (row)

for line_number, row in zip(range(2), csvReader1):
    print (row)
