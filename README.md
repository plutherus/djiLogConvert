DJI Video Log Converter
=======================

Converts information from DJI video subtitle files (.SRT) into csv suitable for use in arcGIS or whatever you want a csv for.

Note that this does *not* read the flight log, just the files associated with every video - so any part of the flight
that doesn't include video won't be shown in the csv file.

There is a library (srtConvert) and a script that calls it (djiConvert).

# Using the library directly from another python script

To use the library from your own Python script (for example, if you're using this within arcpy in arcgis), just 
get the file srtConvert.py and put it in your working directory.  Add the line:
```
import srtConvert
```
to your script.  Call it with:
```
srtConvert.convertSRT(inFile,outFile,debug)
```
- ***inFile*** is the .SRT file that DJI generates with every video.
- ***outFile*** is the name of the csv output file that it will generate
- ***debug*** should usually be False unless you want to run it in debug mode, in which case it should be True.

For example:
```
srtConvert.convertSRT(DJI_0123.SRT,DJI_0123.csv,False)
```
It doesn't return anything, just writes the output file.

# Using the script to convert files from the command line

If you want to just run the script from the command line, then get both srtConvert.py and djiConvert.py. 
In djiConvert.py, it will fill in outFile and debug for you if you don't specify them, so you could just run:
```
python djiConvert --inputFile=DJI_0123.SRT
```
and it will automatically create a file called DJI_0123.csv in the same directory.
If you want, you can add the --outputFile and/or --debug options as well. For example:
```
python djiConvert -inputFile=~/video/phantom/DJI_0123.SRT --outputFile=~/arcgis/phantom-flight-123.csv --debug
```