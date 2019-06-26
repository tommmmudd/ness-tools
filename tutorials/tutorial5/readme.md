# NESS Guitar Tutorial 4
This tutorial looks at plucking harmonics with the `playHarmonic()` function

Audio example of this code: [score_tut_5.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_5.mp3)

The code for this tutorial can be found in the [gtr_score_5_harmonics.py](https://github.com/tommmmudd/ness-tools/gtr_score_5_harmonics.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (4)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial4)  / / /  [Next Tutorial (6) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial6)

## Using `playHarmonic()`
Here we create a 3 string guitar using the default string settings and tunings (EAD):
```python
from nesstools import guitar

stringCount = 3
T = 8     

# create a string instrument object with 3 strings
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()
my_guitar.write("ness_files_to_process/gtr_score_5_harmonics.m")
```

The playHarmonic() function does two things:
-- a finger is placed very lightly over a given position on the string
-- a pluck is generated to actually sound the harmonic

This simple example is shown here that plays a 12th fret harmonic on string 1:
```python
my_score.playHarmonic(1, 0.5, 	1/2.0)   # harmonic on string 1, at time 0.5, halfway along the string (12th fret harmonic)
```
The third argument here, `1/2.0` is the position as we saw in the last tutorial. Here though it is useful to think in terms of fractions, as harmonics exist at whole number ratios, such as 1/2, 1/3, 1/4, 1/5, etc. Notice also that the denominator is specified as a floating point number, `2.0`. This is necessary for Python to create a fractional number rather than a whole number.

![Harmonics](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Moodswingerscale.svg/1920px-Moodswingerscale.svg.png)

 Below are some other harmonic events at subsequent points in time across the three strings:

```python
my_score.playHarmonic(2, 0.6, 	1/2.0)   # string 2 at t=0.6s, 12th fret harmonic (0.5)
my_score.playHarmonic(3, 0.7, 	1/2.0)
my_score.playHarmonic(1, 1.5, 	1/3.0)   # string 1 at t=1.5s, 7th fret harmonic (0.333)
my_score.playHarmonic(2, 1.6, 	1/3.0)
my_score.playHarmonic(3, 1.7, 	1/3.0)
my_score.playHarmonic(1, 2.5, 	1/4.0)   # string 1 at t=2.5s, 5th fret harmonic (0.25)
my_score.playHarmonic(2, 2.6, 	1/4.0)
my_score.playHarmonic(3, 2.7, 	1/4.0)
```

Try experimenting with different harmonic ratios on different strings. There will be more on harmonics in the next tutorial.

Audio example of this code: [score_tut_5.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_5.mp3)

The code for this tutorial can be found in the [gtr_score_5_harmonics.py](https://github.com/tommmmudd/ness-tools/gtr_score_5_harmonics.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (4)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial4)  / / /  [Next Tutorial (6) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial6)

