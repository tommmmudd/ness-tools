# NESS Guitar Instrument Tutorial 3
Custom tunings

This tutorial shows how to manually tune strings using the `tuneString()` function. This allows a given string to be set to a particular note - by adjusting it's tension parameter.

The code for this tutorial can be found in the [gtr_instrument_3_tuning.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_3_tuning.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (2)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial2)  / / /  [Next Tutorial (4) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial4)

## Setting up
This part should be familiar by now from the other tutorials. We import the module, create a StringInstrument, and set it to the `defaultGuitar`:
```python
from nesstools import guitar

stringCount = 6   # 6 strings, please

# create a string instrument object and set it to the default guitar
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
```

## Tuning up
The default tuning here is EADGBE. These notes are obviously in different registers. We'll need to be clear about which register we would like our new note to be in, so as well as saying "D" or "F", we will need to add a number for this register. By default a "4" implies the octave beginning with middle C on a piano. So tuning a note to "C4" would set it to middle C. "C3" would be the octave below that. "G3" would be the G between "C3" and "C4". 
In this terminology, a regular guitar is tuned as follows:

1. E2 (thickest string)
2. A2
3. D3
4. G3
5. B3
6. E4 (thinnest string)

We can change the tuning of our default guitar with the `tuneString()` function:
```python
my_guitar.tuneString(1, "D2")    # tune string 1 (thickest) to D2
```
This tunes our E2 down to a C2 on string 1. Now lets tune our entire guitar to DGDGCE in appropriate registers:

```python
my_guitar.tuneString(2, "G2")
my_guitar.tuneString(3, "D3")
my_guitar.tuneString(4, "G3")
my_guitar.tuneString(5, "C4")
my_guitar.tuneString(6, "E4")
```

## MIDI note notation and microtonal tuning
In the above examples the second argument to `tuneString` is a string containing a note name and a register value. We can also specify this value as a MIDI note number, e.g. 60, 64. In MIDI note number notation, middle C4 is represented by 60, and going up or down by 1 represents moving by a semitone. So 61 is C#4, 62 is D4, 72 is C5, etc. See [here](http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies) for a full list. With MIDI note number notation, a regularly tuned EADGBE guitar would look like this:

1. E2 = 40
2. A2 = 45
3. D3 = 50
4. G3 = 55
5. B3 = 59
6. E4 = 64

You can also specify fractional values, e.g. 64.75, 40.9123, etc. We already have our guitar tuned instead to D2 (38), G2 (43), D3 (50), G3 (55), C4 (60) and E4 (64). Let's tune the high strings microtonally:
```python
my_guitar.tuneString(5, 60.5)     # half way between C4 (60) and C#4 (61)
my_guitar.tuneString(6, 64.5)     # half way between E4 (64) and F4 (65)
```

Note that the approach to tuning described here may go awry with more unusal score and instrument parameters. All part of the fun.

## A Quick test score
This score adds a pluck every 0.15 seconds, iterating through the strings. It is a useful tester. It reuses the stringCout variable, so we need to make sure that that has been set properly above. For more on creating scores, see the more score-focused tutorials on the [main repository page](https://tommmmudd.github.io/ness-tools/). 

```python
# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9    # total time
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
pluckRate = 0.15
t = 0.1
i=0
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_3_score.m")
```

The full code for this tutorial is here: [gtr_instrument_3_tuning.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_3_tuning.py).

[<-- Previous Tutorial (2)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial2)  / / /  [Next Tutorial (4) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial4)

