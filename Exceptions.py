#!/usr/bin/python


"""
Exception
Syntax:
    try:
        #You do your oprations here.
    except ExceptionI:
        #If the is ExceptionI, then execute this block
    except ExceptionII:
        #If the is ExceptionI, then execute this block
    ......................
    else:
        If there is no exception then execute this block. 
""" 
print "============================================================="
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: Can\'t find file or read data"
else:
    print "Written content is file successful"   
    fh.close()


print "============================================================="
try:
    fh = open ("text_file", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: Can\'t find file or read data."
else:
    print "Written content in the file successfully"

"""
==============================================================================
The expect Clause with no Exceptions
try: 
    You do your operations here;
except:
    If there any execption, then execute this block
    ..........
else:
    If there is no exception then execute this block

"""

"""
==============================================================================
The except Clause with Multiple Exceptions
try:
    You do your operations here
except(Exception1[, Exception2[,...ExceptionN]]):
    If there is any exception from the figen exception list then execute this block.
    .......... 
else:
    If there is no exception then execute this block
"""

"""
==============================================================================
The try-finally Clause
You can use a finally: block along with a try:block. The finally block is a place to put
any code that must execute, whether the try-block raised an exception or not. The syntax of the try-finally statement
try:
    You do your operations here
    ................... 
    Due to any exception, this may be skipped.
finally:
    This would always be executed.
"""
print "============================================================="
try:
    fh = open("TestFile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print "Error: Can\'t find file or read data"

#
print "============================================================="
try: 
    fh = open("Test_File", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print "Going to close the file"
        fh.close()
except IOError:
    print "Error: Can\'t find file or data"



"""
==============================================================================
    Argument of an Exception
An exception can have an argument, which is a value that gives additional infomatio about the problem.
The contents of the argument vary by exeption. You capture an exception's argument by supplying a variable
in the except clause as follows.

try:
    You do your operations here
    .....
expect ExpectionType, Argument:
    You can print value of Argument here...

"""
print "============================================================="
#Define a function here
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The argument does not contain numbers\n", Argument

#Call above function here.
temp_convert("xyz")


"""
==============================================================================
    Raising an Exceptions
You can raise exception in several ways by using the raise statement. 
The general synrax for the raise statement is as follows
    Syntax 
raise [Exception[, args [, traceback]]]
"""

print "============================================================="
def funcRaiseAnException(level):
    if level < 1:
        raise "Invalid level!", level
        # The code below to this would not be executed
        #If we raise the Exception


try:
    # funcRaiseAnException(-1)
    funcRaiseAnException(1)
except "Invalide level":
    print "The level cannot nagative"
else:
    print "End of here"



"""
==============================================================================
    User-Defined Exceptions

Python also allows you to create your own exceptions by deriving classes from the
standard built-in exceptions.

Here is an example ralates to RuntimeError. Here, a class is created that is subclassed 
from RuntimeError. This is useful when you need to display more specific infomation
when an exception is caught.
"""

print "============================================================="
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try: 
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
