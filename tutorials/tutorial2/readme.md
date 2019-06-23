# NESS Guitar Tutorial 2
Plucking with more control

This tutorial looks at how to specify additional parameters to the `pluck()` function

Audio example of this code: [score_tut_2.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_2.mp3)

The code for this tutorial can be found in the [gtr_score_2_more_plucks.py](https://github.com/tommmmudd/ness-tools/blob/master/gtr_score_2_more_plucks.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/tutorial1)  / / /  [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial3)

## Setting up
As in the last tutorial, we will import the nesstools module, create two global variables, and create our GuitarScore object:

```python
from nesstools import guitar

stringCount = 2
T = 8					# total time

my_score = guitar.GuitarScore(T, stringCount)  
```
As in the last tutorial, we have two strings, but this time our duration, T, is a bit longer: 8 seconds. We can add a simple pluck to this as we did in the last tutorial:

```python
my_score.pluck( 1, 1 )
```

## Advanced plucking
The `pluck()` function can take additional arguments to specify other parameters beyond string number and time. The full range of arguments is as follows:

1. string number (1, 2, 3 ...)
2. time (in seconds)
3. pluck position (from 0 - 1.0 where e.g. 0.75 would mean that the pluck takes place 75% of the way from the nut to the bridge). Default: 0.8
4. pluck duration (in seconds). Typically this will be a very small value. Default: 0.001
5. pluck force (in Newtons). Default: 0.3

Let's add a pluck to the score with some different settings
```python
my_score.pluck( 1, 2, 0.95, 0.0005, 0.5 )
```

This adds a pluck to the score on string 1, at time=2 seconds, at a position of 0.95 (very close to the bridge), with a short duration of 0.0005, and a slightly stronger force of 0.5 Newtons.

You may want to set up variables for this to make things more legible or accessible. E.g. here is a third pluck event in the score at 3 seconds

```python
string = 2		# pluck the first string (lowest, rather than highest)
time = 3			# pluck at 3 seconds in the score
pluckPosition = 0.65		# pluck 80% of the way from the nut to the bridge
pluckDuration = 0.0005	# pluck duration in seconds - the duration of the force on the string
pluckForce = 0.05		# pluck force in Newtons

# create a pluck event with the above parameters
my_score.pluck( string, time, pluckPosition, pluckDuration, pluckForce )
```

## Writing the score
As in the last tutorial, the final step is to add a line to write the score to a file:

```python
my_score.write("ness_files_to_process/example2_basic_score.m")
```

You can then run this on the NESS system with the guitar from the last tutorial (as both scores assume 2 strings), or you can create and write an instrument as shown below.

```python
# create a string instrument object with 2 strings
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/example2_basic_guitar.m")
```

In the next tutorial (3), we will look at adding fingers to the strings at particular frets.

____

[Back to index](https://tommmmudd.github.io/ness-tools/) 

[<-- Previous Tutorial (1)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial1)  / / /  [Next Tutorial (3) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial3)
