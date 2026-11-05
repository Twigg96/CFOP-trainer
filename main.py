from personal_bests import best_ao5, best_ao12, pb
from inputs import full_time, solve_holder
from display import display_history
import json, datetime


try:
    with open('solves.json', 'r') as file:
        solves = json.load(file)
except FileNotFoundError:
    with open("solves.json", 'w') as file:
        solves = []
        json.dump(solves, file, indent=4, default=datetime.datetime.isoformat)
except json.JSONDecodeError:
    with open("solves.json", 'w') as file:
        solves = []
        json.dump(solves, file, indent=4, default=datetime.datetime.isoformat)


for solve in solves:
    solve['date'] = datetime.datetime.fromisoformat(solve['date'])

personal_best = pb(solves)
personal_ao5 = best_ao5(solves)
personal_ao12 = best_ao12(solves)

def main():
    while True:
        if personal_best is None:
            print('PB: ...')
        else:
            print(f"PB: {personal_best['solve_time']:.2f}s")
        if personal_ao5 is None:
            print('Best Ao5: ...')
        else:
            print(f"Best Ao5: {personal_ao5:.2f}s")
        if personal_ao12 is None:
            print('Best Ao12: ...')
        else:
            print(f"Best Ao12: {personal_ao12:.2f}s")
        choice = input('1. Add solve Time\n2. View solve history\n3. Exit\n')
        if choice == '1':
            new_solve = solve_holder()
            full_time(new_solve)
            solves.append(new_solve)
            with open("solves.json", 'w') as file:
                json.dump(solves, file, indent=4, default=datetime.datetime.isoformat)
            print('Solve added\n')
        elif choice == '2':
            if len(solves) == 0:
                print('There are no solves yet')
                continue
            display_history(solves)
        elif choice == '3':
            print('Thanks for using the solve tracker\n')
            break
        else:
            print('Enter a valid option: 1, 2, or 3\n')
            continue

if __name__ == '__main__':
    main()
