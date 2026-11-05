import json
import datetime

date = datetime.datetime.now()
date_string = date.isoformat()

solves = [
        {
            "date":date_string,
            "cross":2.45,
            "f2l":8.32,
            'oll':1.15,
            'pll':1.42,
            'solve_time':13.34
            }
        ]

with open("solves.json", 'w') as file:
    json.dump(solves, file, indent=4)

with open('solves.json', 'r') as file:
    loaded_solves = json.load(file)

print(loaded_solves)
for solve in loaded_solves:
    solve['date'] = datetime.datetime.fromisoformat(solve['date'])
