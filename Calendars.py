#!/usr/bin/python

"""
The Calendar Module:

The calendar module supplies calendar-related functions, including functions to print a text calendar for a given month or year.
By default, calendar takes Monday as the first day of the week and Sunday as the last one. To change this, 
call calendar.setfirstweekday() function

calendar.calendar(year, w=2,l=2,c=6)
    Returns a multiline string with a calendar for year year formatted into three columns separates by c spaces. W is the width 
    in characters of each date; each line has length 21*w+18+2*c. l is the number of lines fof each week.

calendar.firstweekday()
    Returns the current setting for the weekday that starts each week. By default, when calendar is first imported, this is 0, meaning Monday

calendar.leapday(y1,y2)
    Returns the total number of leap days in the year within range(y1,y2).append

calendar.month(year,month, w=2,l=1)
    Returns a multiline string with a calendar for month month of year year, one linee per week plus two header lines. w is the width in characters
    of each date; each line has length 7*w+6. l is the number of lines for each week.

calendar.monthcalendar(year,month,w=2,l=1)
    Returns a 
"""





print "=================================================="