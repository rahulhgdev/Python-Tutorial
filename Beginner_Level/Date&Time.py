import time;
import calendar;

localtime = time.localtime(time.time())
print("Local current time :", localtime)
print('\n')

#Getting formatted time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
print('\n')

#Getting calendar for a month

cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)