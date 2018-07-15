desc="Delete (selected) item fades under threshold. Threshold is fixed."
by="junh1024"

from reaper_python import *
from contextlib import contextmanager

threshold=0.02 #20ms

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
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		
		#If fades are < threshold, set to 0s
		if(RPR_GetMediaItemInfo_Value(MI, "D_FADEINLEN")  < threshold ):
			RPR_SetMediaItemInfo_Value(MI,"D_FADEINLEN",0)
	
		if(RPR_GetMediaItemInfo_Value(MI, "D_FADEOUTLEN") < threshold ):
			RPR_SetMediaItemInfo_Value(MI,"D_FADEOUTLEN",0)
