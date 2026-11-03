import enum


def display_history(solves):
    if len(solves) == 0:
        print('No solves recorded yet')
        return
    for index, solve in enumerate(solves, start=1):
        print(f"Solve #{index}\nCross time: {solve['cross']:.2f}s\nF2L time: {solve['f2l']:.2f}s\nOLL time: {solve['oll']:.2f}s\nPLL time: {solve['pll']:.2f}s\n")

solves= [{"cross":1.235, "f2l":3, "oll":2, "pll":2}]

display_history(solves)
