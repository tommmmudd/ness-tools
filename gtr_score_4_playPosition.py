from nesstools import guitar

# *************************************
# Working with fingers and frets
# GuitarScore.playFret() function
# (1) specify string num, time, and fret number
# (2) additionally specify the glide time and finger force
# *************************************

# Global Parameters
numberOfStrings = 2         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

# Here we use the playFret function to assign a finger to a fret at a particular time
# The finger is placed slightly behind the actual fret

#					string num, time, position
my_score.playPosition	(1, 	0.2,   	0.5)		
my_score.playPosition	(2, 	0.5,   	0.333)	

#add another position movement with some extra parameters for glide time and finger force
#					string num, time (s), position,   glide time (s)		finger force (Newtons - onto string)
my_score.playPosition	(1, 	1, 			0.25,  		0.3,			5)			
my_score.playPosition	(2, 	1.5, 		0.251,		1.3, 			5)				


#					string num, time, position, 	glide time
#my_score.playPosition	(1, 	5,   	0.1, 		0.3)
#my_score.playPosition	(2, 	5.5,   	0.125, 		0.3)


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_4.m")




#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar()
my_guitar.setRegularString(0, 0)	# set both the first and second string to be the same low E string
my_guitar.setRegularString(1, 0)
my_guitar.frets = False
# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/gtr_instrument_4_fretless.m")
