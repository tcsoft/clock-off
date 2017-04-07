#############################################################################
##                                                                         ##
##  clock-off.py                                                           ##
##  Copyright (c)2017 - Tim Clark - TC Soft Consulting Limited             ##
##  Issued under an MIT license                                            ##
##                                                                         ##
#############################################################################
##                                                                         ##
##  For use with:                                                          ##
##  - Raspberry Pi Zero or Rapsberry Pi Zero W                             ##
##  - Python 3.x                                                           ##
##  - Four Letter pHAT - from Pimoroni                                     ##
##  - https://github.com/pimoroni/fourletter-phat                          ##
##                                                                         ##
#############################################################################
##                                                                         ##
##  Clock routine taken from Pimoroni samples                              ##
##  Time checking code from StackOverflow                                  ##
##  - http://stackoverflow.com/a/41824605                                  ##
##  - Thanks to - http://stackoverflow.com/users/4004188/maulik-gangani    ##
##                                                                         ##
#############################################################################
##                                                                         ##
##  Version 0.1 07-Apr-17                                                  ##
##                                                                         ##
#############################################################################


#!/usr/bin/env python

#############################################################################
##  Import the various libraries needed                                    ##
#############################################################################
##  time - for the functions around calculating if between two times       ##
##  fourletterphat - to address the Four Letter pHAT from Pimoroni         ##
##  datetime - to enable us to get the system date/time and use it         ##
#############################################################################
import time
import fourletterphat as flp
from datetime import datetime
from datetime import date

#############################################################################
##  Main code block. This has to be in a while loop or it will stop at the ##
##  end of the first loop and not continue.                                ##
#############################################################################
while True:
#############################################################################
##  Returns correct calculation if the time spans midnight                 ##
#############################################################################
    def isNowInTimePeriod(startTime, endTime, nowTime):
        if startTime < endTime:
            return nowTime >= startTime and nowTime <= endTime
        else: #Over midnight
            return nowTime >= startTime or nowTime <= endTime
#############################################################################
##  Returns daynum to calculate if a weekend or not. 0=Monday - 6=Sunday   ##
##  <5 = Mon-Fri and therefore a weekday                                   ##
##  In my application I want the clock to come on later at a weekend       ##
##                                                                         ##
##  timeStart is the time the clock should first be visible (24hr clock)   ##
#############################################################################
    daynum = date.today().weekday()
    if daynum < 5:
        timeStart = '06:30'
    else:
        timeStart = '07:30'
#############################################################################
##  Here is where the end time (bedtime) is set (timeEnd)                  ##
#############################################################################
    timeEnd = '19:50'
#############################################################################
##  timeNow is the 24hr clock from the current system time                 ##
#############################################################################
    timeNow = time.strftime("%H:%M")
#############################################################################
##  These times are now formated correctly for the 24hr clock              ##
#############################################################################
    timeEnd = datetime.strptime(timeEnd, "%H:%M")
    timeStart = datetime.strptime(timeStart, "%H:%M")
    timeNow = datetime.strptime(timeNow, "%H:%M")

#############################################################################
##  In the Pimoroni code this is a while True: block. I had to change this ##
##  to make sure that it didn't just drop out of the end of the while      ##
##  if it got to a false condition. Also to make it check back to test the ##
##  validity of showing the time or not.                                   ##
#############################################################################
##  The rest of this block is the code from Pimoroni's clock.py sample     ##
#############################################################################
    if isNowInTimePeriod(timeStart, timeEnd, timeNow) == True:
        flp.clear()
        str_time = time.strftime("%H%M")
        flp.print_number_str(str_time)
        if int(time.time()) % 2 == 0:
            flp.set_decimal(1, 1)
        else:
            flp.set_decimal(1, 0)
        flp.show()
        time.sleep(0.1)
    else:
        flp.clear()
        flp.show()
#########################################################################################
##  By rights, you should never get to this code, but it will tell you if you do! ;o)  ##
#########################################################################################
else:
    print('Error occured in time')
