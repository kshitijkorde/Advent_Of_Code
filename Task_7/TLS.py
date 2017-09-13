#!/usr/bin/python
# https://adventofcode.com/2016/day/7
import re

f = open("input.txt")
cnt = 0

def checkABBA(string):
	if(string[0] == '['):
		string = string[1:]
		string = string[:-1]

	if(len(string) >= 4):
		for pos in range(0, len(string)-3):
			token = string[pos:pos+4]	
			if(token[0] == token[3] and token[1] == token[2] and token[0] != token[1]):
				return 1
	return 0

	
for line in f.readlines():
	result = re.findall(r'\[\w+\]+',line)
	if result:
		stillvalid = 1 
		for token in result:
			if(checkABBA(token) == 1):
				stillvalid = 0; break

		if stillvalid == 1:
			line = re.sub(r'\[\w+\]','$', line)
			if(checkABBA(line) == 1):
				cnt += 1
print cnt	
