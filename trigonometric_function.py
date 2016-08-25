#!/usr/bin/python

# acos(x): Return the arc cosine of x, in radians
# asin(x): Return the arc sine of x, in radians
# atan(x): Return the arc tangent of x, in radians
# atan2(y,x): Return atan(y/x), in radians
# cos(x): Return the cosine of x radians
# hypot(x): Return the Euclidean norm, sqrt(x*x + y*y)
# sin(x): Return the sine of x radians
# tan(x): Return the tangent of x radians
# degrees(x): Converts ang;e x from radians to fegrees.
# radians(x): Converts angle x from degrees to radians
import math

print "cost(x)"
print "acos(0.64) : ", math.acos(0.64)
print "acos(0)    : ", math.acos(0)
print "acos(-1)   : ", math.acos(-1)
print "acos(1)    : ", math.acos(1)

print "\nasin(x)"
print "asin(0.64) : ", math.asin(0.64)
print "asin(0)    : ", math.asin(0)
print "asin(-1)   : ", math.asin(-1)
print "asin(1)    : ", math.asin(1)

print "\natan(x)"
print "atan(0.64) : ", math.atan(0.64)
print "atan(0)    : ", math.atan(0)
print "atan(-1)   : ", math.atan(-1)
print "atan(1)    : ", math.atan(1)

print "\natan2(y, x)"
print "atan2(-0.50, -0.50 ) : ", math.atan2(-0.50, -0.50)
print "atan2(0.50, 0.50)    : ", math.atan2(0.50, 0.50)
print "atan2(5, 5)          : ", math.atan2(5, 5)
print "atan2(-10, 10)       : ", math.atan2(-10, 10)
print "atan2(10, 20)        : ", math.atan2(10, 20)

print "\ncos(x)"
print "cos(3)         : ", math.cos(3)
print "cos(-3)        : ", math.cos(-3)
print "cos(0)         : ", math.cos(0)
print "cos(math.pi)   : ", math.cos(math.pi)
print "cos(2*math.pi) : ", math.cos(math.pi*2)

print "\nhypot(x)"
print "hypot(3, 2)  : ", math.hypot(3, 2)
print "hypot(-3, 3) : ", math.hypot(-3, 3)
print "hypot(0, 2)  : ", math.hypot(0, 2)

print "\nsin(x)"
print "sin(3)         : ", math.sin(3)
print "sin(-3)        : ", math.sin(-3)
print "sin(0)         : ", math.sin(0)
print "sin(math.pi)   : ", math.sin(math.pi)
print "sin(math.pi/2) : ", math.sin(math.pi/2)

print "\ntan(x)"
print "tan(3)         : ", math.tan(3)
print "tan(-3)        : ", math.tan(-3)
print "tan(0)         : ", math.tan(0)
print "tan(math.pi)   : ", math.tan(math.pi)
print "tan(math.pi/2) : ", math.tan(math.pi/2)
print "tan(math.pi/4) : ", math.tan(math.pi/4)

print "\ndegrees(x)"
print "degrees(3)         : ", math.degrees(3)
print "degrees(-3)        : ", math.degrees(-3)
print "degrees(0)         : ", math.degrees(0)
print "degrees(math.pi)   : ", math.degrees(math.pi)
print "degrees(math.pi/2) : ", math.degrees(math.pi/2)
print "degrees(math.pi/4) : ", math.degrees(math.pi/4)

print "\nradians(x)"
print "radians(3)         : ", math.radians(3)
print "radians(-3)        : ", math.radians(-3)
print "radians(0)         : ", math.radians(0)
print "radians(45)        : ", math.radians(45)
print "radians(90)        : ", math.radians(90)
print "radians(180)       : ", math.radians(180)

print "\n"
print "math.pi = ", math.pi
print "math.e  = ", math.e
