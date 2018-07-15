desc="Set (selected) item start to position. Useful for say, converting items from recorded dialog timings to a rendered dialog stem"
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
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		take= RPR_GetTake( MI, 0 )
		#Set take "start in source" to item position
		RPR_SetMediaItemTakeInfo_Value( take, "D_STARTOFFS", RPR_GetMediaItemInfo_Value(MI, "D_POSITION") )