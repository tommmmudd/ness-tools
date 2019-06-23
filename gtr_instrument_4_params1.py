from nesstools import guitar

stringCount = 2

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()  # set our two strings to default E and A

# print the tension of our single string.
# note that the array index is 0, not 1 for the first string - we start counting at zero.
print (my_guitar.strings[0].tension)
print (my_guitar.strings[1].tension)

# 1st string settings
my_guitar.strings[0].tension = 9.5      # less tension
my_guitar.strings[0].length = 1.0       # longer string (1 metre)
my_guitar.strings[0].radius = 0.0004    # twice as thick

# 2nd string settings
my_guitar.strings[1].tension = 20.5     # more tension
my_guitar.strings[1].length = 0.5       # short string (1 metre)
my_guitar.strings[1].radius = 0.0001    # thinner

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_4_instrument.m")


#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
pluckRate = 0.333
t = 0.1
i=0
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_4_score.m")



