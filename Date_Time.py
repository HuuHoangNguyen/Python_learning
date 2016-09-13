#!/usr/bin/python
"""
=========================================================================================================================
A Python program can handle date and time in several ways. Converting between date format is a common chore for computers.
Python's time and calendar modules help track dates and times

What is Tick?
Time intervals are floating numbers in units of seconds. Particular instants in time are 
expressed in seconds since 12:00am, January 1, 1997(epoch)

There is a popular time module availabel in Python which provides fuctions for working
with times, and for converting between representation. The function time.time() 
returns the currrent system time in ticks sine 12:00am, January 1, 1970(epoch)
"""

import time     #This is required to include time module
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970 : ", ticks

"""
=========================================================================================================================
Date arithmetic is easy to do with ticks. However, dates before the epoch cannot be represented in this format
Dates in the far future also cannot be represented this way - the cutoff point is sometime is 2038 for UNX and Windows

What is TimeTuple?
Index         Field                             Values
 0          4-digit year                        2008
 1          Month                               1 to 12
 2          Day                                 1 to 31
 3          Hour                                0 to 23
 4          Minute                              0 to 59
 5          Second                              0 to 61(60 or 61 are leap seconds)
 6          Day of Week                         0 to 6(0 is Monday)
 7          Day of Year                         1 to 266 (Julian day)
 8          Daylight savings                    -1, 0, 1; -1 means library determines DST 
 """

"""
=========================================================================================================================
The above tuple  is equivalent to struct_time structure. This structure has following attributes

Index         Field                             Values
 0          tm_year                             2008
 1          tm_mon                              1 to 12
 2          tm_mday                             1 to 31
 3          tm_hour                             0 to 23
 4          tm_min                              0 to 59
 5          tm_sec                              0 to 61(60 or 61 are leap seconds)
 6          tm_wday                             0 to 6(0 is Monday)
 7          tm_ydate                            1 to 266 (Julian day)
 8          tm_isdst                            -1, 0, 1; -1 means library determines DST
 ========================================================================================================================= 
"""

print "=================================================="
print "Getting current time"
print "To translate a time instant from a seconds sice the epoch floating-point value into a time-tuple"
print "pass the floating-point value to a function(e.g, localtime) that returns a time-tuple with all "
print "nine items valid"
print "----------"
localtime = time.localtime(time.time())
print "Local current time:", localtime 

print "=================================================="
print "Getting formatted time"
print "You can format any time as per your requirement, but simple method to get time in readable formar in asctime()"
print "----------"
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time: %s" %localtime

print "=================================================="
print "Getting calendar for a month"
print "The calendar module gives a wide range of methods to play with yearly and monthly calendars."
print "Here , we print a calendart for a given month(Jan 2008)"
print "----------"
import calendar
cal = calendar.month(2008, 1)
print "Here is the calendar: \n\n", cal

print "=================================================="
print "THE TIME MODULE"
print "This is a popular time module available in Python which provides functions for working"
print "with times and for converting between representations. Here is the list of all available methods"

print "=================================================="
print """time.altzone: The offset of the local DST timezone, in second west of UTC, if one defined. This is
negative if the local DST timezone is east of UTC(as in Western Europe, including the UK). Only use this if daylight is nonzero
"""
print "----------"
print "The time.altzone %d " % time.altzone

print "=================================================="
print "time.asctime([tupletime]): Accepts a time-tuple and returns a readable 24 character string as 'Mon Sep 12 16:22:39 2016'"
t = time.localtime()
print "time.asctime(t): %s " %time.asctime(t)

print "=================================================="
print "time.clock(): Returns the current CPU time as a floating-point number of seconds. To measure computational costs of "
print "different approaches, the value of time.clock is more useful than that of time.time()."
print "----------"
def procedure_q():
    time.sleep(2.5)
#measure process time
t0 = time.clock()
procedure_q()
print time.clock() - t0, "second proces time"

#measure wall time
t0 = time.time()
procedure_q()
print time.time() - t0, "seconds wall time"

print "=================================================="
print "time.ctime([secs]): Like asctime(localtome(secs)) and without arguments is like asctime()"
print "----------"
print "time.ctime(): %s " % time.ctime()

print "=================================================="
print "time.gmtime([secs]): Accepts and instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note ttm_isdst is always 0"
print "----------"
print "time.gmtime() : %s " %time.gmtime()

print "=================================================="
print "time.localtime([secs]): Accepts an instant expressed in seconds since the epoch and returns a time-tuple t"
print " with the local time(t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules)"
print "----------"
print "time.localtime(): %s " % time.localtime()

print "=================================================="
print """time.mktime(tupletime): Accepts an instant expressed as a time-tuple in local time and returns a floating-point value 
wirh the instant expressed in seconds since the epoch 
"""
print "----------"
t = (2016, 9 , 12, 16, 55, 30, 0, 256, 0)
secs = time.mktime(t)
print "time.mktime(t) : %f " %secs
print "asctime(localtime(secs)): %s " %time.asctime(time.localtime(secs))

print "=================================================="
print "timesleep(secs): Suspends the calling thread for secs seconds"
print "Start: %s " %time.ctime()
time.sleep(5)
print "End: %s" % time.ctime()

print "=================================================="
print """time.strftime(ftm[,tupletime]): Converts a tuple or struct_time representing a time as returned 
by gmtime() or localtime() to a string as specified by the formt argument.
"""

"""
Parameters
    t       : This is the time in number of seconfs to be formatted.
    format  : This is the directive which would be used  to format given time
                The following directives can be embedded in the format string

Directive:
    %a  : abbreviated weekday name 
    %A  : full weekday name 
    %b  : abbreviated month name 
    %B  : Full month name 
    %c  : Preferred date and time representation
    %C  : Century number (the year divided by 100, range 00 to 99)
    %d  : day of the month (01 to 31)
    %D  : same as %m/%d/%y 
    %e  : date of the month (1 to 31)
    %g  : like %G, but without the century
    %G  : 4 digit year corresponding to the ISO week number (see %V).
    %h  : same as %b 
    %H  : hour, using a 24-hour clock (00 to 23)
    %I  : hour, using a 12-hour clock (01 to 12)
    %j  : day of the year (001 t0 366)
    %m  : month (01 to 12)
    %n  : newline character
    %p  : either am or pm accorfing to the given time value  
    %r  : time in a.m or p.m notation
    %R  : Time in 24hours natation
    %S  : Second
    %t  : tab character
    %T  : current time, equal to %H:%M:%S    
    %u  : weekday as a number (1 to 7), Monday=1. Warning: Im Sin Solaris Sunday=1
    %U  : week number of the current year, starting with the first Sunfday as 
          the first day of the first week
    %V  : The ISO 8601 week number of the current year(01 to 53), whwere week 1 is the first week that 
          has at least 4 days in the current year, and with Monday as the first day of the week
    %W  : week number the current year, starting with the first Mondat ad the first day of the first week
    %w  : day of the week as a decimal. Sunday=0
    %x  : Preferred date representation without the time
    %X  : Preferred time representation without the date
    %y  : year without a century (range 00 to 99)
    %Y  : year includeing the century
    %Z or
    %z  : time zone or name or abbreviation
    %%  : a literal % character

Return Value:
    This method does not return any value
"""

print "----------"
t = t = (2016, 9 , 12, 16, 55, 30, 0, 256, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

print "=================================================="
print """time.strptime(str, fmt='%a %b %d %H:%M:%S %Y'): Parses str accoding to format string 
fmt and returns the instant in time-tuple format 
"""
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "Return tuple: %s " % struct_time

print "=================================================="
print "=================================================="
print "=================================================="






