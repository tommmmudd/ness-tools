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
6. [A more advanced look at harmonics](https://tommmmudd.github.io/ness-tools/tutorials/tutorial6)
7. [Creating scores from tab and tab files](https://tommmmudd.github.io/ness-tools/tutorials/tutorial7)
8. [Creating scores from MIDI files](https://tommmmudd.github.io/ness-tools/tutorials/tutorial8)
9. [Creating structures with iteration #1](https://tommmmudd.github.io/ness-tools/tutorials/tutorial9)
10. [Creating structures with iteration #2](https://tommmmudd.github.io/ness-tools/tutorials/tutorial10)
11. (coming soon) NESS Recipe #1: a simple plucking piece
12. (coming soon) NESS Recipe #2: a fretless just intonation tuning piece

## NESS Guitar instrument tutorials:
1. [Instrument basics: defaultGuitar](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial1)
2. [Instrument basics: more tempaltes](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial2)
3. [Tuning / Microtones](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)
4. [Customising string parameters #1](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial4)
5. [Customising string parameters #2](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)
6. [Customising fretboard parameters](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial6)

# How to run these files
- Clone or download this repository
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

stringCount = 6
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
my_guitar.write("basic_guitar.m")

my_score = guitar.GuitarScore(10, stringCount)       
my_score.pluck( 1, 0.5 )
my_score.playFret( 1, 1.0, 5 )
my_score.playFret( 1, 1.5, 7 )
my_score.pluck( 1, 2 )
my_score.write("basic_score.m")
```

Currently includes classes for the brass, guitar and soundboard models
