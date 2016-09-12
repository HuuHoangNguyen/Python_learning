#!/usr/bin/python

# The list  are enclosed in brackets ([]) and their element
# and size can be changed, while tuples are enclosed in parenthese
# ( () ) and cannot be updated. The Tuples can be thought of as
# read-only of list

aTuple = ( 'abcd', 786, 2.23, 'John', 70.2)
bTuple = (  123, 'Vien')

print aTuple                         # Print complete tuple
print aTuple[0]                      # Preint first element of the tuple
print aTuple[1:3]                    # Print element starting from 2nd till 3rd
print aTuple[2:]                     # Print elements starting from 3rd element
print bTuple                        # Print tuple tw0 times
print aTuple + bTuple             # Print concatenated lists

val_tuple = ('abcd', 786, 2.23, 'John', 70.2 )
val_list = ['abcd', 786, 2.23, 'John', 70.2]
#
print "\nPrint the list and tuple before change: "
print val_tuple
print val_list

#val_tuple[2] = 100.2
val_list [2] = 100.2

print "\nPrint the list and tuple after change"
print val_tuple
print val_list

print "=================================================="
tuple1 = ('physics', 'schematic', 1997, 2000)
tuple2 = (1,2, 3, 4, 5, 6, 7)
print "tuple1[0]: ", tuple1[0]
print "tuple2[1:5]: ", tuple2[1:5]

print "=================================================="
print "Updating Tuples"
print "Tuples are immutable which means you can not update or change the value of tuples element."
print "You can able to take portions of existing tuples to creatr new tuples as the following example demonstrates"
tuple1 = (12, 34, 56)
tuple2 = ('abc', 'xyz')
#Following action is n ot valid for tuples
#tuple1[0] = 100
#so let's create a new tuple as follows
tuple3 = tuple1 + tuple2
print "Tuple3 is: ", tuple3

print "=================================================="
print "Delete Tuple Elements"
print "Removing individual tuple elements is not possible. There is, of course, nothing"
print "wrong with ptting together another tuple with the undesired element discarded"

tup = ('physics', 'schemistry', 1997, 2000)
print "The tuple is: ", tup
del tup
print "After deleting tup: "
#print tup

print "=================================================="

print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="
print "=================================================="




