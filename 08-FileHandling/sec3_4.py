###
# Calculates the total value of money spent
#
import re # module for regular expressions
c=0
# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file,'r') as file:
   email_content=file.read()
   email =(email_content)

# regular expression pattern
# for amounts
pattern = '\d{2,3}'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
for amount in amounts:
   c += int(amount)

# print result
print(c)