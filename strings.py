#!/usr/bin/python
from string import maketrans            #

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
print "decode(encoding='UTF-8', errors='strict'): Decode the string using the codec registered for encoding."
print "Encoding defaults to the default tring encoding"
Str = "this is tring example...wow!!!"
print "String is ", Str
#Str = Str.encode('base64', 'strict')
#print "Encoded string: " + str
#print "Encoded String : " + Str.decode('base64', 'strict')

print "=================================================="
print "endswith(suffix , start=0, end=len(string)) :  Determines if string or substring (if start index start and ending index end are given) "
print "ends with suffix; returns true if so and false otherwise"
str = "this is string example...wow!!!"
suffix="wow!!!"
print str.endswith(suffix)
print str.endswith(suffix, 20)
suffix = "is"
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

print "=================================================="
print "expandtabs(tabsize = 8): Expands tabs in string to multiple space; default to 8 spaces per tab if tabsize not provided"
str = "this is \t string example ...wow!!!"
print "string with expanded tab is 4  : " + str.expandtabs(4)
print "string with expanded tab is 8  : " + str.expandtabs(8)
print "string with expanded tab is 2  : " + str.expandtabs(2)

print "=================================================="
print "find(str, begin=0, end=len(string) : Determin if str occurs in string or in a substring of string if starting index begin and )"
print "ending index end are given returns index if found and -1 otherwise"
str1 = "this is a string example....wow!!!"
str2 = "exam"
print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)

print "=================================================="
print "index(str, begin-0, end=len(string)): Same as find(), but raises an exception "
print "if str not found"
str1 = "this is string example...wow!!!"
str2 = "exam"

print str1.index(str2)
print str1.index(str2, 10)
#print str1.index(str2, 40)

print "=================================================="
print "isalnum(): Returns true if string has at least 1 character and all characters"
print "are alphanumeric and false otherwise"
str = "this2009" #No space in this string
print "String is: ", str
print str.isalnum()

str = "this is string example...wow!"
print "String is: ", str
print str.isalnum()

print "=================================================="
print "isalpha(): Returns true if has a least 1 character and all characters"
print "are alphabetic and false otherwise"
str = "this"    # No space & digit in this string
print "String is: ", str
print str.isalpha()

str = "this is string example....wow!!!"
print "String is: ", str
print str.isalpha()

print "=================================================="
print "isdigit(): Returns true if string contains only digits and false otherwise"
str = "123456"          #Only digit in this string
print "String is: ", str
print str.isdigit()

str = "this is string example....wow!!!"
print "String is: ", str
print str.isdigit()

print "=================================================="
print "islower(): Returns true if string has at least 1 cased character and all cased characters are in "
print "lowercase and false otherwise"
str = "THIS is string example....wow!!!"
print "String is: ", str
print str.islower()

str = "this is string example...wow!!!"
print "String is: ", str
print str.islower()

print "=================================================="
print "isnumeric(): Returns true if a unicode string contains only numeric character anf false otherwise"
str = u"thisi2009"
print "String is: ", str
print str.isnumeric()

str = u"23443434"
print "Strign is: ", str
print str.isnumeric()

print "=================================================="
print "isspace(): Returns true if string contains only whitespace character and false otherwise"
str = "                "
print "String is :", str
print str.isspace()

str = "This is string example....wow!!!"
print "String is: "
print str.isspace()

print "=================================================="
print "istitle(): Returns true if string is properly 'titlecased' and false otherwise"
str = "This Is String Example...Wow!!!"
print "String is: ", str
print str.istitle()

str = " This is string example....wow!!!"
print "String is : ", str
print str.istitle()

print "=================================================="
print "isupper(): Returns true if all characters are in uppercase and false otherwise"
str = "THIS IS STRING EXAMPLE....WOW!!!"
print "String is: ", str
print str.isupper()

str = "THIS is string example....wow!!!"
print "String is: ", str
print str.isupper()

print "=================================================="
print "join(seq): Merges(cncatenated) the string reoresentations of elements in sequence sew into "
print "a string, with separator string"
str = "_"
seq = ("a", "b", "c")       #This is sequence of string
print str.join(seq)

print "=================================================="
print "len(string): Returns the length of string"
str = "This is string example....wow!!!"
print "The string is: ", str
print "Length of the string is: ", len(str)

print "=================================================="
print "ljust(wirdth[,fillchar]): Returns a space-padded string wirh the original string left-justified to a total of with columns"
str = "this is string example....wow!!!"
print "The string is: ", str
print str.ljust(50, '0')

print "=================================================="
print "lower(): Converts all uppercase letters in string to lowercase"
str = "THIS IS STRIng EXAMPLE....WOw!!!"
print "The string is: ", str
print str.lower()

