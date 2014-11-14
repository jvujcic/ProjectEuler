import calendar

print len([day for day in [calendar.weekday(year,month,1)
                           for year in xrange(1901, 2001)
                           for month in xrange(1,13)]
           if day == 6])
