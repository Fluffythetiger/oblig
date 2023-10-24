def is_it_leap_year():
    pass


# leep year
def is_it_divisible_on_4(y):
    s = y%4 == 0
    return s

def not_divisible_on_100(y):
    s = y%100 == 0
    return s

def is_it_divisible_on_400(y):
    s = y%400 == 0
    return s

# not leap year
def is_it_not_divisible_4(y):
    s = y%4 == 0
    return s

def is_divisible_100(y):
    s = y%100 == 0
    return s

def not_divisible_on_400(y):
    s = y%400 == 0
    return s


def see_if_leepYear(y):
    if (y % 400 == 0):
        s = True
    elif (y % 4 == 0) and (y % 100 != 0):
        s = True
    else:
        s = False
    return s

def isLeapYear(year):
   s = see_if_leepYear(year)
   return s

print(isLeapYear(1800))
print(isLeapYear(18))
print(isLeapYear(100))
print(isLeapYear(0))
print(isLeapYear(40))