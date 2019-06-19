from nesstools import guitar
import random as r

numberOfStrings = 3         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 3 strings
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/RENAME_basic_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

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

# for these strings we also specify a pluck position
# the default pluck position for the playHarmonic function is 0.8 (1/5 of the string away from the bridge)
# this default makes the 1/5 harmonic impossible as it makes a maximum in the string at the exact point where we want a node!
# in the harmonics below, the pluck position is swapped around to avoid the node
my_score.playHarmonic(1, 3, 	1/5.0, pluckPos=0.654)
my_score.playHarmonic(2, 3.1, 	1/5.0, pluckPos=0.654)
my_score.playHarmonic(3, 3.2, 	1/5.0, pluckPos=0.654)
my_score.playHarmonic(1, 3.5, 	1/6.0, pluckPos=0.754)
my_score.playHarmonic(2, 3.6, 	1/6.0, pluckPos=0.754)
my_score.playHarmonic(3, 3.7, 	1/6.0, pluckPos=0.754)

# as it goes down the neck, the force needs to be reduced?


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/RENAME_harmonics_score.m")
