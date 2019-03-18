# NESS Python library

Python classes for building score and instrument files for the [NESS physical models](http://ness.music.ed.ac.uk).

Example implementation

```python
from nesstools import guitar

my_guitar = guitar.StringInstrument(2)
my_guitar.defaultGuitar()
my_guitar.write("basic_guitar.m")

my_score = guitar.GuitarScore(60, 2)       
pluckTime = 1
pluckString = 1
my_score.plucks.append( [pluckString, pluckTime, 0.8, 0.0001, 1] )
my_score.write("basic_score.m")
```

Currently includes classes for the brass, guitar and soundboard models
