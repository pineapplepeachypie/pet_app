from reg_page import *
from upload_pic import *
from pet_profile import *

class Pet():
    
    def __init__(self, name, dob, breed, weight):
        self.name = name
        self.dob = dob
        self.breed = breed
        self.weight = weight

def pet_profiles():
  print ("Create your pet's profile!")
  print("Step 2: Fill in your pet's information")
  name = input("Name: ")
  dob = input('Date of Birth: ')
  breed = input('Breed: ')
  weight = input('Weight: ')

  print(" \
    \n ~~~~~~~~~~~~~~~~ \
    \n | S for Submit | \
    \n ~~~~~~~~~~~~~~~~")

  print(" \
    \n ~~~~~~~~~~~~~~~~ \
    \n | R for Return | \
    \n ~~~~~~~~~~~~~~~~")
  submit = input("Enter 'S' to Submit or 'R' to Return: ")
  if submit == 'S':
    pet1 = Pet(name, dob, breed, weight)
