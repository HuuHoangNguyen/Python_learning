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
print "Document of class is %s" %Employee.__main__
print "Document of class is %s" %Employee.__doc__