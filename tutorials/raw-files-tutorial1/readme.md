# Raw score and instrument files 1
This tutorial looks at creating score and instrument files by directly editing the .m files.

Here we will create text files that describe a virtual instrument (instrument files) and that tell that instrument what to do (score files)

## To run these files
- You will need to register for an account:
- 1) Register for an EASE Friend account with the University of Edinburgh: https://www.ease.ed.ac.uk/friend/
- 2) Then email the NESS team synthesis@epcc.ed.ac.uk, including your EASE username (usually your email address) in the email.  You will then be added to the user access list for the NESS web UI.
- Upload your score and instrument .m files to the [NESS User Interface](https://ness-frontend.eca.ed.ac.uk/) to create audio files

## To edit these files
You will need a simple text editor. Notepad or TextEdit will do, but something with syntax highlighting might be useful, e.g. [Sublime Text](https://www.sublimetext.com/) or [Atom](https://atom.io/)

## Creating a simple string instrument file
Create a new document with your text editor and save the empty file as *inst_single_string.m*.

There are a few fundamental things that will need to be in an instrument file for the net1 code.
The file should start with this line:

```matlab
%gtversion 1.0
```

On a new line, a sample rate is also necessary, e.g. 44100, 48000, 96000, etc.
```matlab
SR=48000;       % Sample rate
```

Note that text to the right of the % sign is treated as a comment in the code, and doesn't actually do anything, it is just a note to help you with the code (with the exception of the %gtversion message).

We will define a single string here. This requires a list of **six** parameters that represent:
- the string length in metres
- the material type where 1: steel, 2: gold, 3: lead
- the tension in Newtons
- the radius in metres
- the decay time (T60) for low frequencies (at DC)
- the decay time (T60) for higher frequencies (at 1kHz)

Our string definition might therefore look like this:
```matlab
string_def = [0.68 1 12.1 0.0002 15 5];
```
This creates a steel string that is 68cm long, 0.02cm in radius, tightened to 12.1 newtons, with a decay time of 15 seconds for low frequencies and 5 seconds for higher frequences.

As a minimum requirement for a working instrument file, we also require the following:
- An output_def: at least one output position on the string to take a reading from (this acts a little bit like a pickup)
- A pan position (between ±1) for each of the outputs (a stereo file will automatically be created that mixes the outputs together)
- the line *itnum = 20;*


The syntax for these lines looks like this:
```matlab
output_def = [1 0.8];  % string one outputs 80% of the way along the string 
pan = [0]              % 0 is the centre
itnum = 20;            % don't change this!
```

Finally, a useful but not essential addition is this line:
```matlab
normalize_outs = 0;    % individually normalise output channels
```
This makes sure all the string output wavs are normalised.

Your final instrument file should now look something like this:
```matlab
%gtversion 1.0
SR=48000;     % sample rate

string_def = [0.68 1 12.1 0.0002 15 5];

output_def = [1 0.8];  % string one outputs 80% of the way along the string 
pan = [0]              % 0 is the centre
itnum = 20;            % don't change this!

normalize_outs = 0;    % individually normalise output channels
```

Save your file. We will now make a quick score file that we can use to test this instrument.

## Creating a simple score file
Create another new file with your text editor, and save the empty file as *score_single_string.m*. The score file also has a few necessary elements. Firstly, we are required to provide the total duration of the score file. This simulation will cut off abruptly after this amount of time, so make sure you leave room for the sound to decay to zero! In some of our examples we will be a little lazy with this just to test things slightly more quickly.

The time is specified as Tf:
```matlab
Tf = 10;   % duration in seconds
```

Secondly, we need to create a specific variable called *exc* that we will use to store our plucking and striking excitation events. This is done with the following line:
```matlab
exc = [];   % array for excitation events
```

We can now add excitation events. Here we will use the ```event_gen``` function. This takes seven arguments:
- the excitation array, exc
- the **string number** (e.g. 1 in our case)
- the **time** at which to excite (in seconds - must be less that then Tf duration!)
- the **position** on the string to excite (0-1)
- the **duration** of the excitation (usually very small, e.g. 0.001)
- the **force** of the excitation in Newtons
- the **type** of event, where 0 is a strike and 1 is a pluck

The syntax for an event looks like this:
```matlab
% excitation event, where string=1, time=0.01, pos=0.8, duration=0.001, force=2, type=0 (strike)
exc = event_gen(exc, 1, 0.01, 0.8, 0.001, 2, 1);
```



## Testing the Instrument and Score files
Now that we have an excitation event, we can try running this though the NESS system to generate audio. Go to [NESS User Interface](https://ness-frontend.eca.ed.ac.uk/) and use the *Browse...* buttons to upload your score and instrument files. Press the *Submit Job* button to send the files. After a short time you should see an audio file player appear that will play back a stereo mix of your file as shown below.

![NESS audio playback](http://tommudd.co.uk/ness/images/ness_interface_playback.png)

If your file is quite long, the system will not give you the player and will give you a message with a rough estimate of how long the processing will take as shown here:

![NESS long processing message](http://tommudd.co.uk/ness/images/ness_slow_processing.png)

In this case you will need to use the link to the folder where the files will appear when they are ready. This is the *Click for result directory (opens in new tab)* link in the image above. The folder will initially just contain your score and instrument files:

![NESS waiting for results](http://tommudd.co.uk/ness/images/ness_waiting_for_results.png)

Refresh the page to check whether the processing has been completed. When the files have been created, you will see audio files in the directory as shown below.

![NESS results](http://tommudd.co.uk/ness/images/ness_results.png)

The *output-mix.wav* file is the stereo mix of any number of outputs. If you have more than one string, you will also see files named *output-string1-1.wav*, *output-string2-2.wav* etc. These correspond to the ```output_def``` specified in your instrument.

You can download the files to listen to and work with the stereo mix or the individual string files.
