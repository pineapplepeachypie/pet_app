from reg_page import *
from upload_pic import *
from pet_profile import *

class User: 

    def __init__(self, fName, eAdd, pWord):
        self.fName = fName
        self.eAdd = eAdd
        self.pWord = pWord


def register_account():
    print ('Create a new account')
    fname = input("Full Name: ")
    eAdd = input('Email Address: ')
    pWord = input("Type '?' for additional information \
                  \n Password (?): ")
    if pWord == '?':
        print('Please enter a password that is at least 6 characters long, with 1 uppercase and 1 lowercase letter.')
        pWord = input("Password: ")
    #i need to implmenet password verification here. 
    pWord = input('Confirm Password: ')
    x_sign = input("Enter 'x' to confirm you have reviewed your information: ")

    while x_sign != 'x':
        x_sign = input("Enter 'x' to confirm you have reviewed your information: ")

    print(" \
      \n ~~~~~~~~~~~~~~~~ \
      \n | S for Submit | \
      \n ~~~~~~~~~~~~~~~~")
    
    submit_button = input("Please enter 'S' to Submit: ")

    user1 = User(fname, eAdd, pWord)
    return
