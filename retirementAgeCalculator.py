import re


# convert month to calendar month
def getMonthCalendarName(monthNumericalVal):
    if monthNumericalVal == 0:
        monthNumericalVal = 1
    monthList = {1: "January",
                 2: "February",
                 3: "March",
                 4: "April",
                 5: "May",
                 6: "June",
                 7: "July",
                 8: "August",
                 9: "September",
                 10: "October",
                 11: "November",
                 12: "December"}
    return monthList[monthNumericalVal]


# convert total number of months to years
def convertToYears(totalMonths):
    remainingMonths = totalMonths % 12
    totalYears = totalMonths // 12
    print("Your full retirement age is", totalYears, "and", remainingMonths, "months")
    return totalYears, remainingMonths


# find the retirement date by finding total months and converting to years
def retirementDate(totalYears, totalMonths, birthYear, birthMonth):
    totalMonths += birthMonth
    totalYears += totalMonths // 12
    totalMonths = totalMonths % 12

    retirementYear = birthYear + totalYears
    print("this will be in", getMonthCalendarName(totalMonths), "of", retirementYear, "\n")


# find the total number of months to retirement then call retirementDate
def retirementCal(birthYear, birthMonth):
    retirementAge = 780  # base year 1937 converted to months

    if birthYear < 1900:
        print("Month or year invalid must be 1900 or later\n")
        return
    elif birthMonth > 12 or birthMonth < 1:
        print("Months are from labeled as number 1-12, 1 for January\n")
    elif birthYear <= 1937:
        retirementAge = 780

    else:
        year = 1937
        while (year != birthYear):
            if year >= 1943 and year < 1954:
                retirementAge += 0
            elif year >= 1960:
                retirementAge += 0
            else:
                retirementAge += 2

            year += 1
            # print(year)
    totalYears, totalMonths = convertToYears(retirementAge)

    retirementDate(totalYears, totalMonths, birthYear, birthMonth)


def main():
    answer = ' '
    while answer != '':
        year = None
        month = None

        print("Social Security Full Retirement Age Calculator")
        answer = input("Enter the year of birth or to exit: ")
        # must be 4 digit number
        if re.search("[0-9]{4}", answer) and len(answer) == 4:
            year = int(answer)
            month = int(input("Enter birth month: "))
            retirementCal(year, month)
        elif answer == '':
            break
        else:
            print("invalid input\n")


main()
