#!/usr/bin/python

print "=================================================="
aDict = {}
aDict['one'] = "This is one"
aDict[2] = "This is two"

tinyDict = { 'name': 'john', 'code':4472, 'dept': 'sales'}

print aDict['one']                   # Print value for 'one' key
print aDict[2]                       # Print value for 2 key
print tinyDict                       # Print complete dictionary
print tinyDict.keys()                # Print all the keys
print tinyDict.values()              # print all the values

print "=================================================="
""" Each key is se[arated from it value by a colon (:), the items are separates by commas,
and the whole thing is enclosed in curlt braces, An empty dictionary without any items is written 
with just teo curly braces, like this: '{}'

Keys are unique within a dictionary while values may not be. The values of a dictionary can be og any type,
but the keys must be of an immutable data type such as string, numbers, or tuples

To access dictionary elements, you can use the familiar square brackets along with the KeyboardInterrupt
to obtain its values. 
"""

aDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "aDict['name']: ", aDict['Name']
print "aDict['Age'] : ", aDict['Age']

print "=================================================="
print "If we attempt to acces a data item with a key, which is not part of the dictionarty,"
print "we get an error as following:"
aDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print "aDict['Alice']: ", dict['Alice']

print "=================================================="
print "Updating Dictionary"
print "You can update a dictionary by adding a new entry or a key-value pair, modifying and"
print "existing entry, or deleting an existing entry as shown below in the simple example"
aDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
aDict['Age'] = 8                # Update existing entry
aDict['School'] = 'DPS School'  # Add new entry
print "aDict['Age']: ", aDict['Age']
print "aDict['School']: ", aDict['School']

print "=================================================="
print "Delete Dictionary Elements"
print "You can either remove individual dictionary elements or clear the entire contents of"
print "dictionary. You can also delete entire dictionary in a single operation."
aDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "------------"
for element in aDict:
    print element, ": ", aDict[element]
del aDict['Name']           #Remove entry with key "Name"
#aDict.clear()               #Remoe all entry dictionary
#del aDict
print "------------"
for element in aDict:
    print element, ": ", aDict[element]
print "dict['Age']: ", aDict['Age']
print "dict['Class']: ", aDict['Class']




print "=================================================="
print "Properties of Dictionary Keys"
print "Dictionay values have no restrictions. They can be any arbitrary Python object. either standard"
print "objects or user-defined objects. However, same is not true for the keys."
print "There are two important points to remember about dictionary keys"
print "a. More than one emtry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered"
print "during assignment, the last assigment wins"
aDict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "aDict['Name']: ", aDict['Name']

print "=================================================="
print "b. Keys must be immutable. Which means you can use strings. numbers or tuples as dictionary keys"
print "but somthing like ['key'] is not allowed"
#aDict = {['Name']: 'Zara', 'Age': 7}
#print "aDict['Name']: ", aDict['Name']

print "=================================================="
print "cmp(dict1, dict2): Compares elements of both dicts"
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age':27}
dict4 = {'Name': 'Zara', 'Age':7}
print "Returns value: %d " % cmp(dict1, dict2)
print "Returns value: %d " % cmp(dict2, dict3)
print "Returns value: %d " % cmp(dict3, dict4)
print "Returns value: %d " % cmp(dict4, dict1)

print "=================================================="
print "len(dist): Gives the total length of the dictionary. This would be qual to the number of items in the dictionary"
aDict = {'Name': 'Zara', 'Age': 7}
print "Length of aDict is %d " % len(aDict)
print "=================================================="
print "str(dist); Produces a printable string representation of a dictionary"
aDict = {'Name': 'Zara', 'Age': 7}
print "Equivalent string: %s" % str(aDict)

print "=================================================="
print "type(dist): Returns the type of the passed variable. If passed variable is dictionary, then it woukd return a dictionary type"
aDict = {'Name': 'Zara', 'Age': 7}
print "Variable Type: %s " % type(aDict)

print "=================================================="
print "dict.clean(): Removes all element of dictionary dict"
aDict = {'Name': 'Zara', 'Age': 7}
print "Length of aDict : %d " %len(aDict)
print "The aDict is: %s " %str(aDict)
aDict.clear()
print "Length of aDict: %d " %len(aDict)
print "The aDict is: %s " %str(aDict)

print "=================================================="
print "dist.copy():Returns a shollow copy of dictionary dict"
aDict = {'Name': 'Zara', 'Age': 7}
bDict = aDict.copy()
print "The aDict is: %s" %str(aDict)
print "The bDict is: %s" %str(bDict)

print "=================================================="
print "dict.fromkeys(seq [, value]): Create a new dictionary with keys from seq and values set to value"
seq =('name', 'age', 'sex')
aDict = dict.fromkeys(seq)
print "New Dictionary: %s " %str(aDict)
bDict = dict.fromkeys(seq, 10)
print "New Dictionary: %s " %str(bDict)

print "=================================================="
print "dict.get(key, default=None): For 'key' key, returns value or default if key not in dictionary"
aDict = {'Name': 'Zara', 'Age': 7}

print "Value: %s" % aDict.get('Age')
print "Value: %s" % aDict.get('Education')
print "Value: %s" % aDict.get('Education', 'Never')


print "=================================================="
print "dist.has_key(key): Returns True if key in dictionary dict, False otherwise"
aDict ={'Name': 'Zara', 'Age': 7}
print "Value: %s "% aDict.has_key('Age')
print "Value: %s "% aDict.has_key('Sex')

print "=================================================="
print "dict.items(): Returns a list of dist's(key, value) tuple pairs"
aDict = {'Name': 'Zara', 'Age': 7}
print "Value: %s" %aDict.items()

print "=================================================="
print "dict.key(): Returns list of dicrionary dict's keys'"
aDict = {'Name': 'Zara', 'Age': 7}
print "Value : %s " %aDict.keys()

print "=================================================="
print "dict.setdefault(key, default=None): Similar to get(), but will set dict[key] = default if key is not already in dict"
aDict = {'Name': 'Zara', 'Age': 7}
print "The aDict is: %s " % str(aDict)
print "Value: %s "% aDict.setdefault('Age', None)
print "Value: %s "% aDict.setdefault('Sex', None)
print "the sDict is: %s" %str(aDict)

print "=================================================="
print "dict.update(dict2): Adds dictionary dict2's key-value to dict"
aDict = {'Name': 'Zara', 'Age': 7}
bDict = {'Sex': 'Female'}
print "The aDict is: %s " %str(aDict)
print "The bDict is: %s " %str(bDict)
aDict.update(bDict)
print "The aDict is: %s " %str(aDict)

print "=================================================="
print "dict.values(): Returns list of dictionary dict's values"
aDict = {'Name': 'Zara', 'Age': 7}
print "The values in aDict is %s" % aDict.values()