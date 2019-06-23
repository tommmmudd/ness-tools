# NESS Guitar Instrument Tutorial 4
String parameters #1

In this tutorial, we will delve into the detail of how NESS strings are defined, altering parameters one-by-one to specific values.

Audio example of this code: [inst_tut_4.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_4.mp3)

The code for this tutorial can be found in the [gtr_instrument_4_params_1.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_4_params_1.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (3)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)  / / /  [Next Tutorial (5) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)

## String Parameters
We will work with a 2 string instrument here, and make some changes to a range of parameters relating to these strings.

```python
from nesstools import guitar

stringCount = 2
my_guitar = guitar.StringInstrument(stringCount)
my_guitar.defaultGuitar()   # set our 2 string to the default low E and A
```

This string has 9 parameters associated with it that we can tweak. The table below outlines these:

| Name | Description | Default Value |
| --- | --- | --- |
|`length` | string length in metres | 0.68 |
| `ym` | Young's modulus in pascals | 2e11 |
| `tension` | string tension in Newtons | 12.1 |
| `radius` | string radius in metres | 0.0002 |
| `density` | string density in kg/m^3 | 7850 |
| `lowDecay` | decay time T60 for lower frequencies | 15 |
| `highDecay` | decay time T60 for higher frequencies | 5 |
| `outputPos` | the point at which a reading is taken for output - akin to the pickup position of an electric guitar (0-1)| 0.89 |
| `pan` | stereo position for the mixed stereo output file (doesn't affect the individual channel output) | randomised by default for each string |

The default values given here are for our low E string.

In this tutorial we will look at three of the first four parameters: `length`, `tension`, and `radius` (ignoring Young's modulus).

## Getting and Setting string parameters
We can access and change any of these values via the StringInstrument object. Our string instrument is called `my_guitar`. This object has a variable called `strings` which contains an array of all our strings as instances of the NessString object. Different string variables can be accessed by referencing the specific string in the array and naming the parameter. Let's look at an example:

```python
print (my_guitar.strings[0].radius)
```
The [0] in this line means that we want to look at the *first* string in our instrument. This line will print the radius of the string to the terminal (which should be 0.0002 for the default guitar E string).

We can look at the parameters for the second string by replacing the [0] with [1]:
```python
print (my_guitar.strings[1].radius)
```

This should output the default value of 0.00015 (the A string is slightly thinner). You can edit these lines to look at any of the other parameters defined above by using the text displayed in the "Name" column.

We can set the values to new ones in a very similar way. The code below makes some changes to the instrument:
```python
# 1st string settings
my_guitar.strings[0].tension = 9.5      # less tension
my_guitar.strings[0].length = 1.0       # longer string (1 metre)
my_guitar.strings[0].radius = 0.0004    # twice as thick

# 2nd string settings
my_guitar.strings[1].tension = 20.5     # more tension
my_guitar.strings[1].length = 0.5       # short string (1 metre)
my_guitar.strings[1].radius = 0.0001    # thinner
```

Try your own parameter settings out. You can also try out creating more strings and referencing them with higher indexes: strings[2], strings[3], etc. We will look at some of the other parameters in the next tutorial.

## Test Score
We are reusing our test score generator from the last tutorial. Here it should create a score for our two string instrument, and alternate between plucking the two strings.

```python
# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9    # total time
my_score = guitar.GuitarScore(T, stringCount)       

# here we create a plucking sequence where each string is plucked in turn, until we are 4 seconds from the end of the score
# the pluck rate is the gap between plucks (in seconds)
pluckRate = 0.2
t = 0.1
i=0
while t < (T-4):
	s = i%stringCount
	my_score.pluck(s+1, t)
	i += 1
	t += pluckRate

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_4_score.m")
```

The full code for this tutorial can be found in the [gtr_instrument_4_params_1.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_4_params_1.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (3)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)  / / /  [Next Tutorial (5) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)
