desc="Batch set BPM of clips, sequentially"
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
	#get project BPM
	
	BPM_proj=RPR_GetProjectTimeSignature2(-1,0,0)[1]
	
	#get file BPM
	# RPR_ShowConsoleMsg(BPM_file)
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		take=RPR_GetActiveTake(MI)
		takename= RPR_GetTakeName( take )
		
		#set timebase to beats+L
		RPR_SetMediaItemInfo_Value(MI, "C_BEATATTACHMODE", 1)
		
		# get length
		item_len = RPR_GetMediaItemInfo_Value(MI, "D_LENGTH")

		BPM_file = RPR_GetUserInputs(takename,1,"What is the BPM of this item?","",64)[4]
		BPM_file = float(BPM_file.strip())

		
		# set length
		RPR_SetMediaItemInfo_Value(MI, "D_LENGTH", item_len*BPM_file/BPM_proj)
		# set playrate
		RPR_SetMediaItemTakeInfo_Value( take, "D_PLAYRATE", BPM_proj/BPM_file )
		 
