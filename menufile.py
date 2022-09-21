#import json
#import sqlite3
#from Rawdata import persons
import functions
#import test

class Menu:

    meny_text = """
    Welcome to this program!

    1. Load data
    2. List all persons from Database
    3. Delete your object
    
    type q or Q to delete
    """

    def user_choice(self):
        return input("Enter your choice 1-3 or q: ")

    def wait_for_user(self):
        if self.running:
            input("Please press any key to continues.")

    def menu_commands(self, choice):
        if choice == 'q' or choice == 'Q':
            self.running = False
            
        elif choice == "1":
           functions.load_file()
           pass

        elif choice == "2":
            pass

        elif choice == "3":
            pass

    # def start_loop(self):
    #     self.running = True
    #     while self.running:
    #         print(Menu.meny_text)
    #         choice = self.user_choice()
    #         self.menu_commands(choice)
    #         self.wait_for_user()

# Menu().start_loop()