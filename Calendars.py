#!/usr/bin/python

print """
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
    Returns a multiline string with a calendar for month month of year year, one linee per week plus two header lines. 
    w is the width in characters of each date; each line has length 7*w+6. l is the number of lines for each week.

calendar.monthcalendar(year,month,w=2,l=1)
    Returns a list of list of ints. Each sublist denotes a week. Dys outside 'month' month of 'year' year are set to 0;
    days within the month are set to their day-of-month, 1 and up.

calendar.monthrange(year, month)
    Returns 2 integer. The first one is the code of the weekday for the first day of the 'month' month in 'year' year; 
    the second one is the number of days in the month. Weekday codes are 0 (Monday) to 6 (Sunday); month number are 1 to 12

calendar.prcal(year,w=2,l=1,c=6)
    Like print caldendar.calendar(year,w,l,c)

calendar.prmonth(year,mont,w=2,l=1)
    Like print clendar.month(year,month,w,l)

calendar.setfirstweekday(weekday)
    sets the first day of each week to weekday code weekday. Weekday code are 0 (Monday) to 6 (Sunday)

calendar.timegm(tupletime)
    The inverst of t time.gmtime: accepts a time instant in time-tuple from and return the sam instant
    as a floating-point number of seconds since the epoch

calendar.weekday(year,month,day)
    Returns the weekday code for the given date. Weekday codes are 0(Monday) to 6(Sunday); month numbers
    are 1 (January) to 12 (December)

"""
