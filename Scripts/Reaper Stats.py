# Clips	Buses	Tracks	FX	RAM	CPU	BPM

from reaper_python import *
from contextlib import contextmanager
from sws_python import *

# import os
Buses=0
Envelopes=0
TrackFXs=0
Sends=0
MIDIitems=0

fastStr = SNM_CreateFastString("")
# SNM_GetFastString(fastStr)


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

# with undoable("Set Pan According To Track Suffix"):

for i in range(RPR_CountTracks(0)): #for all tracks, get track
	trackId = RPR_GetTrack(0, i)
	if ( RPR_CountTrackMediaItems( trackId ) )==0:
		Buses+=1
	Envelopes+=RPR_CountTrackEnvelopes( trackId )
	TrackFXs+= RPR_TrackFX_GetCount( trackId )
	# Sends+=RPR_GetTrackNumSends( trackId, 0 )

Envelopes+=RPR_CountTrackEnvelopes(  RPR_GetMasterTrack( 0 ) )
TrackFXs+= RPR_TrackFX_GetCount(  RPR_GetMasterTrack( 0 ) )

for i in range (RPR_CountMediaItems( 0)):
	MI=RPR_GetMediaItem(0,i)
	take= RPR_GetTake( MI, 0 )
	SNM_GetSourceType( take, fastStr)
	
	# TrackFXs+=RPR_TakeFX_GetCount( take )
	msg(SNM_GetFastString(fastStr))
	if (SNM_GetFastString(fastStr))=="MIDI":
		MIDIitems+=1
		msg(MIDIitems)


# msg("""
# Clips: %s
# Buses: %s
# Tracks: %s
# Envelopes: %s
# BPM: %s
# TrFX: %s
# Sends: %s

# """   % (  RPR_CountMediaItems( 0) ,Buses,  RPR_CountTracks( 0 ) ,Envelopes, RPR_TimeMap_GetDividedBpmAtTime( 2 ), TrackFXs,Sends) )
	
	 # RPR_GetTrackNumSends( tr, 0 )
SNM_DeleteFastString(fastStr)
