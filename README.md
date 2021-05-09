This Python script will ask the user for a source directory which it will recursively traverse in order to move all found picture or video files to the directory specified in the Settings class. 

I found that Google Takeout provided a lot of non-photo files (mainly .json) as well as a bunch of duplicated photos. This script eliminates those by only moving photo and video files to the output directory, and skips any duplicates (after confirming they contain the same data). 

If any files are found that duplicate a name, but don't contain identical data, the script exits for manual intervention. This could be fixed by changing the destination name to something like filename(1), but I never encountered this case.
