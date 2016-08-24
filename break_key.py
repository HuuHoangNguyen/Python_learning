#!/usr/bin/python

for letter in "Python":             #First example
    if letter == 'h':
        break
    print "Current variable value : ", letter

var = 10
while var > 10:
    print "Current variable value : ", var
    var = var - 1
    if var == 5:
        break
print "END"
