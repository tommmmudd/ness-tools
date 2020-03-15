# Troubleshooting
It is not uncommon to get the following message when uploading your score and instrument files:

**"There has been an error during the simulation"**

There may be a range of reasons for this. Below is a quick checklist of potential issues.

## General Issues
- Semicolons! All lines should be terminated by one (prior to any inline comments)
- Arrays do not include commas, e.g. ```string_def = [0.68 1 12.1 0.0002 15 5];```. Functions do include commas, e.g. ```event_gen(exc, 1, 0.5, 0.8, 0.001, 2, 1);```

## Score Issues
- Make sure you are not trying to excite a string that doesn't exist: check the score and instrument files to make sure you are never trying to pluck string 4 on a 3-string instrument.
- Make sure you are not trying to output at a time that is greater than your ```Tf``` variable.

## Instrument Issues
- Remember to include ```itnum = 20```
- Make sure you have the same number of pan positions as you have output positions
- Make sure you are not outputting on a string that doesn't exist in the ```string_def```
- Make sure you have exactly six parameters for each element of the ```string_def```
- Make sure there are semicolons between each set of six parameters for the ```string_def```
