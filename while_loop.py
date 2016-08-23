#!/usr/bin/python

print "============================================================="
count = 0
while ( count < 9):
    print "The count is: ", count;
    count = count + 1

print "============================================================="
var = 1
while var == 1: # THis is construct an infinite loop
    num = raw_input("Enter a number : ")
    print "You entered: ", num
    var_num = int(num)
    if var_num == 0: var = 0

print "============================================================="


print "END"
