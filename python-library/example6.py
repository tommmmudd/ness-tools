from nesstools import guitar

###################################
## Nesstools example 6:
## using a txt tab file to generate score events
###################################


###################################
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 6         # how many strings should the guitar have?


#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 6 strings.
my_guitar = guitar.StringInstrument(numberOfStrings)

# export the instrument as a NESS-compatible instrument file
my_guitar.write("example6_guitar.m")


#____________________________________________________________
# CREATE THE SCORE FILE

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
# Note that because we are using tab to create the score, the initial T is arbitrary, as it will be determined later, 
# but a value for T still needs to be specified (0 in this example)
my_score = guitar.GuitarScore(0, numberOfStrings)       

# specify the tab file as a list of strings, one element for each string
# here, each string is set up as s1, s2, ... s6, where s1 is the thicker E string



# import a txt tab file (have a look at the structure of this text file for guidance)
tabFile = "tab/bach.txt"

# specify the playback rate for this tab.
# where a value of 1 is 1/8 of a second per unit, 2 is 1/16 of a second per unit, 0.5 is 1/4 of a second per unit, etc
rate = 1.0

# convert the tab to score information in the my_score object, specifying the number of strings and the rate
my_score.tabToScore(tabFile, numberOfStrings, rate)

# explort the score as a NESS-compatible score file
my_score.write("example6_bach_score.m")