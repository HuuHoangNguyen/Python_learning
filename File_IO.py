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
# Str = raw_input("Enter yout input: ")
# print "Received input is: ", Str

"""
THis prompts you to enter any string and it would display same strring on the screen.
When I  typed "Hello Python!", its output is like this.
"""

print """
The input[(prompt)] functions is equivalent to raw_input, expect that it assumes the input is a valid Python expression and returns the evaluated
result to you
"""
# Str = input("Enter your input")
# print "Received input is: ", Str

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

    Attribute           Decription 
 file.closed            Return true if file is close, false otherwise
 file.mode              Return access mode with which file was opened.
 file.name              Return name of the file.close
 file.softspace         Returns false if space explicitky required with print, true otherwise.
"""

#Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not :", fo.closed
print "Opening mode: ", fo.mode
print "Softspace flag: ", fo.softspace


"""
The close() Mothod
The 'close()' mothod of a file object flushes any unwritten infomataion and closes
the file object, after which no more writing can be done.

Python automatically closes a file when the reference object of the file is reasigned 
to another file. It is a good practice to use the 'close()' method to close a file.

Syntax: 'fileObject.close()'
"""

print "==========================================================="
#close open file
print "Close file and check"
fo.close()
print "Closed or not :", fo.closed

"""
Reading and writing Files
The 'file' object provides a set of access methods to make our lives easier.
We would see how to use 'read()' adnd "write()" methods to read and writes files.

The write() Method.
The 'write()' method writes string to an open file. It is important to note that
Python strings can have binary data and not just text.

The write() method does not add a newline character ('\n') to the end of string.

Syntax: fileObject.write(string)
"""

print "==========================================================="
#Open a file 
fo = open ("foo.txt", "wb")
fo.write("Python is a great language.\nYeah its great!!\n")

#Close open file 
fo.close()


print "==========================================================="
"""
The read() Mothod
The read() method reads string from an open file. It is important to note that Python string can have binary data, Apart from text.

Syntax 
    fileObject.read([count])

    Here, passed parameter is the number of btes to be read from the opend file. This method starts reading from begining of the file,
    and if count is missing, then it tries to read as much as posible, maybe until the end of file. 
"""

fo = open("foo.txt", "r+")
Str = fo.read(10)
print "Read String is : ", Str

#Close open file
fo.close()

print "==========================================================="
"""
    File Posibles
The 'tell()' method tells you the current position within the file. in other worlds, the next read or write will 
occur at that many bytes from the begining of the file

The 'seek(offset[, from])' method changes the current file position. The offset argumen indicates the number of bytes to be move.
The from argument specifies the reference position from where the byte are to be moved.
    If from iss set to 0, it means use thee beginning of the file as the reference position and 1 means use the current position 
    as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.
    
"""
#Open the file
fo = open("foo.txt", "r+")
Str = fo.read(10)
print "Read string is: ", Str

#Check current position
position = fo.tell()
print "Current the file position: ", position

#Reposition poiter at the begin one again
position = fo.seek(0, 0)
Str = fo.read(10)
print "Again read String is: ", Str

#Close the file
fo.close()

print "==========================================================="
"""
    The remove() Method 
You can use the remove() method to delete file by supplying the name of the file to be deleted as the argument


"""
import os

#Remove foo.txt file

os.remove("foo.txt")


print "==========================================================="
"""
    Directories in Python
All files are contained within various directories, and Python has no problem hangling these too.
The 'os'' module has several mothods that help you create, remove, and change directories. 

    The 'mkdir()' Methon

You can use the 'mkdir()' method of the 'os' module to create directories in the current directory.
You need to supply an argument to this method which contains the name if the directory to be created.

    Syntax :    os.mkdir("newdir")
    
"""

import os
import time
#Create a directory 'test'
os.mkdir('Test')
time.sleep(5)
os.rmdir("Test")

print "==========================================================="
"""
    The chdir() Method 
You can use the 'chdir()' method to change the current directory. The 'chdir()' method takes an argument,
which is the name of the directory that you want to make the current directory.
    Syntax:     os.chdir("newdir")

"""


Str = os.chdir("/home/huuhoang/Src")

print "==========================================================="
"""
    The 'getcwd()' Method 
The getcwd() method displays the current working directory
    Syntax: os.getcwd()
"""
Str = os.getcwd()
print "The current dir is: ", Str


