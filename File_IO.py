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
    
Here are parameter detail:
    + file_name: The file_name argument is a string value that contains the name of 
                 the file that you want to access.
    + access_mode: The access_mode determines the mode in which the file haas to be opened. 
                   i.e read, write, append, etc. A complete list of possible value s is given
                   below in the table. This is optional parameter and the default file access 
                   mode is read(r)

    + buffering: If the buffering value is set to 0, no buffering takes place. If the buffering 
    value is 1, line buffering is performed while accessing a file. If you specify the buffering 
    value as an integer greater than 1, then buffering action is performed with the indicated buffer size.
    If negative, the buffer size is the system default( default behavior)

===============================================================================================
Modes           Description
 r          Opens a file for reading only. The file pointer is placed at the begining of the file.
            This is the default mode.

 rb         Opens a file for reading onl in binary format. The file pointer is place at the begin of the file. 
            This is the default mode.

 r+        Opens a file for both reading and writing. Teh file pointer placed at the begin of the file. 

 rb+       Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file

 w         Opens a file for writing only. Overwrites the file if the file exits. If the file does not exist, creates a new file
           for writing.
 
 wb        Opens a file for writin only. Overwrites the file if the file exists. If the file doed not exist, creates a new file for 
           writing.

 w+        Open a file for both writing and reading. Overwrites the file if the file exist. If the file does not exist, 
           creates a new file for writing.

 wb+      Open the file for both writing and reading. Overwrite the file if the file exist. If the file does not exist, create a new 
          file for reading and writing.

 a        Open the file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append
          mode. If the file node exist, it creates a new file for writing.
        
 ab       Open a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in 
          the append mode. If the file does not exist. It create a new file for writing.

 a+      Open a file for appeding and reading. The file pointer is at the end of the file if the file exists. The file open in the deppend mode. 
         If the file does not exist, it creates a new file for writing.

 ab+     Open a file for appending and reading in binary mode. The file pointer is at the end of the file if the file exists. The file open in append
         mode. If the file does not exist, it creates a new file for reading and writing.

===============================================================================================
The file Object Attributes:

Once a file is opened adn you have one file object, you can get various information releted to that file.close
Here is a list of all atributes related to file object




"""


