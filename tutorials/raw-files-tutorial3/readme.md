# Raw score and instrument files 3
This tutorial expands our instrument by adding connections between strings

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial1/) / / / [Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial3/)

## String connections
We can add a connection between a point on any string to a point on any other string (or even to the same string). We need to define several parameters to do this:

- mass (kg), >0. Do not set to 0!
- angular frequency (rad), >0. try to keep below about 1e4
- loss parameter (bigger means more loss). >=0
- collision exponent (>1, usually <3). Probably best not to use 1 exactly
- rattling distance (m), >=0. Can be zero!
- string index 1 
- connection point 1 (0-1)
- string index 2: if zero, then no connection
- connection point 2 (0-1)

These elements are included in your instrument files as shown below. The parameters 
```matlab
ssconnect_def = [0.001, 10000, 2, 1.6, 0.001, 1, 0.8, 2, 0.7];
```

Try adding this line to a two string instrument (e.g. the instrument from the last tutorial). Then try running the file with different kinds of scores. Note that you will now get sound on outputs on either string, even if you only excite one of them.

Experiment with different settings for the different parameters.

Note that you can also connect strings to themselves (specify the same string number for both string indexes) and you can also add a connection attached at only one end - specify a zero for the other string index.

## Multiple connections
As with the ```string_def```, the ```ssconnect_def``` can have multiple connections defined. The syntax is similar: separate each set of parameters with a semicolon. The following example has three connections for example:

```matlab
% connect string 1 to string 2
% connect string 2 to string 2
% add a loose connection to string 1
ssconnect_def = [0.0001, 10000, 2, 1.6, 0.0001, 1, 0.8, 2, 0.7;   0.0001, 10000, 2, 1.6, 0.0001, 2, 0.1, 2, 0.95;   0.0001, 10000, 2, 1.6, 0.0001, 1, 0.8, 0, 0.7];
```



