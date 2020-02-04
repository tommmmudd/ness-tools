from nesstools import guitar
import random as r

stringCount = 3

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()  # set our two strings to default E and A
my_guitar.setRegularString(0, "Low D")
for string in my_guitar.strings:
	string.length *= 1.333
	string.highDecay = 8
	string.lowDecay = 18
	string.outputPos = 0.97

my_guitar.fingerMass = 0.005
my_guitar.fingerStiffness = 1e5
my_guitar.fingerExp = 3
my_guitar.fingerLoss = 100

my_guitar.backboardParams = [-0.004, 0, -0.0002]
my_guitar.fretHeight = -0.003

my_guitar.write("ness_files_to_process/inst_7_instrument.m")


#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 90                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
t = 0.1
fingerForce = 0.4
pluckForce = 0.08
frets = [2, 3, 5, 7, 8, 11, 12, 14, 15]
while t < T-10:
	fret = frets[ r.randint(0, len(frets)-1) ]
	glide = r.random()*r.random()*r.random()*3
	stringList = [i+1 for i in range(stringCount)]
	fretList = [fret for i in range(stringCount)]
	my_score.playFret(stringList, t, fretList, glideTime=glide, fingerF=fingerForce)
	if r.random() < 0.4:
		pluckPos = r.random()*0.3 + 0.6
		my_score.pluck(stringList, 0.055, pluckPos, 0.001, pluckForce)

	t += r.random()*r.random()*3


# my_score.playFret([1, 2, 3], 0.05, [5, 5, 5], fingerF=fingerForce)
# my_score.pluck([1, 2, 3], 0.055, 0.91, 0.001, pluckForce)
# my_score.playFret([1, 2, 3], 1.5, [2, 2, 2], glideTime=0.1, fingerF=fingerForce)
# my_score.playFret([1, 2, 3], 2, [5, 5, 5], glideTime=0.2, fingerF=fingerForce)
# my_score.playFret([1, 2, 3], 2.5, [3, 3, 3], glideTime=0.01, fingerF=fingerForce)
# my_score.pluck([1, 2, 3], 2.005, 0.91, 0.001, pluckForce)

# my_score.playFret([1, 2, 3], 4, [5, 5, 5], glideTime=0.2, fingerF=fingerForce)
# my_score.pluck([1, 2, 3], 4.005, 0.91, 0.001, pluckForce)
# my_score.playFret([1, 2, 3], 4.3, [2, 2, 2], glideTime=0.004, fingerF=fingerForce)
# my_score.playFret([1, 2, 3], 5, [7, 7, 7], glideTime=0.4, fingerF=fingerForce)
# my_score.pluck([1, 2, 3], 5.005, 0.91, 0.001, pluckForce)

# my_score.playFret([1, 2, 3], 7.3, [2, 2, 2], glideTime=0.004, fingerF=fingerForce)
# my_score.pluck([1, 2, 3], 7.0, 0.91, 0.001, pluckForce)
# my_score.playFret([1, 2, 3], 9, [12, 12, 12], glideTime=1.8, fingerF=fingerForce)




# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_7_score.m")



