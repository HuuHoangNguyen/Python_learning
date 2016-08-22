#!/usr/bin/python

# The list  are enclosed in brackets ([]) and their element
# and size can be changed, while tuples are enclosed in parenthese
# ( () ) and cannot be updated. The Tuples can be thought of as
# read-only of list
list = ['abc', 786, 2.23, 'John', 70.2 ]
tinylist = [ 123, "Vien"]

print list                  # Print complete list
print list[0]               # Print first element of the list
print list[1:3]             # Print elements starting from 2nd till 3rd
print list[2:]              # Print elements starting from 3rd element

print tinylist * 2          # Print list two times
print list + tinylist       # Print concatenated lists
