from nesstools import guitar

stringCount = 2

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()  # set our two strings to default E and A

my_guitar.backboardParams = [-0.001, 0, -0.000]
my_guitar.fretHeight = -0.0005


# export the file as a format compatible instrument file for the NESS model

my_guitar.backboardParams = [-0.00002, 0, -0.000002]
my_guitar.fretHeight = -0.00001
my_guitar.write("ness_files_to_process/inst_6a_instrument.m")

my_guitar.backboardParams = [-0.0002, 0, -0.00002]
my_guitar.fretHeight = -0.0001
my_guitar.write("ness_files_to_process/inst_6b_instrument.m")

my_guitar.backboardParams = [-0.002, 0, -0.0002]
my_guitar.fretHeight = -0.001
my_guitar.write("ness_files_to_process/inst_6c_instrument.m")

my_guitar.backboardParams = [-0.02, 0, -0.02]
my_guitar.fretHeight = -0.01
my_guitar.write("ness_files_to_process/inst_6d_instrument.m")

my_guitar.backboardParams = [-0.2, 0, -0.02]
my_guitar.fretHeight = -0.1
my_guitar.write("ness_files_to_process/inst_6e_instrument.m")


#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 12                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
pluckRate = 0.333
t = 0.1
i=0
my_score.playFret([1, 2], 0.05, [0, 0])
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate

my_score.playFret([1, 2], T/3, [7, 7])

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_6_score.m")



