#add HW send 3/4

import re, sys,string

in_file=sys.argv[1]


with open(in_file,'r') as file:
	lines = file.readlines()

# insertionpoint = re.compile(r'^.*MASTER_NCH.*$')
insertionpoint = re.compile(r'^.*MASTER_NCH.*$')


for index, line in enumerate(lines):
	
	m1 = insertionpoint.search(line)
	# m2 = fileInProjPat.search(line)
	if m1:
		lines[index]= " MASTERHWOUT 2 0 1.00000000000000 0.00000000000000 0 0 2 -1.00000000000000\n" + line


with open(in_file, "w")  as file:
	file.write(''.join(lines))

# input("waiting...")