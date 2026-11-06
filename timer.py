import time
import datetime

date = datetime.datetime.now()

def Timer():
    while True:
        start = input('Press Enter to start')
        if start != '':
            print('Please press Enter to start timer')
            continue
        break
    start_time = time.perf_counter()
    print('Timer Started')
    while True:
        end = input('Press Enter to stop')
        if end != '':
            print('Please press Enter to stop timer')
            continue
        break
    end_time = time.perf_counter()
    solve = end_time - start_time
    print(f'Solve time: {solve:.2f}s')
    return solve
        
def solve_holder_timer():
    full_solve = {
            'date': date,
            'cross': None,
            'f2l':None,
            'oll':None,
            'pll':None,
            'solve_time':Timer()
            }
    return full_solve

