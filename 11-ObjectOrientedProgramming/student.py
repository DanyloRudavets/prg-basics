# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.mood=''

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21
    student1.mood = 'Nice'
    student2.mood ='Bored'
    student3= Student()
    student3.name='Fill'
    student3.age=22
    student3.mood = 'Great'

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old {student1.mood}')
    print(f'{student2.name}, {student2.age} years old {student2.mood}')
    print(f'{student3.name}  {student3.age}  {student3.mood}')

if __name__ == "__main__":
    main()