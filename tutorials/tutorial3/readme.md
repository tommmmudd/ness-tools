# NESS Guitar Tutorial 3
Putting fingers on frets with playFret()


This tutorial looks at:

1. adding finger events to the score with the `playFret()` function.
2. finger slides and finger force as extra parameters

The code for this tutorial can be found in the [gtr_score_3_fingers_and_frets.py](https://github.com/tommmmudd/ness-tools/gtr_score_3_fingers_and_frets.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (2)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial2)  / / /  [Next Tutorial (4) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial4)

## Setting up
Here, we will import the nesstools guitar module, and set up for a single string instrument over 8 seconds:
```python
from nesstools import guitar

stringCount = 1
T = 8					# total time

my_score = guitar.GuitarScore(T, stringCount)  
```

## Moving fingers
We won't specify any plucks in this score - just finger movements <sup>[1](#footnote1)</sup>. We'll do this with the score objects `playFret()` function:

```python
#             string num, time, fret_num
my_score.playFret		(1, 	0.2,   	2)	
```
This function requires at least three arguments:

1. string number (1, 2, 3, ...)
2. time (seconds)
3. fret number (an integer from 0 to a maximum of 20 in the default instrument)

Let's add another event moving the finger on string 1 to fret 7:
```python
my_score.playFret		(1, 	0.5,   	7)		# this says to move a finger on string 1 to fret 7 at 3 seconds
```

## Glide time and finger force
The way that the finger moves from one fret to another can be very important. In these tutorials we won't be lifting the finger off the string to move it to a new location, but will just slide the finger along, maintaining the downward force on the string. We can control the rate of the movement though, with very fast movements being heard as almost percussive events, and slower movements being heard as a finger slide. The `playFret()` function can take an additional two parameters:

4. glide time (in seconds). Default: 0.005
5. finger force (in Newtons). Default: 2

Below, we add two more events that use these parameters in different ways:

```python
#					string num, time (s), fret_num   glide time (s)		finger force (Newtons - onto string)
my_score.playFret		(1, 	2, 			4,  		0.1,			0.5)			
my_score.playFret		(1, 	3, 			2, 			1.9, 			8)		
```

## Writing files
As ever, you will need to then write your score file, e.g.
```python
my_score.write("ness_files_to_process/gtr_score_3.m")
```
And create a corresponding guitar instrument (again, we are using the default guitar, but feel free to change this to any 1-string guitar by looking at the instrument tutorials)
```python
# create a string instrument object with 1 string
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/gtr_instrument_3.m")
```

In the next tutorial (4), we will look at specifying absolute position on the fretboard rather than a fret number.

___
<a name="myfootnote1">[1]</a> *Note that a very gentle pluck is added by the nesstools module if no pluck is found, otherwise the NESS UI will not allow the file to be processed!*

[Back to index](https://tommmmudd.github.io/ness-tools/) 

[<-- Previous Tutorial (2)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial2)  / / /  [Next Tutorial (4) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial4)

