desc="REAPER to FFMPEG edit"
by="junh1024"

from reaper_python import *
from contextlib import contextmanager

fudge_factor=0.01

@contextmanager
def undoable(message):
	RPR_Undo_BeginBlock2(0)
	try:
		yield
	finally:
		RPR_Undo_EndBlock2(0, message, -1)

debug = True

def msg(m):
		RPR_ShowConsoleMsg(m)

# msg(RPR_CountSelectedMediaItems(0))
		
with undoable(desc):
	
	# "  -f concat -safe 0 
	ffmpegstring=""
	filestring=""
	
	#get items
	for i in range (RPR_CountSelectedMediaItems( 0)):
		MI=RPR_GetSelectedMediaItem(0,i)
		take=RPR_GetActiveTake(MI)

		start= RPR_GetMediaItemTakeInfo_Value( take, "D_STARTOFFS" )
		# RPR_ShowConsoleMsg(start)
		
		start=str(start)
		length=RPR_GetMediaItemInfo_Value( MI, "D_LENGTH" )
		# RPR_ShowConsoleMsg(length)
		length=str(length-fudge_factor)
		
		
		
		pcm_source=RPR_GetMediaItemTake_Source( take )
		filepath = str(RPR_GetMediaSourceFileName(pcm_source, "", 512)[1])
		ext = filepath[-3:]
		
		# Remux to new audio-only file, less CPU when full-decode seek
		ffmpegstring+='ffmpeg.exe  -i "'  + filepath + '" -c copy -vn -n "' +  filepath[:-3] + '"_src.mka\n'
		
		newfilepath='"' + filepath[:-3] + "_temp_" + str(i) +'.' + 'mka' + '"'
		
		# Full-decode seek needed for accurate editing. Cut to new temp files since FFMPEG can't cut & join files simultaneously
		ffmpegstring+='ffmpeg.exe  -i "' + filepath[:-3]+  '_src.mka"'  +  " -ss " +start + " -t " + length  + ' -c copy -y ' + newfilepath + '\n'
		# newfilepathnoquotes=newfilepath
		filestring+="file 'file:" + newfilepath[1:-1].replace('\\','/')  + "'\n"
	
	# Join temp tiles to mkv, mkv has less overhead over mp4, sometimes very signifigant
	ffmpegstring+='ffmpeg.exe -f concat -safe 0 -i "' +  filepath[:-3] +'txt"' + ' -c copy -y '+ '"' + filepath[:-3] + "_edited" +'.' +'mkv'+ '"\n'
	
	# ffmpegstring+='ffmpeg.exe   -i "' + filepath[:-3] + "_edited" +'.' +'mkv" ' + '-filter:a "asetpts=PTS-STARTPTS" -c copy ' + '"' + filepath[:-3] + "_edited2" +'.' +'mkv'+ '"'

	# ffmpegstring
	
	# 
	# numberofitems
	
	# get filename, append string, and extention
	# RPR_ShowConsoleMsg(start+' '+length)

	
	RPR_ShowConsoleMsg(ffmpegstring)
	
	with open(filepath[:-3] +"txt", "w")  as file:
		file.write(filestring)
