import json
import sqlite3
import hidden

running = True

def user_choice():
    if running == True:
        return input("Enter your choice: ")

def wait_for_user():
        input("Please press any key to continues.")

def start_loop():
    while running:
        print(hidden.menu_text)
        choice = user_choice()
        menu_commands(choice)
        wait_for_user()

def menu_commands(choice):

    #CREATING CURSOR TO OUR SQLCONNECTION
    cursor = sql_connection.cursor()

    if choice == "q" or choice == "Q":
        return running == False

    elif choice == "1":
        with open("jsonpersons.json") as f:
            json_persons = json.load(f)
            person_list = []
            for p in json_persons["persons"]:
                person_list.append(Person(p["firstname"], p["lastname"], p["birth"], p["address"]))
                sql_connection.execute(hidden.INSERT_PERSON_DATA, tuple(p.values()))
        print("*** DATABASE LOADED ***")

    ### SECOND MENU START ###
    elif choice == "2":
        print(hidden.menu2_text)

        print_choice = input("Enter choice: ")
        if print_choice == "q" or choice == "Q":
            print("*** Returning to mainmenu ***")

        elif print_choice == "1":
            list_all()
            firstname_input = input("Enter the first name: ").lower()
            #cursor = sql_connection.cursor()
            cursor.execute(
                f'SELECT * FROM person WHERE firstname = "{firstname_input}"'
            )
            sql_data = cursor.fetchall()
            for e in sql_data:
                print(e)

        elif print_choice == "2":
            list_all()
            lastname_input = input("Enter the last name: ").lower()
            #cursor = sql_connection.cursor()
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
            cursor.execute(f'SELECT * FROM person WHERE birth = "{birth_input}"')
            sql_data = cursor.fetchall()
            for e in sql_data:
                print(e)

        elif print_choice == "4":
            list_all()
            address_input = input("Enter the address of the person: ").lower()
            cursor.execute(
                f'SELECT * FROM person WHERE address = "{address_input}"'
            )
            sql_data = cursor.fetchall()
            for e in sql_data:
                print(e)
            input("Press any key to continue... ")

        elif print_choice == "5":
            print("*** HERE IS ALL DATA ***")
            list_all()
        
        elif print_choice == "6":
            try:
                cursor.execute(
                '''
                SELECT firstname, lastname, birth, address, hobbyname 
                FROM person AS p 
                INNER JOIN hobby AS h 
                ON p.id = h.personid
                ORDER BY firstname
                '''
                )
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
            new_adress = input("\nEnter the new address: ")
            sql_connection.execute(f"UPDATE person SET address = '{new_adress}' WHERE id = '{userinput}'")
            print("\n Address updated")
        except:
            except_msg()
    
    elif choice == "5":
        list_all()
        try:
            userid = int(input("Enter ID of person to add hobby: "))
            input_hobby = input("Enter the name of the hobby: ")
            sql_connection.execute(hidden.INSERT_HOBBY_DATA, (userid, input_hobby))
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

with sqlite3.connect(":memory:", isolation_level=None) as sql_connection:
    sql_connection.execute(hidden.CREATE_TABLE_PERSON)
    sql_connection.execute(hidden.CREATE_TABLE_HOBBIES)
    
cursor = sql_connection.cursor()

def list_all():
    #cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM person")
    sql_data = cursor.fetchall()
    for e in sql_data:
        print(e)

def except_msg():
    print("Something went wrong.")

start_loop()
