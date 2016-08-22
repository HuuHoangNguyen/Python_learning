#!/usr/bin/python

# The list  are enclosed in brackets ([]) and their element
# and size can be changed, while tuples are enclosed in parenthese
# ( () ) and cannot be updated. The Tuples can be thought of as
# read-only of list

tuple = ( 'abcd', 786, 2.23, 'John', 70.2)
tinytuple = (  123, 'Vien')

print tuple                         # Print complete tuple
print tuple[0]                      # Preint first element of the tuple
print tuple[1:3]                    # Print element starting from 2nd till 3rd
print tuple[2:]                     # Print elements starting from 3rd element
print tinytuple                     # Print tuple tw0 times
print tuple + tinytuple             # Print concatenated lists

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
