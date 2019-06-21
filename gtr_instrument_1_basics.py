from nesstools import guitar

# Global Parameters
stringCount = 6         # how many strings should the guitar have?


#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(stringCount)

# set this to the basic defaultGuitar()
my_guitar.defaultGuitar()

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_1_6stringDefault.m")




#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# create a variable that represents the indexes of all strings
allStrings = [a+1 for a in range(stringCount)]		# creates a list like [1, 2, 3, 4, 5, 6] - a value for each string

my_score.pluck(allStrings, 	0.2)		# pluck all six strings at time 0.2 at fret 0

my_score.playFret(allStrings, 1, 0)		# set all fingers to 0th fret
my_score.playFret(allStrings, 3, 5, 2)	# move all fingers to 5th fret over 2 seconds
		
my_score.pluck(allStrings, 	4)		# pluck all six strings at time 0.2 at fret 0

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_1_score.m")



