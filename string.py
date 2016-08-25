#!/usr/bin/python

str = 'Hello world! '

print str           # Print comple string
print str[0]        # Print first character of the string
print str[2:5]      # Print characters start from 3rd to 5th
print str[2:]       # Print string starting from 3rd character
print str * 2       # Print the string two times
print str + " TEST" # Print concatenated string

print "=================================================="
print "string varibale"
str1 = 'Hello World!'
str2 = "Python Programming"

print "str1 is : ", str1
print "str2 is : ", str2
print "str1[0] : ", str1[0]
print "str2[1:5] : ", str2[1:5]

print "=================================================="
print "Updating strig"
str  = "Hello World"
print "Updating string: ", str[:6] + 'Python'
for i in range(1,10):
    print "\a"

print "=================================================="
str = "HuuHoang Nguyen"
for str_prt in str:
    print str_prt

print "=================================================="
print " String formatting operator"
print "My name is %s ans weight is %d kg!" % ('HuuHoang', 60)


print "=================================================="
print "triple quotes"
para_str = """this is a long string that is made up of several lines and
none-printable character such as TAB ( \t ) nd they will show up that way when displayed.
NEWLINEs with in string, where explicitly given like this within the brackets [ \n ], or just
a NEWLINE within the variable assignment will also show up.
"""
print para_str

print "=================================================="
print "capitabize() : Return a copy the string only its first character capitalized."
str = "this is tring example ... wow !!!"
print "str is ", str
print "str.capitabize() : ", str.capitalize()

print "=================================================="
print "str.center (with. fillchar): Returns a space-padded string with original string centered to a total of width columns "
str = "this is string example ... wow!!!"
print "str is ", str
print "str.center(40, 'a')", str.center(40, 'a')

print "=================================================="
print "count(str, beg = 0, end = len(string)): Count how many times str occures in string or in a substring of string  if starting insex beg and ending index end are given"
str = "this is string example ... wow!!!"
sub ="i"
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

print "=================================================="



print "=================================================="
