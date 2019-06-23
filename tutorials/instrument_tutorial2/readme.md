# NESS Guitar Instrument Tutorial 2
Working with existing instrument templates


This tutorial explores some of the other existing instrument templates

The code for this tutorial can be found in the [gtr_instrument_2_templates.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_2_templates.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (1)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial1)  / / /  [Next Tutorial (3) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)

## Setting up
In this tutorial, we'll introduce some of the built-in guitar examples. First, as ever, we import the module
```python
from nesstools import guitar
```
and now we set up our string instrument object
```python
# create a string instrument object
my_guitar = guitar.StringInstrument()
```
Unlike in many of the other tutorials, we are not going to set up a `stringCount` variable. Instead we are going to take the `stringCount` from an instrument template. Here, we set up our instrument as the default 4-string bass:

```python
my_guitar.defaultBass()			# a 4 string bass: EADG
stringCount = my_guitar.stringCount		# stringCount = 4 in our case, for the bass
```

Here we use the built-in function `defaultBass()` to create an instrument with 4 strings. We could just write `stringCount = 4` after this to set our variable, but it is useful to take the string count from the instrument object, in case we're not sure how many strings the instrument now has. We will resue this variable in creating the score, so it's important that we get it right. If the score attempts to play strings that don't exist then the NESS processing will fail.

## List of instruments
Below is a list of default instruments. They are relatively arbitary! In the subsequent tutorials, we will look at how to get in and edit the instrument parameters more directly rather than relying on these templates. They can be a useful guide to what ranges of values are relevant for which parameters though.

(List last updated 21-06-19)

- `defaultGuitar()`  		   - will NOT set a new stringCount, but adapts to the amount currently defined
- `brightGuitar()`           - a 6 string guitar with a brighter tone
- `defaultBass()`			   - a 4 string bass: EADG
- `bass6String()`			   - a 6 string bass: EADGBE
- `defaultGuitarAndBass()`   - a 10 string combined instrument: 6 regular guitar strings and 4 regular bass strings
- `earthGuitar()`            - a 6 string guitar tuned to AEADF#B
- `dadgadGuitar()`           - a 6 string guitar tuned to: DADGAD
- `lowGuitar()`              - a 6 string guitar with longer strings, resulting in a lower register. The strings are still more-or-less in tune with each other
- `randomGuitar()`           - a 6 string guitar with lots of parameters randomised (won't be in regular tuning!)
- `randomGlassGuitar()`      - a 6 string randomised guitar with thicker strings that give a bar-like glassy sound. NOTE: can lead to some large DC offsets, so you will likely need to download each string output wav separately and add a DC blocker to each file.

## Creating a score file
This score file generation is exactly the same as in the last tutorial. Feel free to tweak it though to explore the specifics of your chosen instrument template. Note that this code relies on the `stringCount` variable having been set according to your instrument choice as shown above.

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

The full code for this tutorial is here: [gtr_instrument_2_templates.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_2_templates.py).
Run the python file to create your score and instrument files. Then upload them to the [NESS user interface](https://ness-frontend.eca.ed.ac.uk/)

[<-- Previous Tutorial (1)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial1)  / / /  [Next Tutorial (3) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)

