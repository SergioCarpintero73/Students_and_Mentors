class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {self.__get_avg_course_grade():,.2f}\n'\
              f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'\
              f'Завершенные курсы: {",".join(self.finished_courses)}'
        return res

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_ment(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade > 0 and grade <=10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __get_avg_course_grade (self):
        """Расчёт средней оценки за все домашние задания"""
        result = []
        for grade in self.grades.values():
            result.extend(grade)
        return sum(result)/len(result)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента!')
            return
        return self.__get_avg_course_grade() < other.__get_avg_course_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__get_avg_course_grade():,.2f}'
        return res

    def __get_avg_course_grade (self):
        """Расчёт средней оценки за лекции"""
        result = []
        for grade in self.grades.values():
            result.extend(grade)
        return sum(result)/len(result)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет лектора!')
            return
        return self.__get_avg_course_grade() < other.__get_avg_course_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)

    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade > 0 and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return student

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Math']

student2 = Student('Abram', 'Ewan', 'man')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Math']

lecturer1 = Lecturer('Andy', 'McBee')
lecturer1.courses_attached += ['Math', 'Python']

lecturer2 = Lecturer('Sam', 'Smith')
lecturer2.courses_attached += ['Git', 'Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Sam', 'Gnus')
reviewer2.courses_attached += ['Git', 'Math']
 
reviewer1.rate_stud(student1, 'Python', 10)
reviewer1.rate_stud(student1, 'Git', 10)
reviewer1.rate_stud(student1, 'Git', 10)
reviewer2.rate_stud(student1, 'Git', 6)
reviewer2.rate_stud(student1, 'Math', 7)
reviewer1.rate_stud(student2, 'Python', 8)
reviewer1.rate_stud(student2, 'Git', 9)
reviewer1.rate_stud(student2, 'Git', 8)
reviewer2.rate_stud(student2, 'Git', 2)
reviewer2.rate_stud(student2, 'Math', 3)

student1.rate_ment(lecturer1, 'Math', 10)
student1.rate_ment(lecturer1, 'Python', 10)
student2.rate_ment(lecturer1, 'Math', 8)
student2.rate_ment(lecturer1, 'Python', 9)
student1.rate_ment(lecturer2, 'Git', 10)
student1.rate_ment(lecturer2, 'Python', 10)
student2.rate_ment(lecturer2, 'Git', 8)
student2.rate_ment(lecturer2, 'Python', 9)

students_list = []
students_list.append(student1)
students_list.append(student2)
lecturers_list = []
lecturers_list.append(lecturer1)
lecturers_list.append(lecturer2)

def get_student_avg_score(students, course):
    average_grade = 0
    for student in students:
        if course in student.courses_in_progress:
            grades = student.grades[course]
            average_grade += sum(grades) / len(grades)
        return average_grade
    else:
        return 'Ошибка'

def get_lecturer_avg_score(lecturers, course):
    average_grade = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            grades = lecturer.grades[course]
            average_grade += sum(grades)/len(grades)
        return average_grade
    else:
        return 'Ошибка'

print(student1)
print(student2)
print()
print(lecturer1)
print(lecturer2)
print()
print(reviewer1)
print(reviewer2)
print(get_student_avg_score(students_list, 'Python'))
print(get_lecturer_avg_score(lecturers_list, 'Python'))


