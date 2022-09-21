import json

with open("testt.json") as f:
    persons = json.load(f)
    for each in persons['persons']:
        executeValues = tuple(each.values())
        print(executeValues)