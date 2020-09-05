desc="requires Reaper 5+ & SWS"
by="junh1024"

from reaper_python import *
from sws_python import *
from contextlib import contextmanager
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

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
		
		pcm_source=RPR_GetMediaItemTake_Source( take )

		filesize=0
		fullPath = str(RPR_GetMediaSourceFileName(pcm_source, "", 512)[1])
		
		audio=FLAC(fullPath)
		key_string=list(audio["comment"])[0]
		
		# RPR_ShowConsoleMsg(key_string)
		
		
		#set timebase to beats+L
		RPR_SetMediaItemInfo_Value(MI, "C_BEATATTACHMODE", 1)
		
		# get length
		item_len = RPR_GetMediaItemInfo_Value(MI, "D_LENGTH")
		item_pos = RPR_GetMediaItemInfo_Value(MI, "D_POSITION")
		
		
		# the_track = RPR_GetMediaItemTrack( MI )
		the_track =  RPR_GetSelectedTrack( 0, 0 )
		
		#make a new text item on selected track with key from comment of file
		key_text_item = RPR_AddMediaItemToTrack(the_track)
		RPR_SetMediaItemInfo_Value(key_text_item, "D_POSITION", item_pos+10)
		RPR_SetMediaItemInfo_Value(key_text_item, "D_LENGTH", item_len*.9)
		ULT_SetMediaItemNote(key_text_item, key_string)
		BR_SetMediaItemImageResource( key_text_item, "", 2 ) #stretch to fit, doesn't work
		
		#group items
		RPR_SetMediaItemInfo_Value(			MI,		"I_GROUPID",i+1)
		RPR_SetMediaItemInfo_Value(key_text_item,	"I_GROUPID",i+1)		
		
"""
		BPM_file = RPR_GetUserInputs(takename,1,"What is the BPM of this item?","",64)[4]
		BPM_file = float(BPM_file.strip())

		
		# set length
		RPR_SetMediaItemInfo_Value(MI, "D_LENGTH", item_len*BPM_file/BPM_proj)
		# set playrate
		RPR_SetMediaItemTakeInfo_Value( take, "D_PLAYRATE", BPM_proj/BPM_file )
		 """
