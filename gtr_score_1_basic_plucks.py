from nesstools import guitar

#______________________________________________________________________
#_____USING THE NESSTOOLS PYTHON MODULE WITH THE NESS PHYSICAL MODELS_________

# These examples show you how to generate score and instrument files for the NESS physical models, using the nesstools Python module
# To run the script, open a terminal, locate the script and type "python gtr_example1.py"
# This will create a score file and an instrument file in the "ness_files_to_process" folder
# Upload these files to https://ness-frontend.eca.ed.ac.uk/ to create audio files
# You will need to register for an account:
# 1) Register for an EASE Friend account with the University of Edinburgh: https://www.ease.ed.ac.uk/friend/
# 2) Then email the NESS team synthesis@epcc.ed.ac.uk, including your EASE username (usually your email address) in the email.  You will then be added to the user access list for the NESS web UI


# *************************************
# Setting up a score, instrument, and plucking
# GuitarScore object, StringInstrument object and GuitarScore.pluck() function
# (1) setup global parameters for string count and total score time
# (2) create an instance of the score object GuitarScore
# (3) specify string num, time, and position
# (4) write the score to a file
# *************************************

# (1) Global Parameters
stringCount = 2
T = 8					# total time


#________________________________________
#_____CREATE THE SCORE FILE_________

# (2) Create a score object, specifying the total duration (8 seconds here) and the string count (using the variable defined above)
my_score = guitar.GuitarScore(T, stringCount)


# (1) create a pluck on a particular string at a particular time
my_score.pluck( 1, 0.5 ) # string=1 (thickest string by default), time=0.5 seconds
my_score.pluck( 2, 1.0 ) # string=2, time=1.0 seconds

# (2) explot the score as a NESS-compatible score file
my_score.write("ness_files_to_process/example1_basic_score.m")


#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 2 strings
my_guitar = guitar.StringInstrument(stringCount)

# set it up as a default steel string guitar (we don't actually need this line, as this is the default)
my_guitar.defaultGuitar()

# export the instrument as a NESS-compatible instrument file
my_guitar.write("ness_files_to_process/example1_basic_guitar.m")