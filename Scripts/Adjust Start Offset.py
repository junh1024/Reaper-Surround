desc="Adjust item start offset"
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
	
	multiply=None
	
	#get desired offset
	ds="Adjust by secs (* to multiply)"
	theoffset = RPR_GetUserInputs("Adjust Start Offset",1,ds,"",64)[4]
	
	#account for multiply, and trim off star
	if theoffset[0]=='*':
		multiply=True
		theoffset=theoffset[1:]
	theoffset = float(theoffset.strip())

	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
	
		# get original offset
		take=RPR_GetActiveTake(MI)
		original=RPR_GetMediaItemTakeInfo_Value( take, "D_STARTOFFS" )
		
		# could use reflection, but more insecure
		if multiply:
			RPR_SetMediaItemTakeInfo_Value( take, "D_STARTOFFS", original* theoffset  )
		else:
			RPR_SetMediaItemTakeInfo_Value( take, "D_STARTOFFS", original+ theoffset  )
		 
