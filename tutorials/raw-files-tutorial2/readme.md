# Raw score and instrument files 2
This tutorial expands our instrument by adding more strings

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial1/) / / / [Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial3/)

## Additional Strings
We can add additional strings to the instrument by expanding the ```string_def``` line. In the last tutorial, we defined a single string like this:
```matlab
string_def = [0.68 1 12.1 0.0002 15 5];   % example from tutorial 1
```

To add a second string, we stay within the square brackets, but add a semicolon and provide a new list of six parameters:
```matlab
% Two strings
string_def = [0.68 1 12.1 0.0002 15 5; 0.68 1 12.3 0.00015 15 5];   
```

The second string here is slightly thinner (radius = 0.00015 metres), and the tension is slightly higher (12.3 Newtons). These two strings correlate roughly to conventional low E and A guitar strings.

If we want to actually hear anything from our second string we will need to add an output (and a corresponding pan position). We expand our output line and panning lines like so:
```matlab
output_def = [1 0.8; 2 0.8];  % an output for each string
pan = [-0.5 0.5];              % slight panning
```

Note that each output definition requires a string number followed by an output position (0-1). This remember is the point on the string at which to output. Each output is separated by a semicolon, as with the ```string_def'''. Note that the panning positions (-1 to +1) are **not** separated by semicolons.

Our final instrument file therefore looks like this:
```matlab
%gtversion 1.0
SR=48000;     % sample rate

% two strings
string_def = [0.68 1 12.1 0.0002 15 5; 0.68 1 12.3 0.00015 15 5];  

output_def = [1 0.8; 2 0.8];  % an output for each string
pan = [-0.5 0.5];              % slight panning
itnum = 20;            % don't change this!

normalize_outs = 0;    % individually normalise output channels
```
## Plucking multiple strings

We will now hear the output of our second string, but we still won't hear any actual sound, because there are no events on that string. We can add another pluck exactly as we did in the previous tutorial, changing the time and string number so the the events are distinct, e.g.

```matlab
Tf = 10;                        % duration (s)
exc = [];                       % initialise excitation array

% excitation events, where pos=0.8, duration=0.001, force=2, type=0 (strike)
exc = event_gen(exc, 1, 0.5, 0.8, 0.001, 2, 1);   % pluck s1 at t=0.5
exc = event_gen(exc, 2, 1.0, 0.8, 0.001, 2, 1);   % pluck s2 at t=1.0
```

Try adding more strings (and outputs/pan positions) and more events to trigger those strings. The following gives an approximate definition for a six string guitar:
```matlab
string_def = [0.68 1 12.1 0.0002 15 5; 0.68 1 12.3 0.00015 15 5; 0.68 1 21.9 0.00015 15 5; 0.68 1 39.2 0.00015 15 7; 0.68 1 27.6 0.0001 15 5; 0.68 1 49.2 0.0001 15 8];
```

[<-- Previous Tutorial](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial1/) / / / [Back to index](https://tommmmudd.github.io/ness-tools/) / / / [Next Tutorial -->](https://tommmmudd.github.io/ness-tools/tutorials/raw-files-tutorial3/)

