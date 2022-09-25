#We created a table called "Persons". It contains four columns: PersonID, FirstName, LastName, Birth and Address.
#The PRIMARY KEY uniquely IDentifies each item in a table with a unique INTEGER value.
CREATE_TABLE_PERSON = """
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birth INTEGER,
                    address TEXT
                )
                """

# New table called "Hobbies".
# The PRIMARY KEY is a clone from the "Persons" table, so that each hobby is linked to the same individual. 
CREATE_TABLE_HOBBIES = """
                CREATE TABLE IF NOT EXISTS hobby(
                    hobbyid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    personid INTEGER NOT NULL,
                    hobbyname   TEXT NOT NULL,
                FOREIGN KEY(personid) REFERENCES person(id)
                )"""

# INSERT DATA -  creates and puts to use the "persons" table in our database. 
INSERT_PERSON_DATA = """
                INSERT INTO person(
                    firstname,
                    lastname,
                    birth,
                    address
                )
                VALUES (?, ?, ?, ?)
                """
# INSERT DATA - Creates and operates "hobbies" in our database.
INSERT_HOBBY_DATA = """
            INSERT INTO hobby(
                personid,
                hobbyname
            )
            VALUES (?, ?)
            """

# Saves the text as a variable to be used later.
menu_text = """

    1. Load data from file
    2. Print persons from database
    3. Delete person
    4. Update address
    5. Add a hobby
    
    type q or Q to exit

    """

# Saves the text as a variable to be used later.
menu2_text = """

What do you want to print for

1. Firstname
2. Lastname
3. Birthyear
4. Address
5. Print all
6. Print all persons with a hobby

type q or Q to return to mainmenu

"""
