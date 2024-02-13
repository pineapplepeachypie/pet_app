from reg_page import *
from upload_pic import *
from pet_profile import *

def upload_pic():
  print("Create your pet's profile!")
  print("Step 1: Upload your pet's picture")
  print(" \
    \n ~~~~~~~~~~~~~~~~~~ \
    \n |  U for Upload  | \
    \n ~~~~~~~~~~~~~~~~~~")

  print(" \
      \n ~~~~~~~~~~~~~~~~~~ \
      \n |   S for Skip   | \
      \n ~~~~~~~~~~~~~~~~~~")

  uploadOrSkip = input("Please choose to Upload by typing 'U' or type 'S' to Skip: ")
  pet_profiles()
