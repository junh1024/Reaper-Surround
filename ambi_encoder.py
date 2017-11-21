from math import sin	,cos	,sqrt, radians
# import os

#TODO: remove if coeff <.1, account for varying w

fuma_pan_equations="""sqrt(1/2)
cos(A)*cos(E)
sin(A)*cos(E)
sin(E)
(1/2)*(3*sin(E)*sin(E)-1)
cos(A)*sin(2*E)
sin(A)*sin(2*E)
cos(2*A)*cos(E)*cos(E)
sin(2*A)*cos(E)*cos(E)
(1/2)*sin(E)*(5*sin(E)*sin(E)-3)
sqrt(135/256)*cos(A)*cos(E)*(5*sin(E)*sin(E)-1)
sqrt(135/256)*sin(A)*cos(E)*(5*sin(E)*sin(E)-1)
sqrt(27/4)*cos(2*A)*sin(E)*cos(E)*cos(E)
sqrt(27/4)*sin(2*A)*sin(E)*cos(E)*cos(E)
cos(3*A)*cos(E)*cos(E)*cos(E)
sin(3*A)*cos(E)*cos(E)*cos(E)"""

fuma_order=['W','X','Y','Z','R','S','T','U','V','K','L','M','N','O','P','Q']

r=2 #radius meters?,ignore
z=0
hz=45#height

global A,E
A=0#angle
E=0#elevation

w="slider2" #hex
# w=45 #cine

f = open("jsfx_shell.txt", "w") 

# slider1:1<0,2,0.1>Gain
# slider2:30<0,90,2.5>Position of R (controls the width of all F & B pairs)
# slider3:45<0,90,5>Height Elevation

speaker_array = [
'L',	['-slider2'	,	r	,z]	,
'R',	['slider2'	,	r	,z]	,
'C',	['0	',	r	,z]	,
'LFE',	['0	',	r	,z]	,
'BL',	['-180+slider2',r	,z]	,				
'BR',	['180-slider2' ,r	,z]	,
'SL',	['-90',	r	,z]	,
'SR',	['90'	,	r	,z]	,

'HL',	['-slider2'	,	r	,'slider3']	,
'HR',	['slider2'	,	r	,'slider3']	,

'BTL',	['-slider2'	,	r	,'-slider3']	,
'BTR',	['slider2'	,	r	,'-slider3'],

'HBL',	['-180+slider2',r	,'slider3']	,				
'HBR',	['180-slider2' ,r	,'slider3']	,
'HSL',	['-90',	r	,'slider3']	,
'HSR',	['90'	,	r	,'slider3']	
]
f.write('@init\n')

coefficientnames=[]

for speaker in range (0, int(len(speaker_array)/2 )):
	print(speaker_array[speaker*2]+'_A='+str(speaker_array[speaker*2+1][0])+';\n')
	print(speaker_array[speaker*2]+'_E='+str(speaker_array[speaker*2+1][2])+';\n')
	
f.write('@slider') 


count=0                                                 
for line in fuma_pan_equations.splitlines():
	for speaker in range (0, int(len(speaker_array)/2 )):
		variablename=fuma_order[count]+"_coeff_"+speaker_array[speaker*2]
		coefficientnames.append(variablename)
		editedline=line.replace('A',str(speaker_array[speaker*2+1][0]))
		editedline=line.replace('E',str(speaker_array[speaker*2+1][2]))
		print(variablename+'='+editedline+';\n')
		# write=line
	count+=1


# print (speaker_array)
# restrictions=[A,E,sin,cos,sqrt,radians]

#create temp variables
# in_chans=16
# for in_chan in range (0,in_chans):
	# f.write(str('spl'+str(in_chan)+'_in=spl'+str(in_chan)+'*gain_comp*gain_slider;\n'))

# count=0
# for line in fuma_pan_equations.splitlines():
	
	# f.write(str('spl'+str(count)+'='))
	# for speaker in range (0, int(len(speaker_array)/2 )):
		# f.write(str ('spl'+str(speaker)+'_in*'))
		# A=radians(-speaker_array[speaker*2+1][0])
		# E=radians(speaker_array[speaker*2+1][2])
		# coeff=eval(line,globals() )
		# f.write(str(round(coeff,5)))
		# if(speaker < int(len(speaker_array)/2 )-1):#dont add + for last element of line
			# f.write('+')
	# f.write(str(';\n'))
	# count+=1
	
f.close
# input("Press Enter to continue")



# //calculate pan coeffs reduces CPU further. These now only happen per slider instead of per sample.
