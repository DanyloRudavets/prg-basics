###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    if points>=14 and points<18:
        grade='Good'
    if points>=10 and points<14:
        grade='satisfactory'
    if points<=10:
        grade='fail'
    return grade

points = 15
final_grade = pts_to_grade(points)
print(f'You scored {points} points on the test. Your final grade is {final_grade}')