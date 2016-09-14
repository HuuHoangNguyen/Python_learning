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



def main():
    print "-----------------------------------------\n"
    myprint("I'm first call to user defined function!")
    myprint("Agaim second call to the same functions")

    print "-----------------------------------------\n"
    mylist = [10, 20, 30]
    mychange(mylist)    
    

if __name__ == "__main__":
    main()
