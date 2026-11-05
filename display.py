import enum
from inputs import date


def display_history(solves):
    if len(solves) == 0:
        print('No solves recorded yet')
        return
    for index, solve in enumerate(sorted(solves, key=lambda solve: solve['date'], reverse=True), start=1):
        print(f"Solve #{index}\nDate and time: {solve['date'].strftime('%b %d %Y %H:%M')}\nCross time: {solve['cross']:.2f}s\nF2L time: {solve['f2l']:.2f}s\nOLL time: {solve['oll']:.2f}s\nPLL time: {solve['pll']:.2f}s\nSolve Time: {solve['solve_time']:.2f}s")

