#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = { 'name': 'john', 'code':4472, 'dept': 'sales'}

print dict['one']                   # Print value for 'one' key
print dict[2]                       # Print value for 2 key
print tinydict                      # Print complete dictionary
print tinydict.keys()                # Print all the keys
print tinydict.values()              # print all the values
