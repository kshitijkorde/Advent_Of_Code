#!/usr/bin/python 
# https://adventofcode.com/2016/day/6
import string

fp = open("input.txt");
data = fp.readlines()
size = len(data[0].strip())
message = ""
for pos in range(0,size):
	mydict = dict.fromkeys(string.ascii_lowercase, 0)
	for line in data:
		mydict[line[pos]] += 1
	message += max(mydict.iterkeys(), key=(lambda key: mydict[key]))
print message
