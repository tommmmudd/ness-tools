# NESS Guitar Score Tutorial 8
This tutorial looks at creating a score from guitar tab.

Audio example of this code (custom tab): [score_tut_8.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_8.mp3). 

The code for this tutorial can be found in the [gtr_score_8_midi.py](https://github.com/tommmmudd/ness-tools/gtr_score_8_midi.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (7)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial7)  / / /  [Next Tutorial (9) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial9)


# Converting MIDI files for Ness scores
Just as we downloaded txt tab files for creating scores, we can do the same for Midi files. Although midi files on the web feels like more of a 1990s phenomenon, there are still lots of places to find midi files (e.g. [freemidi.org](https://freemidi.org). 

Just as with tab, there are some simplifying assumptions in translating Midi data to a score file. Firstly, Midi note offs are ignored in this translation - a note is left ringing until another note on that same string is played. The converter also makes it's own decisions about which string to play a given note on, as this is not explicit from the pitch information alone. Finally, this converter doesn't distinguish between Midi channels, so if you give it a full band/orchestra Midi it will try and pay all the parts on a single guitar! The [example audio](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_8.mp3).  in this tutorial tries to render Cher's *Believe* as a single guitar score. The results are strange but interesting!

The process is largely the same as in the last tutorial. First, setup the score object:

```python
from nesstools import guitar

numberOfStrings = 6
my_score = guitar.GuitarScore(0, numberOfStrings)     
```

Then create a variable with the name of your Midi file (if you've saved it into the same directory as the script, otherwise specify a full path here).
```python
midiFile = "yourmidifile.mid"
```

As before we can specify the rate of playback - how fast the Midi file is to be played through. We can also specify a transposition in semitones, if desired.

```
# specify the playback rate for this midi file
rate = 0.6

# you can use this variable to transpose the whole score by N semitones
# e.g. a 5 would shift everything up 5 semitones
transpose = 0
```

Then we can the conversion funciton and export the score

```python
my_score.midiToScore(midiFile, numberOfStrings, rate, transpose)
my_score.write("ness_files_to_process/gtr_score_8_midi.m")
```

Try this out with different kinds of Midi files. The rendering is rarely perfect or accurate, but often interesting.

Audio example of this code (custom tab): [score_tut_8.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_8.mp3). 

The code for this tutorial can be found in the [gtr_score_8_midi.py](https://github.com/tommmmudd/ness-tools/gtr_score_8_midi.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (7)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial7)  / / /  [Next Tutorial (9) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial9)
