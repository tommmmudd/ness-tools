# NESS Python library

This library presents some Python classes for building score and instrument files for the [NESS physical models](http://ness.music.ed.ac.uk).

Below are a some tutorials that give you an idea of how to use these tools for engaging with the Ness models.


# Tutorials

## NESS Guitar score tutorials:
1. [Score basics: pluck a couple of a strings](https://tommmmudd.github.io/ness-tools/tutorials/tutorial1)
2. [Plucking with more control](https://tommmmudd.github.io/ness-tools/tutorials/tutorial2)
3. [Putting fingers on frets with playFret()](https://tommmmudd.github.io/ness-tools/tutorials/tutorial3)
4. [Putting fingers in positions with playPosition()](https://tommmmudd.github.io/ness-tools/tutorials/tutorial4)
5. [Playing harmonics with playHarmonic()](https://tommmmudd.github.io/ness-tools/tutorials/tutorial5)
6. A more advanced look at harmonics
7. Creating structures with iteration #1
8. Creating structures with iteration #1
9. NESS Recipe #1: a simple plucking piece
10. NESS Recipe #2: a fretless just intonation tuning piece

## NESS Guitar instrument tutorials:
1. coming soon...

# How to run these files
- clone this repository
- Open a terminal and cd to the folder.
- type "python gtr_score_1_basic_plucks.py" (or whichever file you wish to run)
- This should create both a score file and an instrument file in the "ness_files_to_process" folder
- Upload these files to the [NESS User Interface](https://ness-frontend.eca.ed.ac.uk/) to create audio files
- You will need to register for an account:
- 1) Register for an EASE Friend account with the University of Edinburgh: https://www.ease.ed.ac.uk/friend/
- 2) Then email the NESS team synthesis@epcc.ed.ac.uk, including your EASE username (usually your email address) in the email.  You will then be added to the user access list for the NESS web UI.


# Example implementation

```python
from nesstools import guitar

stingCount = 6
my_guitar = guitar.StringInstrument(stingCount)
my_guitar.defaultGuitar()
my_guitar.write("basic_guitar.m")

my_score = guitar.GuitarScore(60, 2)       
pluckTime = 1
pluckString = 1
my_score.plucks.append( [pluckString, pluckTime, 0.8, 0.0001, 1] )
my_score.write("basic_score.m")
```

Currently includes classes for the brass, guitar and soundboard models
