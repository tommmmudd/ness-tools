from nesstools import guitar

stringCount = 3         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = guitar.GuitarScore(T, stringCount)       

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



# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_5_harmonics.m")




#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 3 strings
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/gtr_instrument_5_harmonics.m")