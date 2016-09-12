#!/usr/bin/python

print "=================================================="
adict = {}
adict['one'] = "This is one"
adict[2] = "This is two"

tinydict = { 'name': 'john', 'code':4472, 'dept': 'sales'}

print adict['one']                   # Print value for 'one' key
print adict[2]                       # Print value for 2 key
print tinydict                       # Print complete dictionary
print tinydict.keys()                # Print all the keys
print tinydict.values()              # print all the values
print "=================================================="
