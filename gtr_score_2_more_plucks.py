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
# Working with additional pluck parameters
# GuitarScore.pluck() function
# (1) specify simple string num and time
# (2) additionally specify the pluck position (0-1), glide time (seconds) and finger force (Newtons)
# *************************************


# Global Parameters
stringCount = 2
T = 10					# total time


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       


# (1) create a pluck on a particular string at a particular time
my_score.pluck( 1, 1 )

# create another pluck on a particular string at a particular time, with a given position, duration and force
# here we set the parameters as variables and then use the variables inside the pluck command
string = 2			# pluck the first string (lowest, rather than highest)
time = 3			# pluck at 1 second in the score

# (2) optional extra parameters for position (default=0.8)
pluckPosition = 0.8		# pluck 80% of the way from the nut to the bridge
pluckDuration = 0.0005	# pluck duration in seconds - the duration of the force on the string
pluckForce = 0.05		# pluck force in Newtons

my_score.pluck( string, time, pluckPosition, pluckDuration, pluckForce )

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/example2_basic_score.m")



#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 2 strings
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/example2_basic_guitar.m")