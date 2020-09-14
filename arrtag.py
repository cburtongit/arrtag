# author: C. J. Burton @14.09.2020
# Licence: MIT + Give credit in source files
import os
import sys
import eyed3

directory = sys.argv[1]

# Start Message: Arrtag Verision 1.0
print("\n\n----------------------------------------------------------------------")
print("arrTag - The internet sailor's way to sort out his music metadata!\n --> Version 1.0.4")
print("----------------------------------------------------------------------")
print("\nTarget: " + directory + "\n\nProcessing:")

for filename in os.listdir(directory):
    song = eyed3.load(directory + "/" + filename)
    print("Adding ID3 Tags to: " + filename)
    splitname = filename.split('-')
    song.tag.artist = splitname[0][:-1]
    song.tag.title = splitname[1][1:]
    print("    Saving tags as ARTIST: " + splitname[0][:-1] + " , TITLE: " + splitname[1][1:])
    song.tag.save()
    print("    Tags Saved for : " + filename + "\n")
