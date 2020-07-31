desc="Batch round BPM of clips"
by="junh1024"

from reaper_python import *
from contextlib import contextmanager
from math import floor

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
	
	BPM_proj=RPR_GetProjectTimeSignature2(-1,0,0)[1]
	
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		take=RPR_GetActiveTake(MI)

		rate_file=RPR_GetMediaItemTakeInfo_Value( take, "D_PLAYRATE" )
		if rate_file == 0:
			continue
		
		#compute BPM of item
		BPM_file=BPM_proj/rate_file
		
		#round to nearest number
		BPM_file=floor(BPM_file+0.2)

		# set playrate
		RPR_SetMediaItemTakeInfo_Value( take, "D_PLAYRATE", BPM_proj/BPM_file )
		 
