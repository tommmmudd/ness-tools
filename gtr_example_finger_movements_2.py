from nesstools import guitar
import random as r 			# import the random module as "r"
	
numberOfStrings = 1         # how many strings should the guitar have?
T = 15                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(numberOfStrings)

# set it up as a default steel string guitar
my_guitar.defaultGuitar()

# make the strings 50% longer (try changing this value to stretch the strings to different lengths: 
# e.g. 2 is double length, 0.5 is half length
for string in my_guitar.strings:
    string.length *= 1.25			# <-- string stretch ratio

# disable frets (fretless) - change to "True" if you want the frets back!
my_guitar.frets = True

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/EXPERIMENT2_long_frets_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

# Add score events (plucks and finger placements) using a built in function
t = 0.1                       # events start at 1 second
moveRate = 0.1`5
#					string num, time, fret_num, glide time in seconds
while t < T-6:
	# choose a new fret and glideTime randomly
	newFret = r.randint(0, 12)				# note that the random functions rely on the random module being imported as r (see top of file)
	glideTime = r.random()*moveRate*0.98					# random number between 0 and 0.25
	my_score.playFret		(1, t,   newFret,    glideTime)
	t += moveRate		# increment the time by 

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/EXPERIMENT2_score.m")
