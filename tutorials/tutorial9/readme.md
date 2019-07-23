# NESS Guitar Score Tutorial 9
Using iteration to generate more complex scores

Audio example of this code: [score_tut_9.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_9.mp3). 

The code for this tutorial can be found in the [gtr_score_9_iteration1.py](https://github.com/tommmmudd/ness-tools/gtr_score_9_iteration1.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (8)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial8)  / / /  [Next Tutorial (10) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial10)


# The while loop
This tutorial uses a code loop to add events to the score until we reach the end. We're setting up more or less as normal, but note the inclusion of the `random` module, which we will call via the letter r in our loop.
```python
from nesstools import guitar  # import the guitar module
import random as r 			      # use the random module for randomised events

numberOfStrings = 3         # how many strings should the guitar have?
T = 30                      # the total duration of our score

my_score = guitar.GuitarScore(T, numberOfStrings)
```

We will create a variable called `time` that we will use to keep count of where we are up to in our score, and to add events at that point in time:
```python
time = 1    # start at 1 second to leave a 1 second gap at the start of the file
```

We then use what is called a "while loop" to repeatedly add events to our my_score object as shown below:

```python
while time < T-6:
  # for each iteration, we'll add an event on a particular string
  # here we use the random module to create a random integer between 1 and numberOfStrings for our string number
  string = r.randint(1, numberOfStrings)
  
  # generate a random fret each time between 0 and 12
  fret = r.randint(0, 12)
  
  # we'll use the playFret function from tutorial 3:
  my_score.playFret	(string, time, fret)
  
  # we increase our current time by a quarter of a second and go around the loop again
  time += 0.25
```

This has the effect of **repeatedly running the indented code** until the condition specified at the top is met. Our condition was that the code should loop while the time variable is less than (T-6). This allows us to slowly increment the time, adding events at different time points as we go. We stop 6 seconds before we reach our maximum duration (at 24 seconds in this case).

Note the final line: `time += 0.25`. This increases our time variable by a quarter of a second on each iteration. This is ESSENTIAL! If we don't increment the time, then the while condition `time < T-6` will never be true, so the loop will never end! With this in place though, it means for each run through the loop, the time value will be 0.25 higher on each iteration. We use this to add a score event every quarter of a second.

We use the random module to choose a random string between a and our maximum of 3: `string = r.randint(1, 3)`,  where `numberOfStrings=3` remember. We also use the random module to choose a random fret between 0 and 12. This leads to a very random score - essentially the player chooses one of the three strings, chooses a random fret on that string, and slides their finger to it every quarter of a second.

You can hear the results in the audio example for this code: [score_tut_9.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_9.mp3).

Experiment for yourself. Don't forget to write the score file, and to create an instrument file with 3+ strings:

```python
my_score.write("ness_files_to_process/gtr_score_9_iteration1.m")

my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/gtr_instrument_9_iteration1.m")
```

In the next tutorial, we'll look at generating more nuanced scores with this while loop method.

The code for this tutorial can be found in the [gtr_score_9_iteration1.py](https://github.com/tommmmudd/ness-tools/gtr_score_9_iteration1.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (8)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial8)  / / /  [Next Tutorial (10) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial10)

