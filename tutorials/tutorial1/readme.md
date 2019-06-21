# NESS-tools Tutorial 1

This tutorial looks at:

1. how to set score and instrument objects
2. how to add basic pluck instructions to the score
3. how to write the score and instrument objects to NESS-compatible files (.m)

The code for this tutorial can be found in the [gtr_score_1_basic_plucks.py](https://github.com/tommmmudd/ness-tools/blob/master/gtr_score_1_basic_plucks.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

## First things first
The first step in working with the NESS tools is to import then into the Python script as shown below.

```python
from nesstools import guitar
```
We will show how this is used in creating the score and instrument objects below. Before we do that though, we will set up two key variables that relate to our score and instrument, the number of strings the instrument will have, and the duration of the score.

```python
stringCount = 2       # number of strings on the instrument
T = 5					        # total time
```

## Creating a Score object
We can now use the imported nesstools library to create a new GuitarScore object for an instrument with a given number of strings and a fixed duration:
```python
my_score = guitar.GuitarScore(T, stringCount)     # creates a score file using the imported lib and the two variables defined above
```
You can see how the time variable, T, and the number of strings variable, stringCount, are used in the definition of the GuitarScore object.

### Adding events to the score
Let's pluck each of our two strings. 
```
my_score.pluck( 1, 0.5 )  # pluck string 1 (thickest string by default), at 0.5 seconds
my_score.pluck( 2, 1.0 )  # pluck string 2 at 1.5 seconds
```
We called our GuitarScore object "my_score", so we can use the pluck() function by calling "my_score.pluck( string_num, time )" as shown above.

### Writing our score file for the NESS system
We now have a complete (if simple) score. We can output this as a NESS-compatible score file by using "my_score.write()" and specifying a file name inside the brackets.
```python
my_score.write("ness_files_to_process/example1_basic_score.m")
```
Note that the filename is a string, so must be enclosed within quotes. In this example, we write our score file into the "ness_files_to_process" folder with the filename "example1_basic_score.m". The score is ready to process, but first we'll need a corresponding instrument file.

## Creating an Instrument object
Defining an instrument is a similar process:
```python
my_guitar = guitar.StringInstrument(stringCount)
```
We call our StringInstrument object "my_guitar" and tell it how many strings it has using the "stringCount" variable (2). For this tutorial, we will just use the default guitar instrument (a steel string-like instrument). Since we have two strings, this will default to the low E string and A string.
```python
my_guitar.defaultGuitar()   # set the strings to those of the default guitar prototype
```
### Writing our instrument file for the NESS system
As with the score, the instrument can be written with the "write()" function:
```python
my_guitar.write("ness_files_to_process/example1_basic_guitar.m")
```
This writes the instrument file to a .m file for use with the ness system, as described on the [main page](https://tommmmudd.github.io/ness-tools/).

That should be all you need to create a very simple audio file through the NESS System.
