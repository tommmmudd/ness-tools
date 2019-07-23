from nesstools import guitar
import random as r 			# use the random module for randomised events

#________________________________________
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 6         # how many strings should the guitar have?
T = 60

#________________________________________
#_____CREATE THE SCORE FILE______________

my_score = guitar.GuitarScore(T, numberOfStrings)

# E MINOR - frets for strings
s1Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # low E string
s2Frets = [0, 2, 3, 5, 7, 9, 10, 12]  # A
s3Frets = [0, 2, 4, 5, 7, 9, 10, 12]  # D
s4Frets = [0, 2, 4, 5, 7, 9, 11, 12]  # G
s5Frets = [0, 1, 3, 5, 7, 8, 10, 12]  # B
s6Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # E
allFrets = [s1Frets, s2Frets, s3Frets, s4Frets, s5Frets, s6Frets]

# our rhythm - a quarter-second followed by two eighth-second events
rhythm = [1/4.0, 1/8.0, 1/8.0]

# start from time=1 second
time = 1		# our current time variable that we will increase until we hit our maximum
count = 0		# our iteration counter


while time < T-6:
	# this sets up a WHILE LOOP - all the indented code below is looped 
	# the loop stops when our cumulative time variable, t, gets to 6 seconds from the end of the score
	# (the -6 is so that we have time for the final events to ring out)

	# for each iteration, we'll add an event on a particular string
	# here we use the random module to create a random integer between 1 and numberOfStrings for our string number
	string = r.randint(1, numberOfStrings)

	# choose a fret from the available fret lists above
	fretCountForString = len(allFrets[string-1]) - 1
	fret = allFrets[string-1][r.randint(0, fretCountForString)]

	# we'll use the playFret function from tutorial 3:
	my_score.playFret	(string, time, fret)

	# we increase our current time by whichever is the next in the rhythm list
	# count % len(rhythm) means that as count increases, the (count % 3) stays in the range 0, 1, 2, 0, 1, 2, 0, ...
	# len(rhythm) gets the length of our list, which in this case is 3.
	time += rhythm[count % len(rhythm)]	
	# keep count of how many iterations we have done
	count += 1



# Once the whileloop is finished, export the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_10_iteration2.m")



#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 6 strings.
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/gtr_instrument_10_iteration2.m")