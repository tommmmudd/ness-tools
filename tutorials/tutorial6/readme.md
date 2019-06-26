# NESS Guitar Score Tutorial 6
This tutorial looks at plucking harmonics in a little more depth.

Audio example of this code: [score_tut_6.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_6.mp3)

The code for this tutorial can be found in the [gtr_score_6_harmonics_advanced.py](https://github.com/tommmmudd/ness-tools/gtr_score_6_harmonics_advanced.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (7)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial5)  / / /  [Next Tutorial (7) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial7)

## The fifth harmonic - a problem
In the last tutorial, you may have tried for yourself playing the fifth harmonic (position of `1/5.0`), e.g. as follows:
```python
my_score.playHarmonic(1, 0.5, 	1/5.0) # 5th harmonic on string 1
```

If you haven't already, then do so. You should find that the harmonic doesn't sound clean at all - the pluck is percussive and the harmonic doesn't ring. This isn't actually a problem with the model or with your Python code. You would get the same result with an actual guitar. The problem resides in the relation between the harmonic position and the position of the pluck. The default pluck position for the `playHarmonic()` function is `0.8` (or `4/5.0`). This coincides exactly with a node in the harmonic standing wave as shown in the image below.

![5th harmonic](http://tommudd.co.uk/ness/images/5th_harm.svg.png)

This means that we are plucking at precisely the point at which we need a node in the standing wave. This makes it difficult for the string to resonate at this frequency.

## Changing the pluck position
You can change the position of the pluck with the `pluckPos` parameter as shown below:

```python
my_score.playHarmonic(1, 3, 	1/5.0, pluckPos=0.7)
```

Here, the pluck is shifted to 0.7, which is safely between the two nodes at 0.6 (3/5) and 0.8 (4/5). Notice that we explicitly call the parameter name in the function, as we are specifying the arguments out of sequence (more below).

Here are some more examples

```python
my_score.playHarmonic(2, 3.1, 	1/5.0, pluckPos=0.7)
my_score.playHarmonic(3, 3.2, 	1/5.0, pluckPos=0.7)
my_score.playHarmonic(1, 3.5, 	1/6.0, pluckPos=0.754)
my_score.playHarmonic(2, 3.6, 	1/6.0, pluckPos=0.754)
my_score.playHarmonic(3, 3.7, 	1/6.0, pluckPos=0.754)
```

## Other parameters to playHarmonic()
In full, playHarmonic can take 7 parameters:

|description | param name | default |
| --- | --- | --- |
|string number | s | 1 |
|time | t | 0 |
| glide time | glideTime | 0.01 |
| downwards finger force | fingerF | 0.017 |
| pluck position | pluckPos | 0.8 |
| pluck force | pluckF | 0.3 |

You can either specify these in order, like this:
```python
my_score.playHarmonic(3, 3.7, 1/6.0, 0.01, 0.015, 0.754, 0.4)
```

Or you can name the parameters you want to set, as we have done above with pluckPos. Note that the finger downward force is very sensitive for the harmonic! If you press harder, you will get the fretted sound of the string. If you press more gently, you will get the sound of the open string.

Audio example of this code: [score_tut_6.mp3](http://tommudd.co.uk/ness/audio/gtr_tutorials/score_tut_6.mp3)

The code for this tutorial can be found in the [gtr_score_6_harmonics_advanced.py](https://github.com/tommmmudd/ness-tools/gtr_score_6_harmonics_advanced.py) file. For help on running the code see the [main repository page](https://tommmmudd.github.io/ness-tools/).

[<-- Previous Tutorial (7)](https://tommmmudd.github.io/ness-tools/tutorials/tutorial5)  / / /  [Next Tutorial (7) -->](https://tommmmudd.github.io/ness-tools/tutorials/tutorial7)




