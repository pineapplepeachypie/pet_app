from reg_page import *
from upload_pic import *
from pet_profile import *

print(" \
      \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \
      \n|  Keep track of your furry friend's info | \
      \n|  & vet records to better care for their | \
      \n|          health and well-being!         | \
      \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \ ")

print(" \
      \n ~~~~~~~~~~~~~~~~~~ \
      \n | R for Register | \
      \n ~~~~~~~~~~~~~~~~~~")

print(" \
      \n ~~~~~~~~~~~~~~~~~ \
      \n |  L for Login  | \
      \n ~~~~~~~~~~~~~~~~~")

regOrLogin = input("Please choose to Register by typing 'R' or type 'L' to login: ")

if regOrLogin == 'R':
    register_account()

upload_pic()
