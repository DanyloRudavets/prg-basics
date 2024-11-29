###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'
n=1
with open(file_name, 'r') as s:
   content=s.read()
   file_lines=content.splitlines()
   for line in file_lines:
      if job_title in line:
         print(n)
         n+=1