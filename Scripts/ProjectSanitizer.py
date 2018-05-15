#python3

import re, sys,string

in_file=sys.argv[1]
 	
read_file = open(in_file).readlines()


nameInProjPat = re.compile(r'(.*)("C:\\Users\\.*\\)(.*".*)$')

write_file = open(in_file+"_S.RPP", "w") 


for line in read_file:
	
	m1 = nameInProjPat.search(line)
	# m2 = fileInProjPat.search(line)
	if m1:
		line=m1.group(1)+'"' +m1.group(3)+"\r\n"
	
	write_file.write(line)
	# print("working")
	# 
write_file.close
input("Press Enter to continue...")