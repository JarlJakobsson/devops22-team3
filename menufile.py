import json
import sqlite3




class Menu:
    menu_text = """

    1. Load data from file
    2. Print persons from database
    3. Delete person
    4. Update address
    5. Add a hobby
    
    type q or Q to exit
    """

    def user_choice(self):
        return input("Enter your choice: ")

    def wait_for_user(self):
        if self.running:
            input("Please press any key to continues.")

    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.menu_text)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()

    def menu_commands(self, choice):
        printbool = False
        if choice == "q" or choice == "Q":
            self.running = False

        elif choice == "1":
            printbool = True
            with open("jsonpersons.json") as f:
                json_persons = json.load(f)
                person_list = []
                for p in json_persons["persons"]:
                    person_list.append(Person(p["firstname"], p["lastname"], p["birth"], p["address"]))
                    sql_connection.execute(INSERT_DATA, tuple(p.values()))
            print("*** DATABASE LOADED ***")

        ### SECOND MENU START ###
        elif choice == "2":
            print(
                """

    What do you want to print for

    1. Firstname
    2. Lastname
    3. Birthyear
    4. Address
    5. Print all
    6. Print all persons with a hobby
    
    type q or Q to return to mainmenu
    """
            )

            print_choice = input("Enter choice: ")
            if print_choice == "q" or choice == "Q":
                print("*** Returning to mainmenu ***")

            elif print_choice == "1":
                list_all()
                firstname_input = input("Enter the first name: ").lower()
                cursor = sql_connection.cursor()
                cursor.execute(
                    f'SELECT * FROM person WHERE firstname = "{firstname_input}"'
                )
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)

            elif print_choice == "2":
                list_all()
                lastname_input = input("Enter the last name: ").lower()
                cursor = sql_connection.cursor()
                cursor.execute(
                    f'SELECT * FROM person WHERE lastname = "{lastname_input}"'
                )
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)

            elif print_choice == "3":
                list_all()
                birth_input = int(
                    input("Enter the birthyear of the person you want to printout: ")
                )
                cursor = sql_connection.cursor()
                cursor.execute(f'SELECT * FROM person WHERE birth = "{birth_input}"')
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)

            elif print_choice == "4":
                list_all()
                address_input = input("Enter the address of the person: ").lower()
                cursor = sql_connection.cursor()
                cursor.execute(
                    f'SELECT * FROM person WHERE address = "{address_input}"'
                )
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)
                input("Press any key to continue... ")

            elif print_choice == "5":
                try:
                    if printbool == False:
                        print("Nothing to print")
                    else:
                        print("*** HERE IS ALL DATA ***")
                        list_all()
                except:
                    print("Nothing to print")
            
            elif print_choice == "6":
                try:
                    cursor = sql_connection.cursor()
                    cursor.execute('''SELECT firstname, hobbyname 
                                    FROM person AS p 
                                    INNER JOIN hobby AS h 
                                    ON p.id = h.personid
                                    ORDER BY firstname
                    ''')
                    sql_data = cursor.fetchall()
                    for e in sql_data:
                        print(e)
                except:
                    except_msg()

                ### SECOND MENU END ###

        elif choice == "3":
            try:
                list_all()
                userinput = input("\nWho do you want to delete? Enter ID: ")
                sql_connection.execute(f"DELETE FROM person WHERE id = '{userinput}'")
                print(f"Person {userinput} has been deleted")
            except:
                except_msg()

        elif choice == "4":
            try:
                list_all()
                userinput = input("\nWhos address do you want to Update? Enter ID: ")
                sql_connection.execute(f"SELECT * FROM person WHERE id = '{userinput}'")
                new_adress = input("\nEnter the new address: ")
                sql_connection.execute(f"UPDATE person SET address = '{new_adress}' WHERE id = '{userinput}'")
            except:
                except_msg()
        
        elif choice == "5":
            list_all()
            try:
                userid = int(input("Enter ID of person to add hobby: "))
                input_hobby = input("Enter the name of the hobby: ")
                sql_connection.execute(INSERT_HOBBY, (userid, input_hobby))
                list_hobbies()
            except:
                except_msg()

class Person:
    def __init__(self, firstname, lastname, birthyear, address):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address

    def add_hobby(self, hobbyname):
        self.hobby = hobbyname

    def __str__(self):
        return self.lastname

    def __repr__(self) -> str:
        return self.firstname

CREATE_TABLE_PERSON = """
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birth INTEGER,
                    address TEXT
                )
                """

CREATE_TABLE_HOBBIES = '''
            CREATE TABLE IF NOT EXISTS hobby(
                hobbyid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                personid INTEGER NOT NULL,
                hobbyname   TEXT NOT NULL,
            FOREIGN KEY(personid) REFERENCES person(id)
            )'''

INSERT_DATA = """
            INSERT INTO person(
                firstname,
                lastname,
                birth,
                address
            )
            VALUES (?, ?, ?, ?)
            """

INSERT_HOBBY = """
            INSERT INTO hobby(
                personid,
                hobbyname
            )
            VALUES (?, ?)
            """

with sqlite3.connect(":memory:", isolation_level=None) as sql_connection:
    sql_connection.execute(CREATE_TABLE_PERSON)
    sql_connection.execute(CREATE_TABLE_HOBBIES)

def list_all():
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM person")
    sql_data = cursor.fetchall()
    for e in sql_data:
        if bool(e) == True:
            print("Database empty")
        else:
            print(e)

def list_hobbies():
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM hobby")
    sql_data = cursor.fetchall()
    for e in sql_data:
        print(e)

def except_msg():
    print("Something went wrong.")

Menu().start_loop()

# SELECT ArtistName, AlbumName 
# FROM Artists AS a 
#   INNER JOIN Albums AS b 
#   ON a.ArtistId = b.ArtistId
# ORDER BY ArtistName;

# SELECT firstname, hobbyname 
# FROM person AS p 
#   INNER JOIN hobby AS h 
#   ON a.id = b.id
# ORDER BY firstname