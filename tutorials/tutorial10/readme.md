# NESS Guitar Score Tutorial 10
More with iteration

Audio example of this code (custom tab): [score_tut_10.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_10.mp3). 

The code for this tutorial can be found in the [gtr_score_10_iteration2.py](https://github.com/tommmmudd/ness-tools/gtr_score_10_iteration2.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (9)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial9)  / / /  [Next Tutorial (11) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutoria11)

# Refined fret selection
We will build on the last tutorial, but make our events a bit less random, and a bit more informed by the nature of our guitar. We are going to create a map of the guitar to allow us to target specific frets in a specific scale. Below we set up variables to store our map of the guitar:

```python
# E MINOR - frets for strings
s1Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # low E string
s2Frets = [0, 2, 3, 5, 7, 9, 10, 12]  # A
s3Frets = [0, 2, 4, 5, 7, 9, 10, 12]  # D
s4Frets = [0, 2, 4, 5, 7, 9, 11, 12]  # G
s5Frets = [0, 1, 3, 5, 7, 8, 10, 12]  # B
s6Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # E
```
Each of these six variables holds a list of fret numbers for an E minor scale up to the 12th fret [See here for more scale maps](https://jguitar.com/scale/E/Aeolian). We then make a single `allFrets` variable that combines these six strings into one 2 dimensional list. If the concept of a 2 dimensional list sounds strange, that is understandable! Hopefully it will be a little clearer when we use the list below though.

```python
# compile the strings into a single variable
allFrets = [s1Frets, s2Frets, s3Frets, s4Frets, s5Frets, s6Frets]
```

We can now access a particular position on a particular string and know that we will be in the scale of E minor still. For example, we could choose the 4th position on the 1st string as follows:
```python
fret = allFrets[0][3]   # first string (0), fourth usable fret position (3)
```
In this case, the fret variable would be set to 5, because that is the 4th entry in the list for the first string. Note that the indexes start from 0 rather than 1, so the first string would be 0, the second string is 1, etc. The same goes for the fret positions.

We can now use this in our for loop.

# Fret selection in the while loop
First, let's set up, including our new code for storing fret positions for different strings:

```python
from nesstools import guitar
import random as r 			# use the random module for randomised events

numberOfStrings = 6         # how many strings should the guitar have?
T = 60

my_score = guitar.GuitarScore(T, numberOfStrings)

# E MINOR - frets for strings
s1Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # low E string
s2Frets = [0, 2, 3, 5, 7, 9, 10, 12]  # A
s3Frets = [0, 2, 4, 5, 7, 9, 10, 12]  # D
s4Frets = [0, 2, 4, 5, 7, 9, 11, 12]  # G
s5Frets = [0, 1, 3, 5, 7, 8, 10, 12]  # B
s6Frets = [0, 2, 3, 5, 7, 8, 10, 12]  # E
allFrets = [s1Frets, s2Frets, s3Frets, s4Frets, s5Frets, s6Frets]

```

Now let's add our while loop which will choose from these fret positions:

```python
time = 1		# our current time variable that we will increase until we hit our maximum

while time < T-6:
  # we will still randomly select our string number
  string = r.randint(1, numberOfStrings)
  
  # now we use our randomly chosen string number to get a relevant fret for that string
  # there are 8 possible frets in each string, so we pick one with the r.randint(0, 7)
  fret = allFrets[string-1][r.randint(0, 7)]
  
  # we'll use the playFret function from tutorial 3:
  my_score.playFret	(string, time, fret)
  
  time += 0.25
```

The only line here that differs from the last tutorial is the fret line. We use the selected string (-1 because we need it to start at 0) to choose from the appropriate string list, then create a random integer between 0 and 7 using the random module. This should then give us random notes in the key of E minor.

# Rhythm control
We can use a similar process for rhythm. Let's say we have a specific rhythm that we want to use to play the notes in, instead of triggering one every quarter of a second. As we did with the frets, we can define a list of timing values as follows:

```python
# a quarter-second followed by two eighth-second events
rhythm = [0.25, 0.125, 0.125]
```

This gives us something like a crotchet followed by two quavers (0.125 is half of 0.25). We will need to modify our while loop a little to use this rhythm:

```python
time = 1		# our current time variable that we will increase until we hit our maximum
count = 0		# our iteration counter

while time < T-6:
  # we will still randomly select our string number
  string = r.randint(1, numberOfStrings)
  
  # now we use our randomly chosen string number to get a relevant fret for that string
  # there are 8 possible frets in each string, so we pick one with the r.randint(0, 7)
  fret = allFrets[string-1][r.randint(0, 7)]
  
  # we'll use the playFret function from tutorial 3:
  my_score.playFret	(string, time, fret)
  
  # which rhythm do we want from our list (in our case, 0, 1 or 2)
  # we use the modulo to wrap the count so that it can't be higher that the length of the rhythm.
  # for our 3-step rhythm, this means we get 0, 1, 2, 0, 1, 2, 0... as the index
  rhythmIndex = count % len(rhythm)
  
  # we then use our rhythmIndex to select the appropriate rhythm value from the rhythm list:
  time += rhythm[rhythmIndex]

  # increment our counter
  count += 1
```

As well as the rhythm variable, we introduce the `count` variable. A little like the time parameter, we add to it on every iteration. In this case we only add 1 each time, so that we know how many iterations we have had. We can then use the counter to determine which rhythm value we should use. The `%` sign means "modulo" and wraps our counter into a range defined by the length of the list. For our three step list that means that if `count=3` our `rhythmIndex=0`, if count=4, the index is 1, if the count is 5, the index is 2, if the count is 6, the index is 0, and so on. It basically allows our count to count up from 0 to whatever, but our index cycles roud: 0,1,2,0,1,2,0,1,2... etc. We then use the rhythmIndex to call our the appopriate rhythm value from the list and add it to our time variable.

# Experimenting
Try your own scales and rhythms. Note that if you use more or less than 8 frets per string for your scale, you will have to adapt the r.randint(0, 7) line accordingly. You might want to change this line so that it automatically selects from within the range of frets available for the selected string. You could do that as follows:

```python
  # how many frets have been defined above for the selected string?
  # note the (-1) because if we have 8 strings, we want to select from 0-7
  fretCountForString = len(allFrets[string-1]) - 1
  fret = allFrets[string-1][r.randint(0, fretCountForString)]
```

In the next two tutorials we will look at some more piece-like examples that expand on some of these principles.

Audio example of this code (custom tab): [score_tut_10.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_10.mp3). 

The code for this tutorial can be found in the [gtr_score_10_iteration2.py](https://github.com/tommmmudd/ness-tools/gtr_score_10_iteration2.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (9)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial9)  / / /  [Next Tutorial (11) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutoria11)