print "=================================================="
print "lstrip(): Removes all leading whitespace in string"
str = "     this is string example....wow!!!"
print "The string is ", str
print str.lstrip()

str = "88888888This is string example....wow!!!88888888"
print "The string is: ", str
print str.lstrip('8')

print "=================================================="
#from string import maketrans    # Required to call maketrans function
print "maketrans(): Returns a translation table to be used in translate function"
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str ="this is string example....wow!!!"
print str.translate(trantab)

print "=================================================="
print "max(str) or min(str): Returns the max or min alphabetical character from the string str"
str = "this is really a string example...wow!!!"
print "The string is: ", str
print "Max character is : " + max(str)

str = "this_is_really_a_string_example...wow!!!"
print "The string is: ", str
print "Min character is : " + min(str)

print "=================================================="
print "replace(old, new [,max]): Replaces all occurrences of old in string "
print "with new or at most max occurrences if max given"
str = "this is string example...wow!!! this is really string"
print "The string is: ", str
print str.replace("is", "was")
print str.replace("is", "was", 3)

print "=================================================="
print "rfind(str, begin=0,end=len(str)): Same as find(), but search backwards in string"
str1 = "this is really string example....wow!!!"
str2 = "is"

print "The str1 is: ", str1
print "The str2 is: ", str2

print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)
print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 10)



print "=================================================="
print "rindex(str, begin=0, end=len(string)): Same as index(). but search backwards in string"
str1 = "this is string example....wow!!!"
str2 = "is"
print "The str1 is: ", str1
print "The str2 is: ", str2
print str1.rindex(str2)
print str1.rindex(str2)

print "=================================================="
print "rjust(width,[fillchar]): Return a space-padded string with the original string right-justified to a total of width columns"
str = "this is string example....wow!!!"
print "The string is: ", str
print str.rjust(50, '0')

print "=================================================="
print "split(str="",num=string.count(str)): Splits string according to delimiter str"
print "(space if not provided) and returns list of substrings; split into at most num substrings if given"
str = "Line1-abcdef \nLine2-abc \n\nLine4-abcd"
print "The string is: ", str
print str.split()
print str.split(' ', 1)

print "=================================================="
print "slpitlines(num=string.count(str)): Splits string at all(or num) NEWLINEs and returns a list of each line with NEWLINEs removed "
str = "Line1-a b c d e f\nLine2- a b c \n\nLin4- a b c d"
print str.splitlines()
print str.splitlines(0)
print str.splitlines(3)
print str.splitlines(4)
print str.splitlines(5)

print "=================================================="
print "startswith(str, begin=0, end=len(string)): Determines if string or s substring of string"
print "(if starting index begin and ending index end are given) starts with substring str; return true if"
print "so and false otherwise"
str = "this is string example....wow!!!"
print "The string is: ", str
print str.startswith('this')
print str.startswith('is', 2, 4)
print str.startswith('this', 2, 4)

print "=================================================="
print "strip([char]): Performs both lstrip() and rstrip() on string"
print "The string is: ", str
str = "0000000this is string example....wow!!!0000000"
print str.strip('0')

print "=================================================="
print "swapcase(): Inverts case for all letters in string"
str = "this is string example....wow!!!"
print "The string is: ", str
print str.swapcase()
str = "THIS IS STRING EXAMPLE....WOW!!!"
print str.swapcase()

print "=================================================="
print "title(): Return titlecased version of string, that is, all words befin with uppercase and the rest are lowercase"
str = "this is string example...wow!!!"
print "The string is: ", str
print str.title()

print "=================================================="
print "translate(table, deletechars=""): Translates string according table str(256 chars), removing those in the del string"
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
#print "trantab is: ", trantab
str = "this is string example....wow!!!"
print "The string is: ", str
print str.translate(trantab)

str = "this is string example...wow!!!"
print str.translate(trantab, 'xm')

print "=================================================="
print "upper(): Converts lowercase letters in string to uppercase"
str = "This is string exmaple...wow!!!"
print "The string is: ",str
print "str.capitabize(): ", str.upper()

print "=================================================="
print "zfill(width): Return original string leftpadded with zeros to a totsl of width character; intended for numbers, "
print "Zfill() retains any sign given(less one zero)"
str = "this is string example....wow!!!"
print "The string is: ", str
print str.zfill(40)
print str.zfill(50)

print "=================================================="
print "isdecimal(): Returns true if a unicode string contains only decimal character and false otherwise"
str = u"this2009"
print "The string is: ", str
print str.isdecimal()

str = u"23443434"
print "The string is: ", str
print str.isdecimal()

print "=================================================="
