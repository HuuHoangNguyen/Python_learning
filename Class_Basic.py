#!/usr/bin/python

"""
    Create a class
class ClassName:
    'Optional class documentation string'
    class_suite
"""
print "=================================================="
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1
    
    def displayCount(self):
        print "Total Employee %d" %Employee.empCount
    
    def displayEmployeeInfo(self):
        print "Name : ", self.name,  ", Salary: ", self.salary, "Age: ", self.age



emp1 = Employee("Zara ", 2000, 25)
emp2 = Employee("Manni", 5000, 35)           
emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()
print "Total Employee %d" % Employee.empCount
print "Document of class is %s" %Employee.__doc__
print "Class name %s" %Employee.__name__
print "Module class is %s" %Employee.__module__
# print "Base class is %s" %Employee.__bases__

"""
    Destroyin Objects (Farbage Collection)
Python deletes unneeded objects(built-in types or class instances)
automatically to free the memory space. The process by which Python 
periodically reclaims blocks of memory that no longer are in use 
is termed Garbage Collection
    You normally will not notice when the garbage collector destroys and 
    orphaned instance and reclaime its space. But a class can implement the 
    special method __del()__, called a destructor, that is invoked whene the
    instance is about to be destroyed. This method might be used to clean up
    any none memory resources used by an instance.
"""
print "=================================================="
class Point:
    def __init__(self, x=0, y =0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

pta = Point(10,10)
pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1), id(pt2), id(pt3) #Print the ids of objects
del pt1
del pt2
del pt3

"""
    Class Inheritance
Instead if starting from cratch, you can create a class by deriving it from a 
preexisting class by listing the parent class in marentheses after the new class name.

The child clas inherits the attibutes of its parrent class, and you can use those atributes
as if they were defined in the child class. A chiuld class can also override data members and 
methods from the parent.import

Syntax:
Derived classes are declared much like their parent class; however, a list of base classes to inherit
from is given after the class name,
        class SubClassName(ParentClass1[, ParentClass2, ....]):
            'Optional class documentation string.'
            class_suite.            
"""
print "=================================================="
class Parent:       #Define parent class
    parentAttr = 100
    def __init__(self):
        print "Calling the parent constructor"

    def parentMethod(self):
        print "Call the parent method"
    
    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute: ", Parent.parentAttr
        return Parent.parentAttr
    
class Child(Parent):    #Define child class
    def __init__(self):
        print "Calling child contructor"
    
    def childMethod(self):
        print "Calling child method"

c = Child()         #instance of child 
c.childMethod()     #child calls its def FunctionName(self, args):
c.parentMethod()    #call parent's method
c.setAttr(200)      #Again call parent's method.
d = c.getAttr()     #again call parent's method


"""
======================================================================================
You can use 'issubclass()' or 'isinstance()' function to check a relationships 
of two classes and instances.
    - The 'issubclass(sub, sub)': boolean function returns true if the given subclass sub
    is indeed a subclass of the supperclass sup.
    The 'isinsatance(obj, Class)': boolean function return true if  obj is an instance of class Class 
    or is an instance of a subclass if Class
"""

"""
======================================================================================
    Overddiding Methods
You can always override your parent class methods. One reeason for ovverriding
parent's method is because you may want special or different functionality in 
your subclass.
"""

print "=================================================="
class Parent_c: #define parent class
    def myMethod(self):
        print "Calling parent method"
class Child_c(Parent_c):   #define child class
    def myMethod(self):
        print "Calling child method"

c = Child_c()     #instance of Child
c.myMethod()    #Child call overriding method.     


"""
======================================================================================
    Base Overddiding Methods
1. __init__(self[,args..]): Constructor
2. __del__(self): Evatuatable string respresentation
3. __repr__(self): Evaluatable string representation
4. __str__(self): Prinable string representation
5. __cmp__(self): Object comparison
"""

"""
======================================================================================
     Overddiding Operators
Suppose you have created a Vector class to represent two-dimensional vectors, 
what happens when you the plus operator to add them? Most likely Python will yell
at you.

You could, however, define the __add__ method in your class to perform vector addition
and then the plus operator would behave as per expectation.
"""
print "=================================================="
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "Vector (%d.%d)" %(self.a, self.b)
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

"""
======================================================================================
     Data Hiding
An objects;s attributrs may or may not be visible outside the class definition. You need 
to name attributes with a double underscore prefix, and those attriubutes athen are not be directly visble to outsiders.

"""
class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount +=1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

print counter._JustCounter__secretCount
