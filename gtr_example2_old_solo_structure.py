from nesstools import guitar

numberOfStrings = 6         # how many strings should the guitar have?
T = 25                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(numberOfStrings)

# set it up as a default steel string guitar
my_guitar.defaultGuitar()

# make the strings 50% longer (try changing this value to stretch the strings to different lengths: 
# e.g. 2 is double length, 0.5 is half length
for string in my_guitar.strings:
    string.length *= 1.5			# <-- string stretch ratio

# disable frets (fretless) - change to "True" if you want the frets back!
my_guitar.frets = False

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/example2_long_fretless_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

# Add score events (plucks and finger placements) using a built in function
startTime = 1                       # events start at 1 second
endTime = T-6                       # final event comes 6 seconds before the end of the generated audio file, allowing the notes to ring out
timingArray = [0.25, 0.25, 0.5]     # specify a rhythm as a list of timing values (in seconds)
timingScale = 1                     # a scalar for all timing values (e.g. a value of 2 would double the duration of all events)
fingerForce = 1                     # finger force on the string/fretboard in Newtons

# Use these parameters with the built in structureSolo function, 
# which ensures that only one string is played at a time
# string and fret changes are made with a random walk
# There are a range of functions like this, most of which are probably fairly idiosynchratic to my own process
# but they may be of interest.
# be sure to check the argument requirements for each.
my_score.structureSolo(startTime, endTime, timingArray, timingScale, fingerForce)

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/example2_score.m")
