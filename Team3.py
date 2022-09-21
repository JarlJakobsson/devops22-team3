#import json
import sqlite3
#from Rawdata import persons
import menufile
#import functions

# try:
#     with open(input("Enter path: "), 'x') as f:
#         f.write(json.dumps(persons, indent=4))

# except: 
#     print("File already exist.")

class Person():
    def __init__(self, firstname, lastname, birthyear, address):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address

    def __str__(self):
        return self.lastname
    
    def __repr__(self) -> str:
         return self.firstname

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
def start_loop():
        running = True
        while running:
            print(menufile.Menu().meny_text)
            choice = menufile.Menu().user_choice()
            menufile.Menu().menu_commands(choice)
            menufile.Menu().wait_for_user()
start_loop()

#ÄNDRA memory = name of database
with sqlite3.connect(':memory:', isolation_level=None) as sql_connection:
    sql_connection.execute(CREATE_TABLE_PERSON)



#'databas.db'

#ÄNDRA userinput what file to read and create a DB of
# with open("jsonpersons.json") as f:
#     json_persons = json.load(f)
#     mydudes = []
#     for p in functions.['persons']:
#         mydudes.append(Person(p['firstname'], p['lastname'], p['birth'], p['adress']))
#         sql_connection.execute(INSERT_DATA, tuple(p.values()))

# print("---------------------DUDES INC--------------------")
# print(mydudes)
# print("---------------------DUDES OUT--------------------")

def list_all():
    cursor = sql_connection.cursor()
    cursor.execute('SELECT * FROM person')
    sql_data = cursor.fetchall()
    for e in sql_data:
        print(e)

sql_connection.close()
