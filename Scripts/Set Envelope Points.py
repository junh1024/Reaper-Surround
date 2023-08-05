desc="Stretch & lock files depending on BPM of project & file. Length correction may be buggy"
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
	# code from https://github.com/X-Raym/REAPER-ReaScripts/blob/1a0d13ebcef3efe32f18ef213aa70673dc2d6bbe/Envelopes/X-Raym_Set%20selected%20envelope%20points%20value.eel
	
	# RPR_ShowConsoleMsg(BPM_proj)
	
	#get file BPM
	retval=  envelope=  ptidx=  timeOut=  valueOut=  shapeOut=  tensionOut=  selectedOut=0
	new_value = RPR_GetUserInputs("Point",1,"What to set these point(s) to?","",64)[4]
	new_value=float(new_value.strip())
	
	# RPR_ShowConsoleMsg(BPM_file)
	envelope = RPR_GetSelectedEnvelope(0)
	#get items
	for i in range (  RPR_CountEnvelopePoints( envelope ) ):
		
		( retval,  envelope,  ptidx,  timeOut,  valueOut,  shapeOut,  tensionOut,  selectedOut) = RPR_GetEnvelopePoint(envelope, i, timeOut, valueOut, shapeOut, tensionOut, selectedOut)
		
		if ( selectedOut == 1 ):
			RPR_SetEnvelopePoint(envelope, i, timeOut, new_value, shapeOut, tensionOut, 1, True );
