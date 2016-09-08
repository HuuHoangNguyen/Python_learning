#!/usr/bin/python

# The list  are enclosed in brackets ([]) and their element
# and size can be changed, while tuples are enclosed in parenthese
# ( () ) and cannot be updated. The Tuples can be thought of as
# read-only of list


print "=================================================="
list1 = ['abc', 786, 2.23, 'John', 70.2 ]
tinylist = [ 123, "Vien"]

print list1                  # Print complete list
print list1[0]               # Print first element of the list
print list1[1:3]             # Print elements starting from 2nd till 3rd
print list1[2:]              # Print elements starting from 3rd element

print tinylist * 2          # Print list two times
print list1 + tinylist       # Print concatenated lists


print "=================================================="
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print "list1[0] = ", list1[0]
print "list2[1:5] = ", list2[1:5]

print "=================================================="
# You can update single mor multiple elements of lists by giving the slice on the left-hand side
# of the assignment operator, and you can add to elements in a list with the append() method.
list_a = ['physics', 'chemistry', 1997, 2000]
print "Value available at index 2: ", list_a[2]
list_a[2] = 2001
print "New value available at index 2: ", list_a[2]

print "=================================================="
# To remove a list element, you can use either the del statement if you know exactly which
# element(s) you are deleting or the remove() method if you do it know
list1 = ['physics', 'chemistry', 1997, 2000]
print list1
del list1[2]
print "After deletin value at index 2: "
print list1

print "=================================================="
print "Basic List Operations"
print "Lists respond to the + and * operators much like string; They mean concatenation and repetition here too,"
print "except that the result is a new list, not a string."
print "If fact, list respond to all of the general sequence operations we used on string in the prior chapter."
print " Python Expression               Results                         Description"
print " len([1, 2, 3])                    3                               Length"
print " [1, 2, 3] + [4, 5, 6]             [1, 2, 3, 4, 5, 6]              Concatenation"
print " ['Hi!'] * 4                       ['Hi!', 'Hi!', 'Hi!', 'Hi!']    Repetition"
print " 3 in [1, 2, 3]                   True                            Membership"
print " for x in [1, 2, 3]: print x       1 2 3                           Iteration"

print "=================================================="
print " Indexing, Slicing, and Martixes"
print " Because lists are sequences, indexing and slicning work the same way for list as they do"
print " do for strings."
L = ['spam', 'Spam', 'SPAM']
print "L[2] = ", L[2]
print "L[-2] =  ", L[-2]
print "L[1:] = ", L[1:]

print "=================================================="
print "cmp(list1, list2): Compares elements of both lists"
list1, list2 = [123, 'xyz'], [456, 'abc']
print "the list1 is : ", list1
print "the list2 is : ", list2
print "cmp(list1, list2) = ", cmp(list1, list2)
print "cmp(list2, list1) = ", cmp(list2, list1)
list3 = list2 + [786];
print "the list3 = ", list3
print "cmp(list2, list3) = ", cmp(list2, list3)

print "=================================================="
print "len(list): Given the total length of the list "
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print "the list1 is: ", list1
print "the first list length: ", len(list1)
print "the list2 is: ", list2
print "the second list length: ", len(list2)

print "=================================================="
print "max(list): Returns item that have max value in the list"
print "min(list): Returns item that have min value in the list"
lis1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
print "the list1 is: ", list1
print "the list2 is: ", list2
print "Max value element of list1: ", max(list1)
print "Max value element of list2: ", max(list2)
print "Min value element of list1: ", min(list1)
print "Min value element of list2: ", min(list2)

print "=================================================="
print "list(seq): Converts a tuple into list"
aTuple = (123, 'xyz', 'zara', 'abc')
print " The tuple is: ", aTuple
aList = list(aTuple)
print " The list is :", aList

print "=================================================="
print "list.append(obj): Appends objects obj to list"
aList = [123, 'xyz', 'zara', 'abc']
print "The list is: ", aList
aList.append(2009)
print "The List after updated: ", aList

print "=================================================="
print "list.count(obj): Returns count of how many times obj occurs in list"

print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="
