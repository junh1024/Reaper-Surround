# junh1024 and AI to make codes
# external python script to turn a VideoReDo project file to a markers file for REAPER DAW
# of selected video scenes

import sys



import xml.etree.ElementTree as ET
from datetime import datetime

divisor=10000000

def parse_xml(file_path):
	tree = ET.parse(file_path)
	root = tree.getroot()

	times = []
	
	First=True
	
	for cut in root.findall('.//cut'):

		# VRD vprj format stores the timecodes of the cuts we don't want, so we ignore the 1st timecode
		if First == False:
			CutTimeStart = float(cut.find('CutTimeStart').text)/divisor
			times.append(CutTimeStart)
			# print('start\n')
		
		# Thereafter, we put the timecodes in a list
		CutTimeEnd = float(cut.find('CutTimeEnd').text)/divisor
		times.append(CutTimeEnd)
		# print('end\n')
		First = False

	return times

def calculate_time_differences(times):
	differences = []
	
	
	the_range= int ( ( len(times)-1  ) /2 )
	# print(type(the_range))
	
	i=0
	for i in range(0, the_range  ):
		
		# pairs of times form scenes, of which we are interested in the length
		time_difference = times[i*2+1]-times[i*2]
		
		if i>0:
			cumulative_time_difference=time_difference+differences[i-1]
		else:
			cumulative_time_difference=time_difference
		
		differences.append(cumulative_time_difference)
		
		i+=1

	return differences

if __name__ == "__main__":
	file = sys.argv[1]
	times = parse_xml(file)
	differences = calculate_time_differences(times)
	
	# Finally, write the times to a file
	csv_file = open(file[0:-5]+'_cuts.csv', 'w')
	csv_file.write('#,Name,Start,End,Length\r\n')

	
	i=2
	for diff in differences:
		
		print(diff)
		csv_file.write('M'+str(i) +',,'+str(diff)+'\n')
		i+=1
	
	csv_file.close()
	
	
