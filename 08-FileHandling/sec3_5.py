###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username =input('username:')
password = input('password:')

# pattern (criteria) for username and password
username_pattern ='[a-z]{6,}'
password_pattern = '[A-Z-za-z-z0-9_]{8,}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match :
   print(True)
else:
   print(False)