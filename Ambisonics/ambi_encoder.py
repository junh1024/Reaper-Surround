from math import sin ,cos ,sqrt, radians

fuma_pan_equations="""sqrt(1/2)*slider4
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
z=0#ELL elevation
hz=45#height degrees

f = open("jsfx_shell.txt", "w") 

#pi is anticlockwise
speaker_array = [
'L',['(-A_rad)',r,z],
'R',['(A_rad)',r,z],
'C',['(0)',r,z],
'LFE',['(0)',r,z],
'BL',['($pi+A_rad)',r,z],
'BR',['(-$pi-A_rad)' ,r,z],
'SL',['(-(-$pi/2))',r,z],
'SR',['((-$pi/2))',r,z],

'HL',['(-A_rad)',r,'E_rad'],
'HR',['(A_rad)',r,'E_rad'],

'BTL',['(-A_rad)',r,'-E_rad'],
'BTR',['(A_rad)',r,'-E_rad'],

'HBL',['($pi+A_rad)',r,'E_rad'],
'HBR',['(-$pi-A_rad)' ,r,'E_rad'],
'HSL',['(-(-$pi/2))',r,'E_rad'],
'HSR',['((-$pi/2))',r,'E_rad']
]
f.write("""desc: 15.1 to 3oA Fuma downmixer. LFE is moved to C, so gain -10dB or silence it.
//Generated from ambi_encoder.py , comments there.

slider1:30<0,90,2.5>Angle of R (influences speaker width)
slider2:45<0,90,5>Elevation of height speakers
slider3:1<0,2,0.1>Gain
slider4:1<0,2,0.1>W Gain
slider5:1<0,2,0.1>Reserved

@init
A_rad=slider1*($pi/-180);
E_rad=slider2*($pi/180);
""")

coefficientnames=[]

#make initial speaker positions
for speaker in range (0, int(len(speaker_array)/2 )):
	f.write(speaker_array[speaker*2]+'_A='+str(speaker_array[speaker*2+1][0])+';\n')
	f.write(speaker_array[speaker*2]+'_E='+str(speaker_array[speaker*2+1][2])+';\n')
	
f.write("""
@slider
A_rad=slider1*($pi/-180);
E_rad=slider2*($pi/180);
""") 

count=0
#make pan equations in @slider
for line in fuma_pan_equations.splitlines():
	for speaker in range (0, int(len(speaker_array)/2 )):
		variablename=fuma_order[count]+"_coeff_"+speaker_array[speaker*2]
		coefficientnames.append(variablename)
		editedline=line.replace('A',str(speaker_array[speaker*2+1][0]))
		editedline=editedline.replace('E',str(speaker_array[speaker*2+1][2]))
		f.write(variablename+'='+editedline+'*slider3;\n')
		# write=line
	count+=1

# print (speaker_array)
# restrictions=[A,E,sin,cos,sqrt,radians]
f.write('\n@sample\n')

#create temp variables for speaker inputs
in_chans=int(len(speaker_array)/2 )
for count in range (0,in_chans):
	if(count%2 ==0): #need this hack because splN is active even though Nchans is below that
		f.write("num_ch>"+str(count)+"?\n(")
	f.write(str('spl'+str(count)+'_in=spl'+str(count)+';\n'))
	if(count%2 !=0):
		f.write(");\n")
f.write('\n')

count=0
coefficientnamescounter=0
#write coefficients, multiply each speaker in with fuma coefficient for each fuma chan
for line in fuma_pan_equations.splitlines():
	if(count%2 ==0): #need this hack because splN is active even though Nchans is below that
		f.write("num_ch>"+str(count)+"?\n(")
	f.write(str('spl'+str(count)+'='))
	for speaker in range (0, int(len(speaker_array)/2 )):
		f.write(str ('spl'+str(speaker)+'_in*') + coefficientnames[coefficientnamescounter] )
		# A=radians(-speaker_array[speaker*2+1][0])
		# E=radians(speaker_array[speaker*2+1][2])
		# coeff=eval(line,globals() )
		# f.write(str(round(coeff,5)))
		coefficientnamescounter+=1
		if(speaker < int(len(speaker_array)/2 )-1):#dont add + for last element of line
			f.write('+')
	f.write(str(';\n'))
	if(count%2 !=0):
		f.write(");\n")
	count+=1
	
f.close
# input("Press Enter to continue")
