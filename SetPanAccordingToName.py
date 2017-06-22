#Some Codes from "Rename tracks to take source filename", -- Set pan for selected track(s) (SPK77)
#This script by junh1024 sets pans of tracks according to their suffixes. Useful for say, film dialogue. See global variables below for pans.

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

#Track suffixes
L=-0.15 #initial Left pan, everything else is derived modularly. Change to taste.
R=-L
LW=2*L
RW=-LW
LC=(2*L)/3
RC=-LC

#these have parenting set later on
SL=-1
SR=-SL

RR=C=0 #last 2 of naRR,center pans

# msg(L)
# msg(R)
# msg(LW)
# msg(RW)
# msg(LC)
# msg(RC)

with undoable("Set Pan According To Track Suffix"):
	# for i in range(RPR_CountTracks(0)): #for all tracks, get track
		# trackId = RPR_GetTrack(0, i)

	for i in range(RPR_CountSelectedTracks(0)): #for selected tracks, get track
		trackId = RPR_GetSelectedTrack(0, i)
		
		suffix = str(RPR_GetSetMediaTrackInfo_String(trackId, "P_NAME", "", False )[3] )[-2:].lstrip().upper() #get actual track name, last 2 chars, remove whitespace)
		
		if(suffix==''):
			continue
		
		if(suffix[0] == 'S'): #anything rear/surround. I'm not doing else cuz there may be top pans.
			RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 4) #set parent ch 5/6 rear/surround
		
		if(suffix in globals()): #if a suffix is one of the global preset pans, see global variables above
			RPR_SetMediaTrackInfo_Value(trackId, "D_PAN", eval(suffix)) #set it according to the pan designated by the suffix REFLECTION USED
		
		
		if(suffix in ('C,RR,L,R,LW,RW,LC,RC'.split(','))): #anything front
			RPR_SetMediaTrackInfo_Value(trackId, "C_MAINSEND_OFFS", 0)


