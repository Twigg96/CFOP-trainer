import datetime
from hmac import new
from logging import raiseExceptions
from operator import ne


def solve_holder():
    date = datetime.datetime.now()
    cross = float_validation("Enter cross time: ")
    f2l = float_validation("Enter f2l time: ")
    oll = float_validation("Enter oll time: ")
    pll = float_validation("Enter pll time: ")
    print(date.strftime("%Y-%m-%d %H:%M:%S"))
    full_solve = {
            'date': date,
            'cross': cross,
            'f2l':f2l,
            'oll':oll,
            'pll':pll,
            }

    return full_solve

def float_validation(prompt):
    while True:
        try:
            tmp = input(prompt)
            tmp = float(tmp)
        except ValueError:
            print('Please enter a valid number')
            continue

        if tmp <= 0:
            print('Cannot be a negative number or 0')

        return tmp

new_solve = solve_holder()
print(new_solve)

#print(new_solve['date'].strftime("%Y-%m-%d %H:%M:%S"))
