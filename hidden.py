<<<<<<< HEAD
# function to creata a person table in our sql database with id as primary key

=======
#We created a table called "Persons". It contains four columns: PersonID, FirstName, LastName, Birth and Address.
#The PRIMARY KEY uniquely IDentifies each item in a table with a unique INTEGER value.
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
CREATE_TABLE_PERSON = """
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birthyear INTEGER,
                    address TEXT
                )
                """

<<<<<<< HEAD
# function to create a hobby table in our sql database, with hobbyid as primary key
# and personid as a forgin key that refrences to id in person table        
=======
# New table called "Hobbies".
# The PRIMARY KEY is a clone from the "Persons" table, so that each hobby is linked to the same individual. 
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
CREATE_TABLE_HOBBIES = """
                CREATE TABLE IF NOT EXISTS hobby(
                    hobbyid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    personid INTEGER NOT NULL,
                    hobbyname   TEXT NOT NULL,
                FOREIGN KEY(personid) REFERENCES person(id)
                )"""

<<<<<<< HEAD
# function to insert data into our person table. It want 4 values
=======
# INSERT DATA -  creates and puts to use the "persons" table in our database. 
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
INSERT_PERSON_DATA = """
                INSERT INTO person(
                    firstname,
                    lastname,
                    birthyear,
                    address
                )
                VALUES (?, ?, ?, ?)
                """
<<<<<<< HEAD

# function to insert data into our hobby table. Takes 2 values
=======
# INSERT DATA - Creates and operates "hobbies" in our database.
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
INSERT_HOBBY_DATA = """
            INSERT INTO hobby(
                personid,
                hobbyname
            )
            VALUES (?, ?)
            """

<<<<<<< HEAD
# Main menu text saved as a variable
=======
# Saves the text as a variable to be used later.
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
menu_text = """

    1. Load data from file
    2. Print persons from database
    3. Delete person
    4. Update address
    5. Add a hobby
    
    type q or Q to exit

    """

<<<<<<< HEAD
# Second menu text saved as a variable
=======
# Saves the text as a variable to be used later.
>>>>>>> a610fb69bce202f25a04f6c10f6ace618b451070
menu2_text = """

What do you want to print for?

1. Firstname
2. Lastname
3. Birthyear
4. Address
5. Print all
6. Print all persons with a hobby

type q or Q to return to mainmenu

"""
