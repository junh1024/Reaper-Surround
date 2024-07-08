desc="Get item start timecodes for mix tracklist"
by="junh1024"

from reaper_python import *
from contextlib import contextmanager

# fast string building https://waymoot.org/home/python_string/
from io import StringIO
file_str = StringIO()

# https://stackoverflow.com/a/24507708 convert seconds to HMS
from time import strftime, gmtime

# https://stackoverflow.com/a/44144136 get filename w/o ext

@contextmanager
def undoable(message):
	RPR_Undo_BeginBlock2(0)
	try:
		yield
	finally:
		RPR_Undo_EndBlock2(0, message, -1)

debug = True

def msg(m):
	if 'debug' in globals():
		RPR_ShowConsoleMsg(m)

# msg(RPR_CountSelectedMediaItems(0))
		
with undoable(desc):
	
	my_dict = {}
	
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		
		take_name = None
		item_pos = None
		item_pos_in_my_dict = None
		item_pos = RPR_GetMediaItemInfo_Value(MI, "D_POSITION")
		
		# set start time for songs almost at the start to 0
		if item_pos <=5:
			item_pos = 0
		
		try:
			take=RPR_GetActiveTake(MI)
			take_name=RPR_GetTakeName( take ).rsplit('.', maxsplit=1)[0] # w/o ext
		except:
			# not a media
			continue

		# if not muted
		if (RPR_GetMediaItemInfo_Value( MI, "B_MUTE"))== True :
			continue
		
		# check if take is MIDI https://forums.cockos.com/showthread.php?t=254697
		# skip MIDI takes
		# if "MIDI" in take_name:
			# continue
		if RPR_TakeIsMIDI(take):
			continue
		
		# if song not in my_dict
		if take_name not in my_dict:
			# RPR_ShowConsoleMsg("can add")
			my_dict.update({take_name:item_pos})
			continue
		
		
		# if current item pos is earlier than one in my_dict, update it
		item_pos_in_my_dict=my_dict.get(take_name)
		if item_pos<item_pos_in_my_dict  :
			my_dict.update({take_name:item_pos})
		
	# sort songs by start time with python 3.7
	# https://stackoverflow.com/questions/613183/how-do-i-sort-a-my_dictionary-by-value
	my_dict=dict(sorted(my_dict.items(), key=lambda item: item[1]))
	
	# set time of 1st song to 0
	# my_dict.update({my_dict.items()[0][0]:0})
	
	# put timecodes & filenames into string

	n=1
	for name, time in my_dict.items():
		# file_str.write(str(n)+'. '+strftime("%M:%S", gmtime(time)) +' '+name+'\r\n')
		file_str.write(strftime("%M:%S", gmtime(time)) +' '+name+'\r\n')
		n+=1
		
	RPR_ShowConsoleMsg(file_str.getvalue())
