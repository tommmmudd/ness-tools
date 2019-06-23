from nesstools import guitar

stringCount = 6

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument()

my_guitar.defaultGuitar()			# a 4 string bass: EADG
my_guitar.tuneString(1, "D2")
my_guitar.tuneString(2, "G2")
my_guitar.tuneString(3, "D3")
my_guitar.tuneString(4, "G3")
my_guitar.tuneString(5, "C4")
my_guitar.tuneString(6, "E4")

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_3_tunedGuitar.m")




#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
pluckRate = 0.15
t = 0.1
i=0
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_3_score.m")



