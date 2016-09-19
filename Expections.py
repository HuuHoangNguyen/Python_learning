#!/usr/bin/python

"""
The assert Statement
When it encounter an assert statement, Python evaluates  the accompanying expression, 
Which is hopefully true. If the expression is false, Pyhon raises an AssertionError exception.

assert Expression[, Arguments]

If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. 
AsseerError exceptions can be caught and handled like any other exception using the try-except statement,
but if not handled, they will teminate the program adnf produce a traceback.

"""

def Kelvin2Fahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return (((Temperature - 273) * 1.8 ) + 32)

print Kelvin2Fahrenheit(273)
print int(Kelvin2Fahrenheit(505.78))
print Kelvin2Fahrenheit(-5)

