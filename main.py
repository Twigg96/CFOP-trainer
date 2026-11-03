from inputs import full_time, solve_holder

solves = []

def main():
    while True:
        choice = input('1. Add solve Time\n2. View solve history\n3. Exit\n')
        if choice == '1':
            new_solve = solve_holder()
            full_time(new_solve)
            solves.append(new_solve)
            print('Solve added\n')
        elif choice == '2':
            print(solves)
        elif choice == '3':
            break
        else:
            print('Enter a valid option: 1, 2, or 3\n')
            continue

if __name__ == '__main__':
    main()
