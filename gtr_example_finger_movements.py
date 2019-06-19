from nesstools import guitar

numberOfStrings = 1         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(numberOfStrings)

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/EXPERIMENT_long_frets_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

#					string num, time, fret_num
my_score.playFret		(1, 	0.2,   	2)		# this says to move a finger on string 1 to fret 2 at 1 second
my_score.playFret		(1, 	0.5,   	7)		# this says to move a finger on string 1 to fret 7 at 3 seconds

#add another pluck with some extra parameters for glide time and finger force
#					string num, time (s), fret_num   glide time (s)		finger force (Newtons - onto string)
my_score.playFret		(1, 	2, 			4,  		0.1,			0.5)			
my_score.playFret		(1, 	3, 			2, 			1.9, 			8)				

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/EXPERIMENT_score.m")
