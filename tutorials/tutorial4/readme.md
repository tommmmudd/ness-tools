# NESS Guitar Tutorial 4
This tutorial looks at adding finger events to the score with the `playPosition()` function.

Audio example of this code: [score_tut_4.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_4.mp3)

The code for this tutorial can be found in the [gtr_score_4_playPosition.py](https://github.com/tommmmudd/ness-tools/gtr_score_4_playPosition.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (3)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial3)  / / /  [Next Tutorial (5) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial5)

## Setting up
The `playPosition()` function is very similar to the `playFret()` that we used in our previous tutorial, except that we specify the exact position of the finger on the string. This means that you can specify a very precise position to the finger instead of a fret position. This can be useful for a range of things, including the potential to do work with just intonation tunings with fretless instruments. Here we set up a two string instrument with the usual process:

```python
from nesstools import guitar

stringCount = 2
T = 8					# total time
my_score = guitar.GuitarScore(T, stringCount)  
```

## Fretless guitar with two identical strings
We will use a fretless guitar for this example, set up with two identical low E strings. See the instrument tutorials for more information on setting up the guitar.

```python
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar()
my_guitar.setRegularString(0, 0)	# set both the first and second string to be the same low E string
my_guitar.setRegularString(1, 0)
my_guitar.frets = False
my_guitar.write("ness_files_to_process/gtr_instrument_4_fretless.m")
```

Note that the frets are set to `False` so that there are no frets, and we can place a finger anywhere on the string to get a precise pitch. Let's set up a score file that takes advantage of microtonal differences in position.

## playPosition()
To specify position to `playPosition()` we give a position value (0-1) instead of a fret value. We do this alongside a string number and a time value. The example below places a finger half way along the first string at 0.25 seconds (12th fret), and a finger at a third of the way along the second string at 0.5 seconds (7th fret).

```python
my_score.playPosition	(1, 	0.25,   0.5)		  # finger at pos 0.5, at time 0.25 on string 1 
my_score.playPosition	(2, 	0.5,   	0.333)	  # finger at pos 0.333, at time 0.5 on string 2
```
The fingers in this case are exactly where the frets would be. Let's try something more interesting:

```python
my_score.playPosition	(1, 1, 0.25, 0.3, 5)   # finger at pos 0.25 on string 1, at time=1s, glide time of 0.3s, finger force of 5N
my_score.playPosition	(2, 1.5, 0.251, 1.3, 5)   # finger at pos 0.251 on string 2, at time=1.5s, glide time of 1.3s, finger force of 5N				
```
The finger placements are very close - the first is a pure majord third above the string root. The second is an equal tempered majord third above the string root. We can here the two beat against each other. Here we also make use of the additional glide time and finger force parameters, as we did in the last tutorial.

You can listen to this example here: [score_tut_4.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_4.mp3)

Now we just write the score file to try this out as usual
```python
my_score.write("ness_files_to_process/gtr_score_4.m")
```

The code for this tutorial can be found in the [gtr_score_4_playPosition.py](https://github.com/tommmmudd/ness-tools/gtr_score_4_playPosition.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (3)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial3)  / / /  [Next Tutorial (5) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial5)


