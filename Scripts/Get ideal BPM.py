desc="Get selected items weighted BPM"
by="junh1024"

from reaper_python import *
from contextlib import contextmanager

global total_lengths, BPM_file
total_lengths=0
global total_rates
total_rate=0

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
	#get project BPM
	
	# https://forum.cockos.com/showthread.php?t=46432
	# https://github.com/metalmike/ReaScoreMusicXML/blob/master/reascoremusicxml/reascoremusicxml.py
	BPM_proj=RPR_GetProjectTimeSignature2(-1,0,0)[1]
	# RPR_ShowConsoleMsg(BPM_proj)
	
	#get file BPM
	# BPM_file = RPR_GetUserInputs("BPM",1,"What is the BPM of this item?","",64)[4]
	# BPM_file = float(BPM_file.strip())
	# RPR_ShowConsoleMsg(BPM_file)
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		
		
		# get length
		item_len = RPR_GetMediaItemInfo_Value(MI, "D_LENGTH")
		length_file=item_len
	# compute length
		# adjusted_length=item_len*1/
		
		# set length
		# RPR_SetMediaItemInfo_Value(MI, "D_LENGTH", item_len*BPM_file/BPM_proj)
		# set playrate
		# MediaItem_Take*  RPR_GetMediaItemTakeInfo_Value( take, parmname )(MediaItem* item, int tk )
		take=RPR_GetActiveTake(MI)
		# RPR_ShowConsoleMsg(RPR_GetMediaItemTakeInfo_Value( MI, "B_MUTE"))
		if (RPR_GetMediaItemInfo_Value( MI, "B_MUTE"))== False : 
		#calculate weighted BPM

			
			rate_file=RPR_GetMediaItemTakeInfo_Value( take, "D_RATE" )
			if rate_file == 0:
				continue
			# length_file=RPR_GetMediaItemTakeInfo_Value( take, "D_LENGTH" )
			pitch_file=RPR_GetMediaItemTakeInfo_Value( take, "D_PITCH" )
			
			BPM_file=BPM_proj/rate_file
			
			total_pitches+=pitch_file*length_file
			total_lengths+=length_file
	avg_pitch=total_pitches/total_lengths
	ideal_rate=1+(1.06^avg_pitch) # 12th root of 2
	ideal_bpm=BPM_file*ideal_rate
	RPR_ShowConsoleMsg(str(ideal_bpm) + "\n")
	

