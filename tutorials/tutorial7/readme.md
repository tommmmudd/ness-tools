# NESS Guitar Score Tutorial 7
This tutorial looks at creating a score from guitar tab.

Audio example of this code: [score_tut_7.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_7.mp3)

The code for this tutorial can be found in the [gtr_score_7_tab1.py](https://github.com/tommmmudd/ness-tools/gtr_score_7_tab1.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (6)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial6)  / / /  [Next Tutorial (8) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial8)

# Guitar Tab
A common way to notate music for guitar players is tablature. This specifies fret numbers on specific strings as shown below.

```
An example of conventional 6-string guitar tablature:
|-----------0------5---------|  <-- thinnest string
|---------0--------5---------|
|-------1----------6---------|
|-----2------------7---------|
|---2--------------7---------|
|-0----------------5---------|   <-- thickest string
```

You can find lots of examples of guitar tabs as plain txt files on sites such as [classtab.org](http://www.classtab.org). We can translate this kind of notation into Ness score files. In doing so however, we make the simplifying assumption that each horizontal step is a fixed unit of time.

# Converting tabs to score files
Let's set up a score object to put our tab into:
```python
from nesstools import guitar

numberOfStrings = 6         # how many strings should the guitar have?
my_score = guitar.GuitarScore(0, numberOfStrings) 
```

Unlike the previous examples, we don't yet know what the duration of our score will be. We have put a `0` in as a placeholder. The score will then take the duration from the length of the tab input.

We specify each line of the tab as a separate string (in a coding sense), in the same format as you see above:
```python
s6 = "|-0------0--2--3-3-----|"     # <-- thinnest string
s5 = "|-0-----0-------3------|"
s4 = "|-0----0---------4-----|"
s3 = "|-2---2-----------5----|"
s2 = "|-2--2-----------5-----|"
s1 = "|-0-0----------3---3---|"     # <-- thickest string
# collate the strings into a list
tab = [s1, s2, s3, s4, s5, s6]
```

Note that unlike conventional guitar terminology, we refer to the lowest string as string 1. The individual strings are then assembled into a list as the variable `tab`. Once we have this list of strings, we can pass it to the `tabToScore()` function. 

```python
my_score.tabToScore(tab, numberOfStrings, 1.0)    
```

Note that the function needs to be told how many strings there are, and can be optionally given a `rate` parameter. Here the rate is 1. A rate of 2 would play the tab in half the time. This scales the amounut of time for each step `-` in the tab (1/8 of a second by default).

This is all we need to do to create our score file! So now we just write it, and you can try processing it with any 6-string instrument file (preferably one that is in tune!).
```python
my_score.write("ness_files_to_process/gtr_score_7_tab1.m")
```

In the next tutorial we will look at importing an entire tab from a txt file.

Audio example of this code: [score_tut_7.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_7.mp3)

The code for this tutorial can be found in the [gtr_score_7_tab1.py](https://github.com/tommmmudd/ness-tools/gtr_score_7_tab1.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (6)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial6)  / / /  [Next Tutorial (8) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial8)



