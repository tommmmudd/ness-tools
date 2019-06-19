from nesstools import guitar
import random as r

numberOfStrings = 3         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 3 strings
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/RENAME_basic_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

#					string num, time, fret_num
#my_score.playFret		(1, 	0.2,   	2)		# this says to move a finger on string 1 to fret 2 at 1 second
#my_score.playFret		(1, 	0.5,   	7)		# this says to move a finger on string 1 to fret 7 at 3 seconds


# play harmonics
my_score.playHarmonic(1, 0.5, 	1/2.0)
my_score.playHarmonic(2, 0.6, 	1/2.0)
my_score.playHarmonic(3, 0.7, 	1/2.0)
my_score.playHarmonic(1, 1.5, 	1/3.0)
my_score.playHarmonic(2, 1.6, 	1/3.0)
my_score.playHarmonic(3, 1.7, 	1/3.0)
my_score.playHarmonic(1, 2.5, 	1/4.0)
my_score.playHarmonic(2, 2.6, 	1/4.0)
my_score.playHarmonic(3, 2.7, 	1/4.0)



# as it goes down the neck, the force needs to be reduced?


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/RENAME_harmonics_score.m")
