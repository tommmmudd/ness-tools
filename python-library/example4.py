from nesstools import guitar

###################################
## Nesstools example 4:
## using tab information to generate score events
###################################


###################################
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 1         # how many strings should the guitar have?


#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 1 string.
my_guitar = guitar.StringInstrument(numberOfStrings)

# export the instrument as a NESS-compatible instrument file
# as we have changed nothing and only specified a single string, this will be the low E string
my_guitar.write("example4_guitar.m")


#____________________________________________________________
# CREATE THE SCORE FILE

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
# Note that because we are using tab to create the score, the initial T is arbitrary, as it will be determined later, 
# but a value for T still needs to be specified (0 in this example)
my_score = guitar.GuitarScore(0, numberOfStrings)       

# specify the tab file as a list of strings, one element for each string
# As we only have one string, we have a single string within square brackets
tab = ["|-5-6-5-3-1-3-1-3-|"]

# specify the playback rate for this tab.
# where a value of 1 is 1/8 of a second per unit, 2 is 1/16 of a second per unit, 0.5 is 1/4 of a second per unit, etc
rate = 1.0

# convert the tab to score information in the my_score object, specifying the number of strings and the rate
my_score.tabToScore(tab, numberOfStrings, rate)

# explort the score as a NESS-compatible score file
my_score.write("example4_score.m")