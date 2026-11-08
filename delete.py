import datetime, json

def delete_solves(solves):
    if len(solves) == 0:
        return
    for index, solve in enumerate(sorted(solves, key=lambda solve: solve['date'], reverse=True), start=1):
        print(f'#{index}      Time:{solve["solve_time"]:.2f}s')
    while True:
        try:
            sorted_list = sorted(solves, key=lambda solve: solve['date'], reverse=True)
            choice = int(input("Choose a Solve Number to Delete"))
            if 1 <= choice <= len(solves):
                selected_solve = sorted_list[choice - 1]
                print(f"Delete {selected_solve['date']} {selected_solve['solve_time']}?\n")
                confirmation = input('y/n\n')
                if confirmation.lower() == 'y':
                    sorted_list.remove(selected_solve)
                    solves.remove(selected_solve)
                    with open("solves.json", 'w') as file:
                        json.dump(solves, file, indent=4, default=datetime.datetime.isoformat)
                    break
                elif confirmation.lower() == 'n':
                    break
                else:
                    print('Please enter y/n\n')
                    continue
            else:
                print('Enter a valid Solve Number\n')
                continue
        except ValueError:
                print('Enter a valid Solve Number\n')
                continue
            
