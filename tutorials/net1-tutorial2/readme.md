# Using the Python nesstools with Net1 - part 2
This tutorial introduces some methods to generate more complex score and instrument files with the Python nesstools module.

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/net1-tutorial1/) / / / [Back to index](https://tommmmudd.github.io/ness-tools/)

## Creating a score with a loop
It can be useful to create scores with a loop-based method, where each time the loop is run, we move forward in time by some increment and create a new event at that time point. The example below shows a simple example of this:


```python
from nesstools import net1

# general variables
stringCount = 1         # how many strings should the guitar have?
T = 8                   # how long should the piece be (in seconds)?

# create a string instrument object with 1 string and write the instrument file
my_inst = net1.Net1Instrument(stringCount)
my_inst.write("ness_files_to_process/net1_tutorial2a_inst.m")

#__________________
# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = net1.Net1Score(T, stringCount)    

t = 0
dt = 0.25

while t < T-4:
	# strike string 1 at the current time
	my_score.makeEvent(t, 1)

	# increment the current time and repeat the loop (until t > T-4)
	t += dt
  
# write the score file
my_score.write("ness_files_to_process/net1_tutorial2a_score.m")
```
The first half of the file is the setup - importing the module, setting up a default one string instrument, and writing the instrument file.

The second half looks less familiar. We use a **while loop** to continually add events to the score. This keeps looping while the condition ```(t < T-4)``` is true. We are using ```t``` to denote the time in our score, and each time we run the loop we add a fixed quantity, ```dt = 0.25``` to the time. We can then use the ```t``` variable in our ```makeEvent()``` function to indicate the current time. We end the loop at ```t>=T-4``` rather than ```t=T``` so that there is time for the last event to ring out (in practice, you will probably want to leave a bit more time than this).

In this example therefore, every quarter of a second, we will add a strike to string 1. Try pasting this script into a new file, saving it into the ness-tools-master folder and running it to produce a score and instrument files, and have a look in the score file to see the result. Try uploading this to the Ness system.

## Variation
We can create more varied events with a whole host of processes. A simple start is to randomise certain parameters. For this we will need another module: the ```random``` module. We can add this very simply alongside our ```nesstools``` module at the start of the code, so that the first two lines now look like this:

```python
from nesstools import net1
import random as r
# ...
```

We can now vary some of the parameters in the makeEvent() function, like the strength of the strike, the position, and so on. We have imported the random module "as r", which means that we can refer to the module just by the letter ```r```. Some useful functions from the random module are:
- r.random()  -  returns a random number between 0 and 1
- r.uniform(A, B)  -  returns a random number in the range A-B, e.g. r.uniform(0.3, 0.5) gives a random number between 0.3 and 0.5.
- r.randint(A, B)  -  returns a random whole number between A and B (inclusive)

The example below utilises some of these functions. We spread the parameter definitions out onto separate lines as new variables, then include the variables in the ```makeEvent()``` function:


```python
from nesstools import net1
import random as r

# general variables
stringCount = 1         # how many strings should the guitar have?
T = 8                   # how long should the piece be (in seconds)?

# create a string instrument object with 1 string and write the instrument file
my_inst = net1.Net1Instrument(stringCount)
my_inst.write("ness_files_to_process/net1_tutorial2b_inst.m")

#__________________
# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = net1.Net1Score(T, stringCount)    

t = 0
dt = 0.25

while t < T-4:
	stringNum = r.randint(1, stringCount)		# which string to play
	strength = r.uniform(0.25, 2.0)				# how hard to strike/pluck
	pos = r.uniform(0.5, 0.99)					# where to strike/pluck
	eventType = r.randint(0, 1)  				# 0 is strike, 1 is pluck

	# add an event to the score at the current time, with the above settings
	my_score.makeEvent(t, stringNum, strength, pos, eventType)

	# increment the current time
	t += dt
  
my_score.write("ness_files_to_process/net1_tutorial2b_score.m")
```
Note that if you change the score duration ```T``` the score will adapt, so if T was set to 30 seconds, we would get continuous strikes for 26 seconds, then 4 seconds of the strings ringing out. Experiment with your own uses of the random functions and ranges for generating scores. You might also want to try altering the value of ```dt``` within the loop for rhythmic variation. You can obviously include more than one ```makeEvent()``` per cycle in the loop for multiple simultaneous events (e.g. several string strikes).

## Generative Instruments
We can apply the above techniques to instrument generation too. Instead of the while loop, we use a **for loop**, because we want to do things like iterate through all of the different strings, or add a fixed number of connections. Have a look at the following example (we are only looking at the instrument generation here):

```python
from nesstools import net1
import random as r

# general variables
stringCount = 6         # how many strings should the guitar have?
T = 8                   # how long should the piece be (in seconds)?

# create a string instrument object with 1 string and write the instrument file
my_inst = net1.Net1Instrument(stringCount)
for string in my_inst.strings:
  string.length = r.uniform(0.5, 1.5)
  string.radius = r.uniform(0.0001, 0.0006)
  
my_inst.write("ness_files_to_process/net1_tutorial2c_inst.m")
```

In this example, we loop through each string in the instruments ```strings``` array, randomising the length and radius for each. Note that this will work whatever we set the ```stringCount``` to, from 1 string to 100 strings.

We can apply the same logic to creating or modifying connections:

```python
for i in range(5):
  stringA = r.randint(1, stringCount)
  stringB = r.randint(1, stringCount)
  rattleDistance = r.uniform(0.00005, 0.001)
  my_inst.addConnection(stringA, stringB, rattleDistance=rattleDistance)
```

Here we add a fixed quantity of connections (5) between randomly chosen strings, also randomising the rattle distance parameter. Make sure you include this code **before** the ```write()``` function for the score.

These are relatively simple examples, but you can take these processes a lot further, creating potentiall much more complicated structures and processes to output to the NESS models.

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/net1-tutorial1/) / / / [Back to index](https://tommmmudd.github.io/ness-tools/)
