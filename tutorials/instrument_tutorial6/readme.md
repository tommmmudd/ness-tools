# NESS Guitar Instrument Tutorial 6
Customising the frets and the fretboard.

Audio example of this code: [inst_tut_6.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_6.mp3)

The code for this tutorial can be found in the [gtr_instrument_6_backboard.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_6_backboard.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (5)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)  / / /  [Next Tutorial (7) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial7)

## The fretboard
There are three parameters that can be controlled that determine the offset, slope and curvature of the fretboard below the strings. These parameters make up a quadratic curve for the fretboard of the form:

> ![Backboard equation](http://tommudd.co.uk/ness/images/ness_backboard_equation.png)

We can specify b0 (offset), b1 (slope) and b2 (curvature) with the backboardParams parameter. Note that they are usually negative - below the strings. If b1 and b2 are 0, we have a flat fretboard as shown below:

![Flat backboard](http://tommudd.co.uk/ness/images/ness_backboard_flat.png)

In this example, b0 is set to -0.001 (metres), which corresponds to a fretboard that is 1mm below the strings. On the graph, the strings are at y=0 (the horizontal axis), so when a finger is placed on a string, the string is pushed down against the green line.

We can have the fretboard begin to slope linearly away from the strings by introducing a b1 parameter (in this case, also -0.001):

![Linear backboard](http://tommudd.co.uk/ness/images/ness_backboard_linear.png)

Finally, if we want the fretboard to curve away, we can set a value for b2. In the below example, b1 is again 0, and b2 is -0.002 to produce quite an extreme curve away from the strings:

![Curved backboard](http://tommudd.co.uk/ness/images/ness_backboard.png)

Note that with the defaultGuitar instrument we have been using, the default shape is b0=-0.002, b1=0, b2=-0.0002. You can change the fretboard parameters by altering the backboardParams for the GuitarInstrument object as shown here:

```python
from nesstools import guitar

stringCount = 2
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()  # set our two strings to default E and A

my_guitar.backboardParams = [-0.001, 0, -0.0002]   # set the backboard params for b0, b1 and b2 respectively
```

You can replace these values with your own. The parameters are specified in the list in order `[b0, b1, b2]`.

## The frets
In addition to the backboard, we can specify the height of the frets. By default, there are 20 frets at a height of -0.001m. Note that the fret height must be less than 0 (the string position), but greater than the height of the fretboard, otherwise the frets will have no effect. The image below gives an idea of how the fretHeight parameter relates to the fretboard parameters:

![Fret height parameter](http://tommudd.co.uk/ness/images/ness_frets.png)

Note that the axis on the diagram are not on the same scale, so this image is giving an exaggerated vertical profile of the fretboard and frets. We can set the height with the fretHeight parameter as shown below:

```python
my_guitar.fretHeight = -0.0005    # raise the frets away from the backboard towards the strings
```

Finally, note that you can remove the frets from the simulation completely with the following line:
```python
my_guitar.frets = False    # note that the word 'False' must have a capital 'F'!
```

## Comparing parameters
The script below (and linked to as the code for this tutorial) creates five different 2-string instruments with different fretboard and fretHeight settings. A score file that plays a short test pattern is also created for use with all five instrument files. Listen to the audio example to hear them: [inst_tut_6.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_6.mp3).

```python
from nesstools import guitar

stringCount = 2
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar() 

my_guitar.backboardParams = [-0.00002, 0, -0.000002]   # fretboard is very close to the strings!
my_guitar.fretHeight = -0.00001
my_guitar.write("ness_files_to_process/inst_6a_instrument.m")  # write instrument 6a

my_guitar.backboardParams = [-0.0002, 0, -0.00002]
my_guitar.fretHeight = -0.0001
my_guitar.write("ness_files_to_process/inst_6b_instrument.m")  # write instrument 6b

my_guitar.backboardParams = [-0.002, 0, -0.0002]     # default parameters in the defaultGuitar() instrument
my_guitar.fretHeight = -0.001
my_guitar.write("ness_files_to_process/inst_6c_instrument.m")  # write instrument 6c

my_guitar.backboardParams = [-0.02, 0, -0.02]
my_guitar.fretHeight = -0.01
my_guitar.write("ness_files_to_process/inst_6d_instrument.m")  # write instrument 6d

my_guitar.backboardParams = [-0.2, 0, -0.02]       # fretboard is very very far away from the strings!
my_guitar.fretHeight = -0.1
my_guitar.write("ness_files_to_process/inst_6e_instrument.m")  # write instrument 6e

#___________________________________
# create a test score file
T = 12                      # total time
my_score = guitar.GuitarScore(T, stringCount)       


# alternating picking pattern
pluckRate = 0.333
t = 0.1
i=0
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate

# open strings for first third of the score, then move the fingers to 7th fret on both strings
my_score.playFret([1, 2], 0.05, [0, 0])
my_score.playFret([1, 2], T/3, [7, 7])

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_6_score.m")
```

Some things you can hear in these recordings:
- with instrument 6a, the frets/fretboard are so close to the strings that there is barely any pitched sounds
- 6b is still rattly, but sounds more like a realistic rattly guitar.
- 6c is our default
- 6d and 6e have no rattle, but introduce a strange artifact in the moving of the fingers, due to the extreme fretboard distances



Audio example of this code: [inst_tut_6.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_6.mp3)

The code for this tutorial can be found in the [gtr_instrument_6_backboard.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_6_backboard.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (5)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)  / / /  [Next Tutorial (7) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial7)

