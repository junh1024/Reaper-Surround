#add HW send 3/4

import re, sys,string

in_file=sys.argv[1]
 	
read_file = open(in_file).readlines()


# insertionpoint = re.compile(r'^.*MASTER_NCH.*$')
insertionpoint = re.compile(r'^.*MASTER_NCH.*$')

write_file = open(in_file+"_S.RPP", "w") 


for line in read_file:
	
	m1 = insertionpoint.search(line)
	# m2 = fileInProjPat.search(line)
	if m1:
		line= " MASTERHWOUT 2 0 1.00000000000000 0.00000000000000 0 0 2 -1.00000000000000\r\n" + line
	
	write_file.write(line)
	# print("working")
	# 
write_file.close
# input("Press Enter to continue...")
