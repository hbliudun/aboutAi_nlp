daysOfMonthsNormal = [ 0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeapyear = [ 0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%4 != 0:
        return False
    elif year%100 !=0:
        return True
    elif year%400 !=0:
        return False
    else:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    year,month,day = year1,month1,day1
    retDays = 0
    while year <=year2 :
        for m in range(month,13):
            if isLeapYear(year):
                for i,days in enumerate(daysOfMonthsLeapyear):
                    if i != m:
                        continue
                    if(year == year1 and m == month1):
                        retDays = retDays +days - day
                        break
                    elif (year == year2 and m == month2):
                        retDays += day2
                        break
                    else:
                        retDays = retDays +days
                        break
            else:
                for i ,days in enumerate(daysOfMonthsNormal):
                    if i != m:
                        continue
                    if(year == year1 and m == month1):
                        retDays = retDays + days - day
                        break
                    elif (year == year2 and m == month2):
                        retDays += day2
                        break
                    else:
                        retDays = retDays + days
                        break
            if year == year2 and m ==month2:
                break
        year += 1
        month =1
    return retDays
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()