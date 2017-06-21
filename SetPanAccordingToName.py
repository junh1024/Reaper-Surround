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


debug = True #disable for using

def msg(m):
	if 'debug' in globals():
		RPR_ShowConsoleMsg(m)


L=-0.15 #initial Left pan, everything else is derived modularly. Change to taste.
R=-L
LW=2*L
RW=-LW
LC=(2*L)/3
RC=-LC

# msg(L)
# msg(R)
# msg(LW)
# msg(RW)
# msg(LC)
# msg(RC)

with undoable("Set Pan According To Track SUffiX"):

	for i in range(RPR_CountTracks(0)):
		trackId = RPR_GetTrack(0, i)
		
		suffix = str(RPR_GetSetMediaTrackInfo_String(trackId, "P_NAME", "", False )[3] )[-2:].lstrip().upper() #get actual track name, last 2 chars)
		
		if(suffix in ('C','RR')): #last 2 of naRR
			# msg("suffix was C")
			RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", 0) #center pans
			
		if(suffix in ('C,RR,L,R,LW,RW,LC,RC'.split(','))): #anything front
			RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 0)
		# RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", 0.15)
		
		if(suffix in globals()): #if a suffix is one of the global preset pans
			RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", eval(suffix)) #set it according to the pan designated by the suffix. REFLECTION USED!
		
		if(suffix[0] == 'S'): #anything rear/surround
			RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 4) #set rear/surround

		if(suffix == 'SL'): #set SL pan
			RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", -1)

		if(suffix == 'SR'): #set SR pan
			RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", 1)

