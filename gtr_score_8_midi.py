from nesstools import guitar

#________________________________________
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 6         # how many strings should the guitar have?



#____________________________________________________________
# CREATE THE SCORE FILE

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
# Note that because we are using tab to create the score, the initial T is arbitrary, as it will be determined later, 
# but a value for T still needs to be specified (0 in this example)
my_score = guitar.GuitarScore(0, numberOfStrings)       

# specify the tab file as a list of strings, one element for each string
# here, each string is set up as s1, s2, ... s6, where s1 is the thicker E string



# download a Midi file (e.g. from https://freemidi.org), move it to this directory, then specify the file name like so:
midiFile = "Believe.mid"

# specify the playback rate for this midi file
rate = 0.6

# you can use this variable to transpose the whole score by N semitones
# e.g. a 5 would shift everything up 5 semitones
transpose = 0

# convert the tab to score information in the my_score object, specifying the number of strings and the rate
# NOTE: this process assumes a regularly tuned guitar!
my_score.midiToScore(midiFile, numberOfStrings, rate, transpose)

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_8_midi.m")




#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 6 strings.
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/gtr_instrument_8_midi.m")
