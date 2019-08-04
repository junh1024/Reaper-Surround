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
	dialogstring="0=unity, 1=6dB, 2=12dB"
	new_gain_bits = RPR_GetUserInputs("Set this take to what bits gain?",1,dialogstring,"",64)[4]
	new_gain_bits = int(new_gain_bits.strip())
	# RPR_ShowConsoleMsg(new_gain_bits)
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
	
		# set gain
		take=RPR_GetActiveTake(MI)
		RPR_SetMediaItemTakeInfo_Value( take, "D_VOL", 2**new_gain_bits )
		 
