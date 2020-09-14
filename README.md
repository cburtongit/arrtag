# arrtag
Python Script for extracting ID3 tags from a filename (use with youtube-dl! for best results)!

## Requirements:
- Python (3.8+)
- all files must be mp3 as of right now, have plans to include more
- no non-mp3 files in the target directory

Tested on macOS 10.14 Mojave.

## Instructions:
Download the script you need and run the following:
<code> python3 arrtag.py [path to your music library] </code>

example:
<code> python3 arrtag.py /Users/user1/Music </code>

There are some potential problems:
- having a non music file like "iTunes.library" or "random_picture.png" will cause errors, remove them from the directory before using
- Music files with no '-' characters will cause an error too, you will just have to manually rename those or remove them from the directory before running the script
- using the arrtag.py file on files NOT containing a <code>"[Artist] - [Title]-[random 11 digit string].mp3</code> format will result in some of the [Title] tag being cut off. See formatting below:

For youtube-dl users use arrtag.py:
File format:
<code> [Artist] - [Title]-[video id].mp3 </code>
Example: <code> Black Sabbath - Children of the Grave-xuiOF90djJk.mp3 </code>

For non-youtube-dl users you should use noarrtag.py:
File format:
<code> [Artist] - [Title].mp3 </code>


If you have any suggestions please let me know, I am still learning python as a side hobby alongside C and Java so code cleanups are welcome!
