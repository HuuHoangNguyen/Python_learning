#!/usr/bin/python
"""
A module allows you to logically organize yout Pyhon code. Grouping related code
into a module makes the code easier to understand and use. A module is a Python 
object with arbitrarily named attributes thay you can bind and reference.

Simply, a module is a file consisting of Python code. A module can define functions, 
classes and variable. A module can also include runnable code.
"""

"""
----------------------------------------------------------------------------------
The import Statement
You can use any Python source file as a module by execuing an import
statement in some other Python source file. The import has the following syntax:

    'import module1[, module2[,...moduleN]]'

When the interpreter encounters an import statement, it imports the module if the
module is present in the search path. A  search path is a list of directories that 
the interpreter searches before importing a module.
"""

print "\n-----------------------------------------"
import Support
Support.print_func("Zara")

"""
The 'from ... import' Statement

    Python's 'from' statement lets you import specific atributes from a module into

Syntax:
    from module_name import name1 [,name2 ,..., nameN]

For examble, to import the function fibonacci frm the module fib,
             use the following
"""
# from fib import fibonacci
"""
This statement dees not import the entire module fib into the current 
namespace; it just introduces the item fibonacci from the module fib into
the global symboy table of the importing module.
"""

"""
----------------------------------------------------------------------------------
The 'from... import *' Statement:
It is also posible to import all names from a module into the current
namespace by using the following import statement.
from module_name import *
"""

"""
----------------------------------------------------------------------------------
When you import a module, the Python interpreter searches for the module in the following sequences:
- The current directory
If the module isn't fount, Python then searches each directory in the shell variable $PYTHONPATH.
- If all else fails, Python checks the default path. On Unix, this default path is normally 
/usr/local/lib/python

The module search path is stored in the system module sys as the sys.path variable.
The sys,path variable contains the current directory, PYTHONPATH, and the installation-dependent default.
"""

"""
----------------------------------------------------------------------------------
Variables are names (identifiers) that map to objects. A namespace is a dictionary of variable names(keys)
and their corresponding objects(values).

A Python statement can access variables in a local namespace and in the global namespace. If a local and a 
global variable have the same name. the local variable shadows the  global variable.

Each function has sits own local namespace. Class methods follow the same scoping rule as ordinary functions.

Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned 
a value in a function is local.

Therefore, in order to assign a value to a global variable within a function, you must first use the 'global' statement

The statement 'global VarNam' tell Python that VarName is a global variable. Python stops searching the local namespace for
 the variable.
"""

Money = 2000

def AddMoney():
    #Uncomment the following line to fix the code.
    global Money
    Money = Money + 1

import math
def main():
    print "\n-----------------------------------------"
    print Money
    AddMoney()
    print Money
    

    print """
    ----------------------------------------------------------------------------------
    The 'dir()' Function
    The dir() build-in function returns a sorted list of strings containing the names defined
by a module.
    The listt contains the names of all the modules, variables and functions that are defined 
in a module. 
    """

    content = dir (math)
    print content

    print "==========="
    print dir(Support)





if __name__ == "__main__":
    main()
    

