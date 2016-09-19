#!/usr/bin/python

for letter in "Python":         #First example
    if letter == 'h':
        pass
    else:
        print "Current Letter value: ", letter


var = 10                # Second example
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print "Current variable value: ", var

print "END"
