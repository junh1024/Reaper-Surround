#add HW send 3/4,7/8, master 16ch

import sys,string

in_file=sys.argv[1]
out34=False
out78=False
Master_ch_line_index=0;


with open(in_file,'r') as file:
	lines = file.readlines()

for index, line in enumerate(lines):
	line=line.lstrip(' ')
	lines[index]=line #strip leading spaces
	if line.startswith("MASTERHWOUT 2 0"):
		out34=True
	if line.startswith("MASTERHWOUT 6 0"):
		out78=True

	# if line.startswith("""<JS "Surround/7.1 Stereo panner"""):
		# lines[index]="""<JS "Surround/7.1 Mono panner.txt" "" \n"""
	
	if line.startswith("MASTER_NCH"):
		Master_ch_line_index=index
		lines[index]="MASTER_NCH 16 2\n"
		

if not out34:
	lines.insert(Master_ch_line_index,"MASTERHWOUT 2 0 1 0 0 0 2 -1\n")

if not out78:
	lines.insert(Master_ch_line_index,"MASTERHWOUT 6 0 1 0 0 0 6 -1\n")


with open(in_file, "w")  as file:
	file.write(''.join(lines))

# input("waiting...")