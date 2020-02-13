# Find first and last digits of a number

############ METHOD 1 #################


def first_digit(num):
    # remove last digit from number until only one digit is left
    while num >= 10:
        # // operator is used for division that
        # results into whole number i.e. discard the remainder
        num = num // 10

    return num


def last_digit(num):
    return num % 10


num = 123456789
print(first_digit(num))  # 1
print(last_digit(num))  # 9

############ METHOD 2 #################


def first_digit_method2(num):
    # convert number to list of integers
    list_num = list(map(int, str(num)))

    # get initial index's value which will be first digit
    return list_num[0]


def last_digit_method2(num):
    # convert number to list of integers
    list_num = list(map(int, str(num)))

    # get last index's value which will be last digit
    return list_num[-1]


num = 123456789
print(first_digit_method2(num))  # 1
print(last_digit_method2(num))  # 9
