#!/usr/bin/python

a = 21
b = 10
c = 0

c = a + b
print "Line 1: Value of c = a + b is: ", c

c += a
print "Line 2: Value of c += a is: ",c

c *= a
print "Line 3: Value of c *= a is: ",c

c /= a
print "Line 4: Value of c /= a is: ", c

c = 2
c %= a
print "Line 5: Value of c %= a is: ", c

c **= a
print "Line 6: Value of c **= a is: ", c

c //=b
print "Line 7: Value of c //= b is: ", c
