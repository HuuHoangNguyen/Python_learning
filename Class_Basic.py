#!/usr/bin/python

"""
    Create a class
class ClassName:
    'Optional class documentation string'
    class_suite
"""
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
"""