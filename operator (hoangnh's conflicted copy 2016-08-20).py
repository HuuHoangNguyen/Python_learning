#!/usr/bin/python

#Types of Operator
#Python language supports the following types of Operator

#   Arithmetic Operators
#   Comparison (Relational) Operators
#   Assignment Operators
#   Logical Operators
#   Bitwise Operators
#   Membership Operators
#   Identity Operators

a, b = 10, 20
print "a + b = ", a+b                   # Addition
print "a - b = ", a-b                   # Subtraction
print "a * b = ", a*b                   # Multiplication
print "a / b = ", a/b                   # Devision
print "a '%' b = ", a%b                 # Modulus
print "a ** b = ", a**b                 # Exponent
print "a '//' b = ", a//b                  # Floor Devision
# Floor devison- The divison of operands where the result is the
# quoctient in which the digits after the decimal point are removed.
# But if one of the operands is nagative, the result is floored, i.e.,
# rounded away from zero (towards negative infinity)
# 9 // 2 and 9.0 // 2.0 = 4.0
# -11 // 3 = -4
# -11.0 //3 = -4.0

#-----------------------------------------------
if a == b:
    print " a is equal b"
else:
    print "a i NOT equal b"

#-----------------------------------------------
if a != b:
    print "a is different b"
else:
    print "a and b are similar values"

#There operators compare the values on either sides of them and decide the e
#relation among them. They are also called Relational operators.
#Assume variable a holds 10 and variable b holds 20, then
# Operator              Description                                                     Example
#   ==                  If the values of two operands are equal, then the
