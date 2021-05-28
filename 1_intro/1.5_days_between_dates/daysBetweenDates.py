# # Days Between Dates
# This lesson will focus on one problem: calculating the number of days between two dates.
# This workspace is yours to use in whatever way is helpful. You might want to keep it open in a second tab as you go through the videos.

# pseudocode (lecture 17):
# days = 0
# while date1 is before date2:
#     date1 = day after date1
#     days += 1
# return days
#
# aka:
# input verification
# days = 0
# while dateIsBefore():
#     date1 = nextDate()
#     days += 1
# return days

# steps:
# 1. define simple nextDate() assuming all months have 30 days
# 2. define dateIsBefore()
# 3. define daysBetweenDates() v1.0
# 4. add input validation using assert
# 5. define daysInMonth() without leap years
# 6. refactor nextDate() to show almost accurate month lengths (w/out leap years)
# 7. define isLeapYear()
# 8. refactor daysInMonth() with leap years
# 9. this should result in the final version of daysBetweenDates()
# keep testing at each step!

# script:

def dateIsBefore (year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    return False

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def daysInMonth(year, month, day):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2 and isLeapYear(year):
        return 29
    elif month == 2 and isLeapYear(year) == False:
        return 28

def nextDate(year, month, day):
    if day < daysInMonth(year, month, day):
        return year, month, day + 1
    elif day == daysInMonth(year, month, day) and month < 12:
        return year, month + 1, 1
    else: #new year's day
        return year + 1, 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # input validation
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    # onto the main program
    days = 0
    while dateIsBefore (year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDate(year1, month1, day1)
        days += 1
    return days


# test 1:

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,24,2013,6,29),156),
                  ((1912,12,12,2012,12,12),36525)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed,", "your answer:", result, ", correct answer:", answer)
        else:
            print ("Test case passed!")

test()


# test 2:

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

testDaysBetweenDates()
