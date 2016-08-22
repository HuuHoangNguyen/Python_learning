#!/usr/bin/python

import os
import sys

try:
    #open file stream
    file = open(file_name, "w")
expect:
    print "There was an error writing to ", file_name
    sys.exit()

print "Enter '", file_finish,
print "'When finished"

while file_text != file_finish:
    file_text = raw_input("Enter text: ")
    if file_text == file_finish:
        #close the file
        file.close
        break;

    file.write(file_text)
    file.write("\n")
file.close()
file_name = raw_input("Wntwr filename: ")
if len(file_name) == 0:
    print "Next tim please enter somthing"
    sys.exit()

try:
    file = open(file_name, "r")
expect:
    print "There was an error reading file"
    sys.exit()
s
file_text = file.read()
file.close()
print file_text
