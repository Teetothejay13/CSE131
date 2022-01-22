# 1. Name:
#      TJ Putnam
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      This program is meant to count the days since January 1st, 1753 until the month and year the user inputs, and display an
#      accurate calendar accordingly.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


# of course, main will run the show
def main():
    # first we need the year and month
    year = getYear()
    month = getMonth()
    # now we need to call offset, which will handle the calculations
    offset = computeOffset(month, year)
    monthDays = daysInMonth(month, year)
    # and finally, we display the calendar
    print(offset, monthDays)
    display(monthDays, offset)

# next is a function to get the year from the user
def getYear():
    # of course we want to confirm an acceptable year
    acceptableYear = False
    while acceptableYear == False:
        year = int(input("Enter year: "))
        if year >= 1753:
            acceptableYear = True
        elif year < 1753:
            print("Year must be a positive number greater than or equal to 1753.")
    return year

# we want to do the same for the month
def getMonth():
    # confirming acceptable months is important
    acceptableMonth = False
    while acceptableMonth == False:
        month = int(input("Enter month: "))
        if month <= 12 and month >= 1:
            acceptableMonth = True
        else:
            print("Month must be a positive number from 1 to 12.")
    return month

# now we need to take month and year and calculate what we need to display
def computeOffset(month, year):
    offset = 0
    # now we can see how many days have happened
    num_days = 0
    # first for the years in between
    for year_count in range(1753, year):
        num_days += daysInYear(year_count)
    # then for the months in the final year
    for month_count in range(1, month):
        monthDays = daysInMonth(month_count, year)
        num_days += monthDays
    # now that we have the total days, we need to return the offset and the days in current month
    offset = ((num_days + 1) % 7)
    return offset

# we need a function to take year and check if it is a leap year
def isLeapYear(year):
    # some weird logic, but it works
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        leapYear = True
    else:
        leapYear = False
    # either way, we return a boolean
    return leapYear

# we also need a function to compute how many days are in the year
def daysInYear(year):
    # first we need to check if the year we are on is a leap year
    leapYear = isLeapYear(year)
    # if it is, we return 366 days
    if leapYear:
        return 366
    # if not...
    else:
        return 365

# also also, we need days in the final year up until the final month
def daysInMonth(month, year):
    # if the month is anything but Febraury, we don't need to worry about leap days
    # just returning 31 for some months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # and returning 30 for other months
    elif month in [4, 6, 9, 11]:
        return 30
    # we only need to check the leap year if it is February
    elif month == 2:
        # so let's check
        leapYear = isLeapYear(year)
        # if it's a leap year, we return 29
        if leapYear:
            return 29
        # otherwise...
        else:
            return 28

# lastly, a display function
def display(num_days, offset):
    # this will mostly just be a matter of formatting
    # we can make a string and concatenate each day onto it
    days = "  Su  Mo  Tu  We  Th  Fr  Sa\n"
    for i in range(num_days + offset + 1):
        # first we need the offset
        if (i <= offset) and (offset != 0):
            # but if it's the end of the column, we need to do a newline character
            if (i - 1) % 7 != 0:
                days += "    "
            else:
                days += "\n    "
        # if offset is 0, we need to skip the first loop and only the first loop
        elif offset == 0 and i == 0:
            continue
        # if we're done with offset, we can do the days as normal
        else:
            # but we still need to check the end of the column
            if i % 7 != 0:
                # and we also need to check if it's a single digit or double digit
                if (i - offset) < 10:
                    days += f"   {i - offset}"
                else:
                    days += f"  {i - offset}"
            # gotta remember that newline character
            else:
                # and repeat the logic for single vs double digits
                if (i - offset) < 10:
                    days += f"   {i - offset}\n"
                else:
                    days += f"  {i - offset}\n"
    # now we finally print
    print(days)

# okay legitimate last thing, this makes it run automatically
if __name__ == "__main__":
  main()