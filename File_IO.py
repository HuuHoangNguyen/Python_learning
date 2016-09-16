#!/usr/bin/python

"""
This chapter covers all the basic I/O functions available in Python. For more functions, please refer to 
standard Python document.

Printing to the screen.
The simplest way to produce output is using the print statement where you can pass zero or more expressions
separated by commas. This functions coverts the expressions you pass into a string and writes the result to standard output

"""
import io

print "Python is really a great language,", " isn't it.?"

"""
Reading Keyboard inputPython provides two built-in functions to read a line of text from standard input. 
which by default comes from the keyboard. 
    - raw_input
    - input

The 'raw_input' Function:

    The raw_imput([prompt]) function reads one line from standarrd input and returns it as a string(removing the trailing newline).

"""
Str = raw_input("Enter yout input: ")
print "Received input is: ", Str

"""
THis prompts you to enter any string and it would display same strring on the screen.
When I  typed "Hello Python!", its output is like this.
"""

print """
The input[(prompt)] functions is equivalent to raw_input, expect that it assumes the input is a valid Python expression and returns the evaluated
result to you
"""
Str = input("Enter your input")
print "Received input is: ", Str

"""Opening and Closing Files
Until now, you have been reading and writing to the standard input and output.
Now, we will see how to use actual data files.

Python provides basic functions and methods necessary to manipulate files by default.
You can do most of the file manipulation using file object. 

"""
print "===================================================="
print """
    THE 'open' Functions

before you can read or write a file, you have to open it using Python's built-in
'open()' function. This function creates a file object, which would be utilized to
call other support methods associated with it.
Syntax:
    file object = open(file_name [, access_mod] [, buffering])
    
"""

