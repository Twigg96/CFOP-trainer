def average_calc(solves, count):
    if len(solves) < count:
        return None
    solves = sorted(solves, key=lambda solve: solve['date'], reverse=True)
    shortened_list = solves[:count]
    times = sorted(shortened_list, key=lambda solve: solve['solve_time'])
    sorted_times = times[1:-1]
    total = 0
    for time in sorted_times:
        total += time['solve_time']
    average = total / len(sorted_times)
    return average
