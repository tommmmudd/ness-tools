# Using the Python nesstools with Net1 - part 1
This tutorial introduces the Python nesstools for generating instruments and score files. We will look at setting up and a basic example. This is the same process employed in the NESS guitar tutorials below.

[<-- Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/net1-tutorial2/)

## Getting Started
If you are on Linux or OS X, you should already have Python installed and ready. If you are on Windows, you will need to [download and install the latest release](https://www.python.org/downloads/windows/). 

You will also need to download [this repository](https://github.com/tommmmudd/ness-tools) to use the nesstools. Use the "Clone or Download" button to get these files, and place the folder somewhere appropriate on your computer.

## A quick test
You can check that Python and the nesstools are working together happily by using Terminal or the Windows command prompt to navigate to the "ness-tools-master" folder that you downloaded. Once you are there, run the following line:
```bash
python installation_test.py
```

This should create two files in the "ness_files_to_process" folder called "test_score.m" and "test_instrument.m". Upload these to the NESS system to check that everything works ok. You should get a very short single string pluck.

## Using the nesstools module
To get started using the module for your own creations, you will need to have a text editor such as Sublime Text, Atom, TextWrangler, etc. You can also use notepad or TextEdit, but you will not get any syntax colouration.

Save a blank file as something like ```net1_tutorial1.py``` in the ness-tools-master folder (the ```.py``` extension is important).
At the top of the file we will import the net1 module from the nesstools. This should look like this:

```python
from nesstools import net1
```

It is also useful to set up some initial variables for our instrument and score, such as the total duration, and the number of strings:
```python
# general variables
stringCount = 2         # how many strings should the guitar have?
T = 3                   # how long should the piece be (in seconds)?
```

### Creating a Net1Instrument object
We will create an instance of the ```Net1Instrument``` class. This holds all the settings for our instrument. The class needs to know how many strings there are, so we pass in the ```stringCount``` variable
```python
# create a string instrument object
my_inst = net1.Net1Instrument(stringCount)
```

The variable ```my_inst``` here is our instance of the ```Net1Instrument```. The class defaults to setting up regular guitar strings, so we have a guitar E string and an A string as our two strings. We can access the string parameters individually though to make changes, e.g.
```python
my_inst.strings[0].length = 1.36   # set the first string to 1.36 metres
my_inst.strings[1].lowDecay = 12  # set the t60 for lower frequencies of the second string to 12 seconds
```
The [0] and [1] denote the string index, starting from zero, so 0 refers to the first string, 1 to the second string, and so on. The parameter names for the string are as follows (corresponding to the parameters described in the first net1 tutorial):
- length
- material
- tension
- radius
- lowDecay
- highDecay

We can also add and modify connections between strings. By default there are no connections, but we can add them with the ```addConnection()``` method:
```python
my_inst.addConnection(1, 2)   # add a connection between strings 1 and 2 with default parameters
my_inst.addConnection(1, 2, mass=0.0001)   # add a connection with a specific mass

# add a connection specifying all parameters
my_inst.addConnection(1, 2, mass=0.0001, angularFrequency=1000, loss=2, collisionExponent=1.6, rattleDistance=0.001, stringAPos=0.8, stringBPos=0.8)
```

As with the strings, we can also access these elements individually after creation:
```python
my_inst.connections[0].mass = 0.002   # set the mass of the first connection to 0.002 kg
my_inst.connections[2].loss = 3  # set the loss for the third connection to 3
```

The full parameter list (with defaults) for the connections is as follows:
- stringA (default: 1)
- stringB (default: 1)
- mass (default: 0.0001) 
- angularFrequency (1000)
- loss (2)
- collisionExponent (1.6)
- rattleDistance (0.001)
- stringAPos (0.8)
- stringBPos (0.7)

Once we have everything as we want it, we can create the final, formatted instrument file by calling the ```write()``` function, e.g.:
```python
my_inst.write("ness_files_to_process/net1_tutorial1_inst.m")
```

### Creating a Net1Score object
In the same document, we can also create our Ness score file. We create an instance of the ```Net1Score``` class as follows, passing in a total duration in seconds, and the string count:
```python
my_score = net1.Net1Score(T, stringCount)
```

We can then add events to this score with the ```addEvent()``` function.
```python
my_score.makeEvent(0.1, 1)  # strike string 1 at t=0.1 seconds
```
We can also specify an event in more detail, in terms of the strength, position, event type and the duration of the event as follows:
```python
# strike string 1 at t=0.5 seconds with more detailed info
my_score.makeEvent(0.5, 1, strength=0.5, pos=0.8, event_type=1, dur=0.002)  
```
The event type is either 0 (strike) or 1 (pluck). 

As with the instrument, we use the ```write()``` function to output our score as a NESS-compatible text file:
```python
my_score.write("ness_files_to_process/net1_tutorial1_score.m")
```

## Running your script
Once you have a score and instrument file assembled in your Python script, and have made sure that you have lines that will write the ```.m``` output files, use Terminal or Command Prompt to run your script. As before, navigate to the ness-tools-master folder and run the line:
```python
python net1_tutorial1.py
```
(or with a different file name if you called your script something different).

You should then find your new score and instrument ```.m``` files in the "ness_files_to_process" folder, or wherever you specified in your ```write()``` functions. Try using these files with the Ness online system to hear the audio.

## Full code from this example
An example of a fully formed python script from the above is provided below for reference:

```python
from nesstools import net1


# general variables
stringCount = 2         # how many strings should the guitar have?
T = 8                   # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 2 strings
my_inst = net1.Net1Instrument(stringCount)

# add a connection between string 1 and 2, using the default connection parameters
my_inst.addConnection(1, 2)

# write the instrument file as a NESS-compatible text file
my_inst.write("ness_files_to_process/net1_tutorial1_inst.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = net1.Net1Score(T, stringCount)    

# Add some events
my_score.makeEvent(0.1, 1)
my_score.makeEvent(0.2, 2)
my_score.makeEvent(0.3, 1)
my_score.makeEvent(0.4, 2)
my_score.makeEvent(0.5, 1)
my_score.makeEvent(0.6, 2)

# write the score file
my_score.write("ness_files_to_process/net1_tutorial1_score.m")
```

[<-- Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/net1-tutorial2/)
