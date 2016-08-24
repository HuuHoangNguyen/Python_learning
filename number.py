#!/usr/bin/python

var1 = 1
var2 = 10

print "Value of var1 is : ", var1
print "Value of var2 is : ", var2
del var1
#print "Value of var1 is : ", var1
print "Value of var2 is : ", var2

var_a = 100
var_b = 1000L
var_c = 1.125
var_d = 10 + 3j

print "==============================================================="
print "Value of var_a is ", var_a
print "Value of var_b is ", var_b
print "Value of var_c is ", var_c
print "Value of var d id ", var_d

print "==============================================================="
print "Converted var_c to integer is ", int(var_c)
print "Converted var_c to long is ", long(var_c)
print "Converted var_a to float is ", float(var_a)
print "Converted var_a to complex is ", complex(var_a, var_b)

print "==============================================================="
