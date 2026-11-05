from average import average_calc

def pb(solves):
    if not solves:
        return None
    best = min(solves, key=lambda solve: solve['solve_time'])
    return best

def best_ao5(solves):
    if len(solves) < 5:
        return None
    solves = sorted(solves, key=lambda solve: solve['date'], reverse=True)
    best_average = average_calc(solves, 5)
    if best_average is None:
        return None
    for i in range(1, len(solves) - 5 + 1):
        window = solves[i:i + 5]
        current_average = average_calc(window, 5)
        if current_average is None:
            continue
        if current_average < best_average:
            best_average = current_average
    return best_average

def best_ao12(solves):
    if len(solves) < 12:
        return None
    solves = sorted(solves, key=lambda solve: solve['date'], reverse=True)
    best_average = average_calc(solves, 12)
    if best_average is None:
        return None
    for i in range(1, len(solves) - 12 + 1):
        window = solves[i:i + 12]
        current_average = average_calc(window, 12)
        if current_average is None:
            continue
        if current_average < best_average:
            best_average = current_average
    return best_average
