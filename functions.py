#import sqlite3
import json
import Team3

def load_file():
    with open("jsonpersons.json") as f:
        json_persons = json.load(f)
        mydudes = []
        for p in json_persons['persons']:
            mydudes.append(Team3.Person(p['firstname'], p['lastname'], p['birth'], p['adress']))
            Team3.sql_connection.execute(Team3.INSERT_DATA, tuple(p.values()))
    print("---------------------DUDES INC--------------------")
    print(mydudes)
    print("---------------------DUDES OUT--------------------")

    