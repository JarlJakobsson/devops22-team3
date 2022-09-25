import json
import sqlite3
import hidden
import Rawdata

# Importing json, sqlite3, our "hidden" module and our Rawdata module

# variable to keep loop running
running = True
# Empty list, preparing for our person objects
person_list = []

# Function to help the user read from the terminal before new menu text
def wait_for_user():
    input("\nPlease press any key to continues.")


# function to start our menu loop
def start_loop():
    while running:
        print(hidden.menu_text)
        choice = input("\nEnter your choice: ")
        menu_commands(choice)
        wait_for_user()


def menu_commands(choice):

    # CREATING CURSOR TO OUR SQL CONNECTION
    cursor = sql_connection.cursor()

    if choice == "q" or choice == "Q":
        return running == False

    elif choice == "1":
        try:
            ## ändra till input
            with open("jsonpersons.json") as f:
                json_persons = json.load(f)
                for d in json_persons["persons"]:
                    ## p will be a dict with first:value, last:value, birthyear: value, address: value.
                    ## we will then only take the values by doing p.values and add them as values
                    ##  to our database with the INSERT_PERSON_DATA function we have created in hidden
                    sql_connection.execute(hidden.INSERT_PERSON_DATA, tuple(d.values()))
                update_personlist()
            print("\n*** DATABASE LOADED ***\n")
        except:
            except_msg()

    ### SECOND MENU START ###
    elif choice == "2":
        print(hidden.menu2_text)

        print_choice = input("\nEnter choice: ")
        if print_choice == "q" or choice == "Q":
            print("\n*** Returning to mainmenu ***\n")

        elif print_choice == "1":
            try:
                list_all()
                query_print("firstname")
            except:
                except_msg()

        elif print_choice == "2":
            try:
                list_all()
                query_print("lastname")
                # lastname_input = input("Enter the last name: ").lower()
                # cursor.execute(
                #     f'SELECT * FROM person WHERE lastname = "{lastname_input}"'
                # )
                # sql_data = cursor.fetchall()
                # for e in sql_data:
                #     print(e)
            except:
                except_msg()

        elif print_choice == "3":
            try:
                list_all()
                query_print("birthyear")
            except:
                except_msg()

        elif print_choice == "4":
            try:
                list_all()
                query_print("address")
            except:
                except_msg()

        elif print_choice == "5":
            cursor = sql_connection.cursor()
            cursor.execute("SELECT * FROM person")
            sql_data = cursor.fetchall()
            if len(sql_data) > 0:
                for e in sql_data:
                    print(e)

        elif print_choice == "6":
            try:
                cursor.execute(
                    """
                SELECT firstname, lastname, hobbyname 
                FROM person AS p 
                INNER JOIN hobby AS h 
                ON p.id = h.personid
                ORDER BY firstname
                """
                )
                sql_data = cursor.fetchall()
                print("\n*** PEOPLE WITH HOBBIES ***\n")
                for e in sql_data:
                    print(e)
            except:
                except_msg()

            ### SECOND MENU END ###

    elif choice == "3":
        try:
            list_all()
            input_id = int(input("\nWho do you want to delete? Enter ID: "))
            # Using DELETE to delete a person from the database
            sql_connection.execute(f"DELETE FROM person WHERE id = '{input_id}'")
            print(f"\n *** Person {input_id} has been deleted ***")
            for p in person_list:
                # Checks if id matches any ids in the class list, when match,
                # prints out who got deleted
                if p.id == input_id:
                    print(f"\n *** {p.firstname} {p.lastname} has been deleted ***")
            update_personlist()

        except:
            except_msg()

    elif choice == "4":
        try:
            list_all()
            input_id = input("\nWhos address do you want to Update? Enter ID: ")
            new_adress = input("\nEnter the new address: ")
            # Using SET to update address in database
            sql_connection.execute(
                f"UPDATE person SET address = '{new_adress}' WHERE id = '{input_id}'"
            )
            for p in person_list:
                # Checks if id matches any ids in the class list, when match,
                # adds a new address
                if p.id == input_id:
                    p.address = new_adress
            print("\n*** Address updated ***\n")
        except:
            except_msg()

    elif choice == "5":
        list_all()
        try:
            input_id = int(input("\nEnter ID of person to add hobby to: "))
            input_hobby = input("\nEnter the name of the hobby: ")
            # Using INSERT_HOBBY_DATA to add data do our hobby table
            sql_connection.execute(hidden.INSERT_HOBBY_DATA, (input_id, input_hobby))
            print("\n*** Added Hobby ***\n")
            # Checks if id matches any ids in the class list, when match,
            # call add_hobby method with input_hobby as argument to add a hobby
            for p in person_list:
                if p.id == input_id:
                    p.add_hobby(input_hobby)
                    print(p)
        except:
            except_msg()


