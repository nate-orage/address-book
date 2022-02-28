#!/home/nate/python/python_env/bin/python3

# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/

import os
import subprocess
from typing import final
from os import read, system, name
import sys
import pandas as pd


class Contact:
    # This defines my class. Always remember to include 'self' as the first positional arg.
    def __init__(self, first, last, age, phone, email, address):
        self.first = first
        self.last = last
        self.age = age
        self.phone = phone
        self.email = email
        self.address = address
        # Contact.num_of_contacts += 1
    
    #Capitalizes First and Last name
    def fullname(self):
        return "{} {}".format(self.first.capitalize(), self.last.capitalize())
    
    #Output of a new entry
    def __str__(self):
        return f"{self.first} {self.last} -- {self.age} -- {self.phone} -- {self.email} -- {self.address}\n"


def check_file():
    #File verification - checks to see if the file exists and if so, it also checks to make sure the headers matach. If     not, a new file will be created. 
    if os.path.exists("contacts.csv"):
        check_file = pd.read_csv("contacts.csv")
        if check_file.columns.to_list() == header:
            pass
        else:
            subprocess.call(["touch", "contacts.csv"])
            new_file = pd.DataFrame(columns=header, index=None)
            new_file.to_csv("contacts.csv", index=False)
    else:
        subprocess.call(["touch", "contacts.csv"])
        new_file = pd.DataFrame(columns=header, index=None)
        new_file.to_csv("contacts.csv", index=False)


def entry_info():
    first = input(f"\nFirst name:\n")
    last = input(f"\nLast name:\n")
    age = None
    age = age_check(age)
    phone = input(f"\nPhone number:\n")
    email = input(f"\nE-mail address:\n")
    address = input(f"\nHome or Mailing address:\n")
    contacts = pd.read_csv("contacts.csv")
    contact_data = Contact(
        first.capitalize(),
        last.capitalize(),
        f"Age: " + age,
        f"Phone Number: " + phone,
        f"Email Address: " + email,
        f"Home Address: " + address,
    )
    new_contact = {
        "First": first.capitalize(),
        "Last": last.capitalize(),
        "Age": age,
        "Phone": phone,
        "E-mail": email,
        "Address": address,
    }
    # Create new dataframe based on new contact info.
    new_contact_df = pd.DataFrame(data=new_contact, index=[0], columns=header)
    new_contact_df.to_csv("contacts.csv", mode="a", index=False, header=False)
    clear()
    print(f"\n\nContact Created!! Here" "s your new contact:\n\n")
    print(contact_data)


#Input validation. Only accepts whole numbers,
def age_check(age):
    # Checking for numbers.
    while True:
        age = input(f"\nAge:\n")
        try:
            int(age)
            return age
        except ValueError:
            print(f"Please enter a whole number. {age} is not a number.\n")
            clear()
            return age_check(age)


def user_option():
    print(f"Welcome to the Address Book.\n")
    option_select = None
    #Program will keep running until the user quits by entering 'q'
    while option_select != "q":
        option_select = input(
            f"\n\nChoose an option:\n\n1 - Enter New Contact\n2 - Display Contacts\n3 - Search Contact Information\nq - Quit program\n\n"
        )
        if option_select == "1":
            entry_info()
        elif option_select == "2":
            clear()
            print(pd.read_csv("contacts.csv"))
        #Search Function. Only searches first name. All matching first names are printed with the full contact info.
        elif option_select == "3":
            clear()
            df = pd.read_csv("contacts.csv")
            query = input(f"Welcome. Please enter a first name to search for:\n\n")
            bools = []
            for i in df.First:
                if query.lower() == i.lower():
                    bools.append(True)
                else:
                    bools.append(False)
            clear()
            print(f"Here are your results for search term {query}:\n\n {df[bools]}")
        elif option_select == "q":
            clear()
            print(f"Goodbye.")
            break

#Clear screen for tidyness.
def clear():
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

#Sets headers of the dataframe, checks if the file exists, sets new_contact to None and begins the program. 
header = ["First", "Last", "Age", "Phone", "E-mail", "Address"]
check_file()
new_contact = None
user_option()
