from average import average_calc


def display_history(solves):
    if len(solves) == 0:
        print('No solves recorded yet')
        return
    for index, solve in enumerate(sorted(solves, key=lambda solve: solve['date'], reverse=True), start=1):
        if solve['cross'] != None:
            print(f"Solve #{index}\nDate and time: {solve['date'].strftime('%b %d %Y %H:%M')}\nCross time: {solve['cross']:.2f}s\nF2L time: {solve['f2l']:.2f}s\nOLL time: {solve['oll']:.2f}s\nPLL time: {solve['pll']:.2f}s\nSolve Time: {solve['solve_time']:.2f}s")
        else:
            print(f"Solve #{index}\nDate and time: {solve['date'].strftime('%b %d %Y %H:%M')}\nSolve Time: {solve['solve_time']:.2f}s")

    
    ao5 = average_calc(solves, 5)
    if ao5 is None:
        print('Ao5 : ...')
    else:
        print(f'Ao5: {ao5:.2f}s')
    ao12 = average_calc(solves, 12)
    if ao12 is None:
        print('Ao12 : ...')
    else:
        print(f'Ao12: {ao12:.2f}s')

