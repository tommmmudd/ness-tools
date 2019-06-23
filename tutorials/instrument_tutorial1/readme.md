# NESS Guitar Instrument Tutorial 1
Working with existing instrument templates


This tutorial looks at:

1. creating an instrument object with the nesstools module
2. creating an instrument with n strings
3. writing the file

Audio example of this code: [inst_tut_1.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_1.mp3)

The code for this tutorial can be found in the [gtr_instrument_1_basics.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_1_basics.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial (2) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial2)

## Creating a StringInstrument object
First, we will import the nesstools guitar module.
```python
from nesstools import guitar
```
We can use this module to define a new StringInstrument:
```python
stringCount = 6         # how many strings should the guitar have?
my_guitar = guitar.StringInstrument(stringCount)
```
We use the `stringCount` variable to log the number of strings for the instrument. This makes it very easy to change later. It is also used in the score file generation (see below).

## Using built-in instruments
In this tutorial we will use the built-in default guitar example, which is a steel string-like instrument. We do this as follows:

```python
# set this to the basic defaultGuitar()
my_guitar.defaultGuitar()
```
This default instrument will adapt to the number of strings specified. For example, if the StringInstrument was initialised with 3 strings, these strings would be set to the lowest three strings on a regularly tuned guitar. Here we have six strings, so we have all six regularly tuned strings. These are numbered as follows:

- 1 = lowest E string
- 2 = A
- 3 = D
- 4 = G
- 5 = B
- 6 = high E string

Note that the numbering is in the *opposite* order from conventional guitar notation, where string 1 usually refers to the *thinnest* string.

## Writing the instrument file
We can then export the `my_guitar` instrument to a NESS compatible .m file:

```python
# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_1_6stringDefault.m")
```

## Setting up a score file to test the instrument
Below is a quick example score file that plucks all the strings on the guitar at 0.2 seconds, then slides up to 5th fret on all strings and plucks again at 4 seconds. Note that this script for a score will adapt itself to any number of strings. So if `stringCount` is set to 1, this will set up instructions for 1 string. If `stringCount` is set to 100, it will set up instructions for 100 strings. You can therefore use this same script to test any of the instruments that we make in these tutorials (although results will vary depending on the nature of the instrument!).
The [score tutorials](https://tommmmudd.github.io/ness-tools/)  document and expand upon these basics.

```python
# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = guitar.GuitarScore(T, stringCount)       

# create a variable that represents the indexes of all strings
allStrings = [a+1 for a in range(stringCount)]		# creates a list like [1, 2, 3, 4, 5, 6] - a value for each string

my_score.pluck(allStrings, 	0.2)		# pluck all six strings at time 0.2 at fret 0

my_score.playFret(allStrings, 1, 0)		# set all fingers to 0th fret
my_score.playFret(allStrings, 3, 5, 1)	# move all fingers to 5th fret
		
my_score.pluck(allStrings, 	4)		# pluck all six strings at time 0.2 at fret 0

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_1_score.m")
```

The full code for this tutorial is here: [gtr_instrument_1_basics.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_1_basics.py).
Run the python file to create your score and instrument files. Then upload them to the [NESS user interface](https://ness-frontend.eca.ed.ac.uk/)

[<-- Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial (2) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial2)
