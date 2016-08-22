#!/usr/bin/python

a = 60          # 60 = 2b00111100
b = 13          # 13 = 2b00001101
c = 0           #  0 = 2b00000000

c = a & b       # 12 = 2b00001100
print "Line 1: Value of c = a & b is: ", c

c = a | b       # 61 = 2b00111101
print "Line 2: Value of c = a | b is: ", c

c = a ^ b       # 49 = 2b00110001
print "Line 3: Value of c = a ^ b is: ", c

c = ~a;         #-62 = 11000011
print "Line 4: Value of c = !a is: ", c

c = a << 2      #240 = 2b11110000
print "Line 5: Value of c = a << 2 is: ", c

c = a >> 2      # 15 = 2b00001111
print "Line 6: Value of c = a >> 2 is: ", c
