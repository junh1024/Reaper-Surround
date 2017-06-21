#Some Codes from "Rename tracks to take source filename", -- Set pan for selected track(s) (SPK77)

from reaper_python import *
from contextlib import contextmanager
# import os

@contextmanager
def undoable(message):
	RPR_Undo_BeginBlock2(0)
	try:
		yield
	finally:
		RPR_Undo_EndBlock2(0, message, -1)

def msg(m):
	RPR_ShowConsoleMsg(m)

with undoable("Set Pan According To Track SUffiX"):

	for i in range(RPR_CountTracks(0)):
		trackId = RPR_GetTrack(0, i)
		
		thename = str(RPR_GetSetMediaTrackInfo_String(trackId, "P_NAME", "", False )[3] )
		# msg (thename)
		
		RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", 0.15)
		RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 1)
		 
