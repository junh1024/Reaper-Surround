#convert restream surround routing to parent channel

from reaper_python import *
from sws_python import *
from contextlib import contextmanager
# import os

@contextmanager
def undoable(message):
	RPR_Undo_BeginBlock2(0)
	try:
		yield
	finally:
		RPR_Undo_EndBlock2(0, message, -1)

debug = True #disable for using

def msg(m):
	if 'debug' in globals():
		RPR_ShowConsoleMsg(m)

with undoable("Set Pan According To Track Suffix"):
	# for i in range(RPR_CountTracks(0)): #for all tracks, get track
		# trackId = RPR_GetTrack(0, i)

	for i in range(RPR_CountSelectedTracks(0)): #for selected tracks, get track
		trackId = RPR_GetSelectedTrack(0, i)
		fxname= "ReaStream"
		fxId=RPR_TrackFX_GetByName( trackId, fxname, False )
		# RPR_ShowConsoleMsg(fxId)
		# fxId=RPR_TrackFX_AddByName( trackId, fxname, false, 0 )
		SNM_MoveOrRemoveTrackFX( trackId, fxId, 0 )
		RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 4) #set 5-6 parent ch
		RPR_SetMediaTrackInfo_Value(trackId, "I_NCHAN", 2) # set to stereo


		 

