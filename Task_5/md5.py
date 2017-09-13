#!/usr/bin/python
# http://adventofcode.com/2016/day/5
import hashlib
import re
index = 0
prog = re.compile('^00000(.)');
passwd = ""
cnt = 0
while 1:
	md5str = hashlib.md5("ffykfhsq"+str(index)).hexdigest()
	result = prog.match(md5str);
	if result:
		passwd = passwd+result.group(1)
		cnt = cnt + 1 
		if cnt == 8:
			break
	index = index + 1

print passwd