# Function for printing all persons in database, selects evrything in persons table
# and saves it as sql_data and then prints it out unless sql_data is empty.
def list_all():
    if not person_list == []:
        print(person_list)
    else:
        print("\n*** No data available ***\n")


def except_msg():
    print("\n*** Something went wrong. ***\n")


def query_print(column):
    userinput = input(f"\nEnter the {column} you want to query: \n")
    cursor = sql_connection.cursor()
    # Selects every row where the user input exists in the specified column
    cursor.execute(f'SELECT * FROM person WHERE {column} = "{userinput}"')
    sql_data = cursor.fetchall()
    # Loops through evry tupple in sql_data
    if len(sql_data) == 0:
        print("\n*** NO DATA AVAILABLE ***\n")
    else:
        for e in sql_data:
            for p in person_list:
                    # Checks if id matches any ids in the class list, when match, prints out the class object
                    if p.id == e[0]:
                        print(p)


# Function for updating our person list. Fetches evrything row from the person table database,
# clears person_list and adds evrything as class objecs again
def update_personlist():
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM person")
    sql_data = cursor.fetchall()
    person_list.clear()
    for e in sql_data:
        # loops through evry tupple in sql_data and uses their values to make class objecs
        # e[0] = id, e[1] = firstname, e[2] = lastname, e[3] = birthyear, e[4] = address  
        person_list.append(Person(e[0], e[1], e[2], e[3], e[4]))
    print(person_list)


class Person:
    # constructor for our Person class
    def __init__(self, id, firstname, lastname, birthyear, address):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address
        self.hobby = "Has no hobby."

    # Method to add a hobby to our persons
    def add_hobby(self, hobbyname):
        self.hobby = hobbyname

    # How our class will print itself    
    def __str__(self) -> str:
        return f"\nID: {self.id} | Name: {self.firstname} {self.lastname} | Birthyear: {self.birthyear} | Address: {self.address} | Hobby: {self.hobby}"

    # How our classes will represent themselves, allowing them to look better when we view them
    def __repr__(self) -> str:
        return f"\nID: {self.id} | Name: {self.firstname} {self.lastname} | Birthyear: {self.birthyear} | Address: {self.address} | Hobby: {self.hobby}"


# Opens our rawdata and creates a jsonfile with the data  and lets the user decide where to save it.
try:
    input_filename = input(
        "Welcome\nWhere do you want to save rawdata?\nEnter path and end with .json: "
    )
    with open((input_filename), "w+") as f:
        f.write(
            json.dumps(Rawdata.persons, indent=4)
        )  # indent = 4 to help with readability
        print(f"\n*** {input_filename} CREATED ***")
        wait_for_user()
except:
    except_msg()

# Creates a Database and a connection to it, wich we store in sql_connection
# Creates our table for persons in our database
# Creates our table for hobbys in our database
try:
    with sqlite3.connect(":memory:", isolation_level=None) as sql_connection:
        sql_connection.execute(hidden.CREATE_TABLE_PERSON)
        sql_connection.execute(hidden.CREATE_TABLE_HOBBIES)
except:
    except_msg()

# Starts our loop
start_loop()
