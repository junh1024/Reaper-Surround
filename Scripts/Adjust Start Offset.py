desc=""
by="junh1024"

from reaper_python import *
from contextlib import contextmanager

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
	# RPR_ShowConsoleMsg(BPM_proj)
	
	#get file BPM
	dialogstring="amount"
	theoffset = RPR_GetUserInputs("Adjust take by how much secs",1,dialogstring,"",64)[4]
	theoffset = float(theoffset.strip())
	# RPR_ShowConsoleMsg(new_gain_bits)
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
	
		# set gain
		take=RPR_GetActiveTake(MI)
		original=RPR_GetMediaItemTakeInfo_Value( take, "D_STARTOFFS" )
		RPR_SetMediaItemTakeInfo_Value( take, "D_STARTOFFS", original+ theoffset  )
		 
