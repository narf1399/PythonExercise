# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:20:36 2016

How to read data from a file

@author: Tim Metzler
"""

import csv
import pandas

# With csv
with open('myData.csv', 'rb') as csvfile:
    myDataReader = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    for row in myDataReader:
        print ", ".join(row)
    
print "\n\n"

# Same with pandas
y = pandas.read_csv('myData.csv')
print y
myList = []
myList = y.as_matrix()

print "\n", myList


