#!/usr/bin/python

def myprint (str):
    "This is a passed string into this function"
    print str
    return

def mychange(mylist):
    "This change a passed list into this function"
    mylist.append([1,2,3,4])
    print "Value inside the mylist is: ", mylist
    return

def mychange2(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  #This would assign new reference in mylist
    print "Value inside the function: ", mylist
    return
def printinfo(name, age):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age : ", age
    return

def printinfo2(name, age=35):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age : ", age
    return

"""
def FunctionName([format_args, ]*var_args_tuble):
    "Function docstring"
    Function_suite
    return [expression]
"""
def PrintInfo3(Arg1, *VarTuple):
    "This prints a variable passed arguments"
    print "Output is: "
    print Arg1
    for var in VarTuple:
        print var
    return


"""
THE Anonymous Functions
These functions are called anonymous because they are not declared in the 
standard manner by using the def keywork. You can use the 'lambda' keywork to
create small anonymous functions.
    Lambda forms can take any number of arguments but return just one value 
    in the form of an expression.They cannot contain commands or multiple expressions

    An  anonymous function cannot be a direct call to print because lambda requires an expression

    Lambda functions have their own local nammespace and cannot access variables other than those 
    in their parameter list and those in the global namespace.

    Although it appears that lambda's are a onle-line version of a function, they are not 
    equivalent to inline statements in C or C++, whose putpose is by passing function stack 
    allocation during invocation for performance reasons.

Syntax: 
    lanbda [arg1 [,arg2, ..., argn]]: expression
"""
#Function definition if here
MySum = lambda Arg1, Arg2 : Arg1 + Arg2

"""
    The Return Statement
The statement return [expression] exits a function, optionally paaing back andexpression to the caller.
A return statement with no arguments is the same as return None
"""

def MySum2(arg1, arg2):
    "Add both a parameters and return them."
    total = arg1 + arg2
    print "Inside the function: ", total
    return total

"""
Scope of Variables
    All variables in a program may not be accessible at all localtions in that program.
This depends on where you have declared a variable.
    THe scope of a varible determines the portion of the program where you can access 
a particular identifier. There are two basic scopes of variables in Python.

        Global variables.
        Local variables

 Global & Local variables
    Variables that are defined inside a function body have a local scope,
    and those defined outside have a global scope.
    
    This means that local variables can be accessed only inside the function in which
    they are declared, whereas global variables can be accessed thoughout the program
    body by all functions. When you call a function, the variables declared inside it 
    are brought into scope.
"""

total = 0   # This is global variable
def MySum3(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1 + arg2
    print "Inside the function local total: ", total
    return total



def main():
    print "\n-----------------------------------------"
    myprint("I'm first call to user defined function!")
    myprint("Agaim second call to the same functions")

    print "\n-----------------------------------------"
    mylist = [10, 20, 30]
    print "the mylist inside 'mychange' function ", mylist
    mychange(mylist)
    print "the mylist after 'mychange' function ", mylist

    print "\n-----------------------------------------"
    mylist = [10,20, 30]
    print "The mylist is: ", mylist
    mychange2(mylist)
    print "Values outside the function ", mylist

    print "\n-----------------------------------------"
    # myprint()
    myprint (str = "My string")

    print "\n-----------------------------------------"
    printinfo(age=50, name="miki")
    printinfo2(age=50, name="HuuHoang")
    printinfo2(name="H_H_Nguyen")

    print "\n-----------------------------------------"
    PrintInfo3(10)
    PrintInfo3(70, 60, 50)

    print "\n-----------------------------------------"
    print "Value of total 10 & 20 is : ", MySum(10, 20)
    print "Value of total 20 & 20 is : ", MySum(20, 20)

    print "\n-----------------------------------------"
    oTotal = MySum2(10, 20)
    print "Outside the function: ", oTotal
    
    print "\n-----------------------------------------"
    MySum3(10, 25)
    print "Outside the function global total: ", total

if __name__ == "__main__":
    main()
