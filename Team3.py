import json
import sqlite3
import hidden

running = True
person_list = []


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

    # CREATING CURSOR TO OUR SQL CONNECTION
    cursor = sql_connection.cursor()

    if choice == "q" or choice == "Q":
        return running == False

    elif choice == "1":
        try:
            with open("jsonpersons.json") as f:
                json_persons = json.load(f)
                for d in json_persons["persons"]:
                    ## p will be a dict with first:value, last:value, birth: value, address: value.
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

        print_choice = input("Enter choice: ")
        if print_choice == "q" or choice == "Q":
            print("\n*** Returning to mainmenu ***\n")

        elif print_choice == "1":
            try:
                list_all()
                firstname_input = input("Enter the first name: ").lower()
                cursor.execute(
                    f'SELECT * FROM person WHERE firstname = "{firstname_input}"'
                )
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)
            except:
                except_msg()

        elif print_choice == "2":
            try:
                list_all()
                lastname_input = input("Enter the last name: ").lower()
                cursor.execute(f'SELECT * FROM person WHERE lastname = "{lastname_input}"')
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)
            except:
                except_msg()

        elif print_choice == "3":
            try:
                list_all()
                birth_input = int(
                    input("Enter the birthyear of the person you want to printout: ")
                )
                cursor.execute(f'SELECT * FROM person WHERE birth = "{birth_input}"')
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)
            except:
                except_msg()

        elif print_choice == "4":
            try:
                list_all()
                address_input = input("Enter the address of the person: ").lower()
                cursor.execute(f'SELECT * FROM person WHERE address = "{address_input}"')
                sql_data = cursor.fetchall()
                for e in sql_data:
                    print(e)
                input("Press any key to continue... ")
            except:
                except_msg()

        elif print_choice == "5":
            print("*** HERE IS ALL DATA ***")
            list_all()

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
                for e in sql_data:
                    print(e)
            except:
                except_msg()

            ### SECOND MENU END ###

    elif choice == "3":
        try:
            list_all()
            input_id = int(input("\nWho do you want to delete? Enter ID: "))
            sql_connection.execute(f"DELETE FROM person WHERE id = '{input_id}'")
            print(f"\n *** Person {input_id} has been deleted ")
            update_personlist()

        except:
            except_msg()

    elif choice == "4":
        try:
            list_all()
            input_id = input("\nWhos address do you want to Update? Enter ID: ")
            new_adress = input("\nEnter the new address: ")
            sql_connection.execute(
                f"UPDATE person SET address = '{new_adress}' WHERE id = '{input_id}'"
            )
            for p in person_list:
                if p.id == input_id:
                    p.address = new_adress
            print("\n*** Address updated ***\n")
        except:
            except_msg()

    elif choice == "5":
        list_all()
        try:
            input_id = int(input("Enter ID of person to add hobby: "))
            input_hobby = input("Enter the name of the hobby: ")
            sql_connection.execute(hidden.INSERT_HOBBY_DATA, (input_id, input_hobby))
            print("\n*** Added Hobby ***\n")
            for p in person_list:
                if p.id == input_id:
                    p.add_hobby(input_hobby)
            print(person_list)
        except:
            except_msg()


def list_all():
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM person")
    sql_data = cursor.fetchall()
    for e in sql_data:
        print(e)


def except_msg():
    print("\n*** Something went wrong. ***\n")


def update_personlist():
    cursor = sql_connection.cursor()
    cursor.execute("SELECT * FROM person")
    sql_data = cursor.fetchall()
    person_list.clear()
    for e in sql_data:
        person_list.append(Person(e[0], e[1], e[2], e[3], e[4]))
    print(person_list)


class Person:
    def __init__(self, id, firstname, lastname, birthyear, address):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.address = address
        self.hobby = "Has no hobby."

    def add_hobby(self, hobbyname):
        self.hobby = str(hobbyname)

    def __str__(self):
        return self.lastname

    def __repr__(self) -> str:
        return f"\nID: {self.id} | Name: {self.firstname} {self.lastname} | Birthyear: {self.birthyear} | Address: {self.address} | Hobby: {self.hobby}"


with sqlite3.connect(":memory:", isolation_level=None) as sql_connection:
    sql_connection.execute(hidden.CREATE_TABLE_PERSON)
    sql_connection.execute(hidden.CREATE_TABLE_HOBBIES)

start_loop()
