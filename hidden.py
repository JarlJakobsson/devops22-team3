# function to create a person table in our sql database with id as primary key
CREATE_TABLE_PERSON = """
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    birthyear INTEGER,
                    address TEXT
                )
                """

# function to create a hobby table in our sql database, with hobbyid as primary key
# and personid as a forgein key that references to id in person table        
CREATE_TABLE_HOBBIES = """
                CREATE TABLE IF NOT EXISTS hobby(
                    hobbyid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    personid INTEGER NOT NULL,
                    hobbyname   TEXT NOT NULL,
                FOREIGN KEY(personid) REFERENCES person(id)
                )"""

# function to insert data into our person table with a tuple with 4 values
INSERT_PERSON_DATA = """
                INSERT INTO person(
                    firstname,
                    lastname,
                    birthyear,
                    address
                )
                VALUES (?, ?, ?, ?)
                """

# function to insert data into our hobby table with a tuple with 2 values
INSERT_HOBBY_DATA = """
            INSERT INTO hobby(
                personid,
                hobbyname
            )
            VALUES (?, ?)
            """

# As these are also constants, should probably name them with CAPITAL letters. Then it's also
# better to name them for their purpose rather than just menu1 and 2, e.g. top_menu, print_menu
# Main menu text saved as a variable
menu_text = """

    1. Load data from file
    2. Open print menu
    3. Delete person
    4. Update address
    5. Add a hobby
    
    type q or Q to exit

    """

# Second menu text saved as a variable
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
