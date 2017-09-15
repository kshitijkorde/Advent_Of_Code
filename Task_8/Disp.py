#!/usr/bin/python

import re

pattern = '.+=(\d+)\s+.+?(\d+)'  # rotate row y=0 by 5 # rotate row y=10 by 10
pattern_dimension = '.+\s+(\d+)x(\d+)' # rect 19x3
prog = re.compile(pattern)
prog_dimen = re.compile(pattern_dimension)

screen = [[0]*50 for i in range(6)]

with open("input.txt") as fobj:
	for line in fobj:
		#print line
		cmds = line.split()
		if(cmds[0] == "rect"):
			result = prog_dimen.match(line)
			row = int(result.group(2))
			col = int(result.group(1))
			for r in range(row):
				for c in range(col):
					screen[r][c] = 1
		else:
			result = prog.match(line)
			no = int(result.group(1))
			shift = int(result.group(2))
			if(cmds[1] == "row"):
				#print "Row No:"+str(no) 
				#print "Rotate by:"+str(shift)
				screen[no] = screen[no][-shift:]+screen[no][:-shift]
			elif(cmds[1] == "column"):
				#print "Col No:"+str(no) 
				#print "Rotate by:"+str(shift)
				collist = [screen[x][no] for x in range(6)]
				collist = collist[-shift:]+collist[:-shift]
				for r in range(6):
					screen[r][no] = collist[r]

	#	for element in screen:
	#		print element
	#	k = raw_input()
	

cnt = 0
for r in range(6):
	for c in range(50):
		if(screen[r][c] == 1):
			cnt+=1

print cnt
