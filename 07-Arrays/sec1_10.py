###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
questionnumber = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer==True:
      correct_answers +=1 
incorans=0
for answer in test_results:
   if answer==False:
      incorans+=1 
percent=(correct_answers/len(test_results))*100

# calculates the number of incorrect answers
...

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions:', questionnumber)
print('Number of correct answers:', correct_answers)
print("number of incorrect values:",incorans)
print(f'percent of correct: {percent: .2f}')