def leap_year(year: int) -> bool:
    """
    Function checking if the provided year is leap
    :param year: Numeric value for the year. Integer required.
    :return: Boolean value: True if the year is a leap year, False if it is not.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days_in_month(year: int, month_number: int) -> int:
    """
    Function to check the number of days in a given year.
    Considers if the year is leap and adjusts number of days in February of the leap yer.
    :param year: Numeric value for the year. Integer required.
    :param month_number: Numeric value for the month. Integer required.
    :return: Number of days in specified month of the given year.
    """
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Condition if the year is leap and month is February
    if leap_year(year) and month_number == 2:
        return 29
    # All other cases
    else:
        return months[month_number - 1]


try:
    check_year = int(input('Which year do you want to check?\n'))
    check_month = int(input('Which month are you going to check? 01... 12\n'))

    # Check if month number within 1...12 range
    if 1 >= check_month >= 12:
        print('Please provide correct number for the month')
    else:
        print(f'{check_month:02d}.{check_year} has {days_in_month(check_year, check_month)} days')
except ValueError:
    print('Please provide valid integer values for year and month.')
