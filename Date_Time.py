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






