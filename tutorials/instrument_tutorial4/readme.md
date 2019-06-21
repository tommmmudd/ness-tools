# NESS Guitar Instrument Tutorial 4
String parameters #1

In this tutorial, we will delve into the detail of how NESS strings are defined, altering parameters one-by-one to specific values.

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
print (my_guitar.strings[0].tension)
```
The [0] in this line means that we want to look at the *first* string in our instrument. This line will print the tension of the string to the terminal (which should be 12.1 for the default guitar E string).

We can look at the parameters for the second string by replacing the [0] with [1]:
```python
print (my_guitar.strings[1].tension)
```

This should output the default value of 12.3. You can edit these lines to look at any of the other parameters defined above by using the text displayed in the "Name" column.

We can set the values to new ones in a very similar way. The code below makes some changes to the instrument:
```python
# 1st string settings
my_guitar.strings[0].tension = 9.5      # less tension
my_guitar.strings[0].length = 1.0       # longer string (1 metre)
my_guitar.strings[0].radius = 0.0004    # twice as thick

# 2nd string settings
my_guitar.strings[1].tension = 20.5     # less tension
my_guitar.strings[1].length = 0.5       # short string (1 metre)
my_guitar.strings[1].radius = 0.0001    # thinner
```



The full code for this tutorial can be found in the [gtr_instrument_4_params_1.py](https://github.com/tommmmudd/ness-tools/gtr_instrument_4_params_1.py.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (3)](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial3)  / / /  [Next Tutorial (5) -->](https://tommmmudd.github.io/ness-tools/tutorials/instrument_tutorial5)
