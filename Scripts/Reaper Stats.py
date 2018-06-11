"""Reascript for showing stats in this order:
Tracks	Buses	Clips	MIDIClips	MIDInotes	Markers	FX	Envelopes	Sends	BPM
I wanted to collect various stats from projects for a retrospective spreadsheet. There was a bit of feature creep as I browsed through the API to see what stats I could collect, leaving out ones which are incompatible with 4.52 (TakeFX), and including those I can in a 4.52 compatible way. MIDInotes are disabled since there is a freezing bug. Stats are displayed using raw numbers, separated by tab, for easy copying into a spreadsheet.

On top of the RAW stats, I wanted to have a derived stat which showed how much effort each project was. I was struggling to find a formula for combining stats until I realized it's prolly better to have 2 stats. One reflecting size, and another reflecting complexity. The formulae I have in my spreadsheet is approximately (Tracks + Envelopes) and the average of (Clips per non-bus track, Effects per track)."""

from reaper_python import *
from sws_python import *

Tracks=RPR_CountTracks(0)
Buses=0
Clips=RPR_CountMediaItems(0)
MIDIClips=0
MIDInotes=0
Markers=0
FXs=0
Envelopes=-1#fix
Sends=0
BPM=RPR_TimeMap_GetDividedBpmAtTime(2)

fastStr = SNM_CreateFastString("")


debug = True #disable for using

def msg(m):
	if 'debug' in globals():
		RPR_ShowConsoleMsg(m)

for i in range(RPR_CountTracks(0)): #for all tracks, get track
	trackId = RPR_GetTrack(0, i)
	if ( RPR_CountTrackMediaItems( trackId ) )==0:
		Buses+=1
	Envelopes+=RPR_CountTrackEnvelopes( trackId )
	FXs+= RPR_TrackFX_GetCount( trackId )
	i=0
	while RPR_GetTrackSendName(trackId, i, "", 50)[3] != "":
		Sends+=1
		i+=1
	# RPR_GetTrackNumSends( trackId, 0 )

Envelopes+=RPR_CountTrackEnvelopes(  RPR_GetMasterTrack( 0 ) )
FXs+= RPR_TrackFX_GetCount(  RPR_GetMasterTrack( 0 ) )

for i in range (RPR_CountMediaItems( 0)):
	MI=RPR_GetMediaItem(0,i)
	take= RPR_GetTake( MI, 0 )
	SNM_GetSourceType( take, fastStr)

	if (SNM_GetFastString(fastStr))=="MIDI":
		MIDIClips+=1
		# MidiTake=FNG_AllocMidiTake(take)
		# MIDInotes+=FNG_CountMidiNotes(MidiTake)
		# FNG_FreeMidiTake(MidiTake)
		# msg(MIDIitems)

i=0
while RPR_EnumProjectMarkers(i, 1, 0, 0, "", 0)[0] != 0:#count markers
	Markers+=1	# except
	i+=1
	if i >9999:
		break

msg(			"""%s	%s	%s	%s	%s	%s	%s	%s	%s	%s\n"""
%(Tracks,Buses,Clips,MIDIClips,MIDInotes,Markers,FXs,Envelopes,Sends,BPM ))

SNM_DeleteFastString(fastStr)

