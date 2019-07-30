# NESS Guitar Instrument Tutorial 5
String parameters #2

This tutorial looks at some of the other string properties

Audio example of this code: [inst_tut_5.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_5.mp3)

The code for this tutorial can be found in the [gtr_instrument_5_params_2.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_5_params_2.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (4)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial4)  / / /  [Next Tutorial (6) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial6)

## String decay settings

In the last tutorial, we looked at the radius, tension and length of the strings. We will look here at three more parameters: lowDecay, highDecay and outputPos listed towards the end of the table below.

| Name | Description | Default Value |
| --- | --- | --- |
|`length` | string length in metres | 0.68 |
| `ym` | Young's modulus in pascals | 2e11 |
| `tension` | string tension in Newtons | 12.1 |
| `radius` | string radius in metres | 0.0002 |
| `density` | string density in kg/m^3 | 7850 |
| **`lowDecay`** | decay time T60 for lower frequencies | 15 |
| **`highDecay`** | decay time T60 for higher frequencies | 5 |
| **`outputPos`** | the point at which a reading is taken for output - akin to the pickup position of an electric guitar (0-1)| 0.89 |
| `pan` | stereo position for the mixed stereo output file (doesn't affect the individual channel output) | randomised by default for each string |

The decay settings are *time* values that specify how long it takes for lower and higher frequencies to decay to 60dB below their original sound pressure level. You can experiment with these paremeters, but you should remember one important rule:

> **Make sure the highDecay is less than or equal to the lowDecay**

Otherwise you may get no audio, an abrupt end to the audio file, or glitchy rattling sounds (where the highDecay is only slightly above the lowDecay).

Below we will create an instrument file and a score file that lets us compare different settings.

## Decay comparison
First, we create quite a specific instrument: one that has four identical strings (rather than the four default strings from a guitar: EADG). We do this so that we can test different decay settings, not different radius, tension and other settings. We do this with the setRegularString() function that assigns a given string number to a given template string from the defaultGuitar. Below we set each of the four strings (0, 1, 2, 3) to be the default for the low E string (0).

```python
from nesstools import guitar

stringCount = 4
my_guitar = guitar.StringInstrument(stringCount)

# set all four strings to be low E strings with the 
my_guitar.setRegularString(0, 0)
my_guitar.setRegularString(1, 0)
my_guitar.setRegularString(2, 0)
my_guitar.setRegularString(3, 0)
```

We can now assign each of the four strings different decay settings:

```python
#1st string settings (remember first string index is 0)
my_guitar.strings[0].lowDecay = 2      # very short decay times - the string will sound muted
my_guitar.strings[0].highDecay = 1

# 2nd string settings
my_guitar.strings[1].lowDecay = 5      # short decay times - the string will sound muted
my_guitar.strings[1].highDecay = 2      

# 3rd string settings
my_guitar.strings[2].lowDecay = 15      # default decay times
my_guitar.strings[2].highDecay = 5

# 4th string settings
my_guitar.strings[3].lowDecay = 70      # long decay times
my_guitar.strings[3].highDecay = 35
```

## Creating a score to play the four strings
To test our four strings, we pluck each string a few times using the pluck() function described in (https://tommmmudd.github.io/ness-tools/tutorials/tutorial1/)[first score tutorial]:

```python
T = 40                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# pluck string 1 a few times
my_score.pluck(1, 0.1)        # remember that the numbers here represent string number (1) and time (0.1)
my_score.pluck(1, 0.5)
my_score.pluck(1, 1.5)

# wait a bit, then pluck string 2 a few times
my_score.pluck(2, 4.1)
my_score.pluck(2, 4.5)
my_score.pluck(2, 5.5)

# wait a bit, then pluck string 3 a few times
my_score.pluck(3, 8.1)
my_score.pluck(3, 8.5)
my_score.pluck(3, 9.5)

# wait a bit, then pluck string 4 a few times
my_score.pluck(4, 15.1)
my_score.pluck(4, 15.5)
my_score.pluck(4, 16.5)

# write our score file
my_score.write("ness_files_to_process/inst_5_score.m")
```

## Pickup position
Before we finalise our instrument file, we will also experiment with the outputPos parameter. This determines a point on the string at which to take a reading for the output audio file. In practice, this works a lot like the pickup position on an electric guitar, or the microphone placement on an acoustic guitar. The value is a number between 0 and 1, where 0 is right down at the nut, and 1 is at the bridge. In practice, you will probably want the outputPos to be larger than any fret positions, and you may also want to avoid the exact values of pluck positions (the default position for the pluck funciton is 0.8).

We assign the four different strings different positions as follows:
```python
my_guitar.strings[0].outputPos = 0.95	# pickup position is very close to the bridge
my_guitar.strings[1].outputPos = 0.87   # pickup position is quite close to the bridge
my_guitar.strings[2].outputPos = 0.72   # pickup position is nearer 19th fret
my_guitar.strings[3].outputPos = 0.5   # pickup position is at 12th fret!
```

Note that the settings for strings 0 and 3 are quite extreme! Experiment with your own settings. Make sure you write the instrument file at the end of your Python script.

```python
my_guitar.write("ness_files_to_process/inst_5_instrument.m")
```


Audio example of this code: [inst_tut_5.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/inst_tut_5.mp3)

The code for this tutorial can be found in the [gtr_instrument_5_params_2.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_5_params_2.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (4)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial4)  / / /  [Next Tutorial (6) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial6)
