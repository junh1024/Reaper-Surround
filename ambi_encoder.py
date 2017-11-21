from math import sin	,cos	,sqrt, radians
import os

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

r=2 #radius meters?,ignore
z=0
hz=45#height

global A,E
A=0
E=0

w=30 #hex
# w=45 #cine

speaker_array = [
'L',	[-w	,	r	,z]	,
'R',	[w	,	r	,z]	,
'C',	[0	,	r	,z]	,
'LFE',	[0	,	r	,z]	,
'BL',	[-180+w,r	,z]	,				
'BR',	[180-w ,r	,z]	,
'SL',	[-90,	r	,z]	,
'SR',	[90	,	r	,z]	,

'HL',	[-w	,	r	,hz]	,
'HR',	[w	,	r	,hz]	,

'BTL',	[-w	,	r	,-hz]	,
'BTR',	[w	,	r	,-hz],

'HBL',	[-180+w,r	,hz]	,				
'HBR',	[180-w ,r	,hz]	,
'HSL',	[-90,	r	,hz]	,
'HSR',	[90	,	r	,hz]	
]

# print (speaker_array)
# restrictions=[A,E,sin,cos,sqrt,radians]
F = open("jsfx_shell.txt", "w") 
#create temp variables
in_chans=16
for in_chan in range (0,in_chans):
	F.write(str('spl'+str(in_chan)+'_in=spl'+str(in_chan)+'*gain_comp*gain_slider;\n'))

count=0
for line in fuma_pan_equations.splitlines():
	
	F.write(str('spl'+str(count)+'='))
	for speaker in range (0, int(len(speaker_array)/2 )):
		F.write(str ('spl'+str(speaker)+'_in*'))
		# print (speaker)
		A=radians(-speaker_array[speaker*2+1][0])
		E=radians(speaker_array[speaker*2+1][2])
		coeff=eval(line,globals() )
		F.write(str(round(coeff,5)))
		if(speaker < int(len(speaker_array)/2 )-1):
			F.write('+')
	# F.seek(-1,os.SEEK_CUR)
	F.write(str(';\n'))
	count+=1
	
F.close
# input("Press Enter to continue")



# //calculate pan coeffs reduces CPU further. These now only happen per slider instead of per sample.
