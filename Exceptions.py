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
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: Can\'t find file or read data"
else:
    print "Written content is file successful"   
    fh.close()


try:
    fh = open ("text_file", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: Can\'t find file or read data."
else:
    print "Written content in the file successfully"

