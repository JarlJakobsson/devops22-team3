import json
from lib2to3.pgen2.token import NEWLINE
import sqlite3
from Rawdata import persons

# with open(input("Enter path: "), 'x') as f:
#     f.write(json.dumps(persons, indent=10))

# with open(input("Enter Path: "), "r") as f:
#     person_list = []
#     person = json.load(f)
#     for each in person['persons']:
#         person_list.append(tuple(person.values()))

class Person():
    def __init__(self, firstname, lastname, birthyear, address):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address

    def __str__(self):
        return "hej"
    
    def __repr__(self) -> str:
        return self.firstname

# with open(input("Enter path: "), 'x') as f:
#      f.write(json.dumps(persons, indent=10))

CREATE_TABLE_PERSON = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birthyear INTEGER,
                    address TEXT
                )
                '''

INSERT_DATA = '''
            INSERT INTO person(
                firstname,
                lastname,
                birthyear,
                address
            )
            VALUES (?, ?, ?, ?)
            '''

#memory = name of database
with sqlite3.connect(':memory:', isolation_level=None) as sql_connection:
    sql_connection.execute(CREATE_TABLE_PERSON)
#'databas.db'

#userinput what file to read and create a DB of
with open("testt.json") as f:
    mydudes = []
    json_persons = json.load(f)
    for p in json_persons['persons']:
        mydudes.append(Person(p['firstname'], p['lastname'], p['year_of_birth'], p['adress']))
        sql_connection.execute(INSERT_DATA, tuple(p.values()))

print("---------------------DUDES INC--------------------")
print(mydudes)
print("---------------------DUDES OUT--------------------")

cursor = sql_connection.cursor()
cursor.execute('SELECT * FROM person')
sql_data = cursor.fetchall()
for e in sql_data:
    print(e)

sql_connection.close()
