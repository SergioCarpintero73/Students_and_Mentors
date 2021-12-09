class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_ment(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses or course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def course_in_list (self):

    def get_avg_course_grade(self, student):
        sum_grade = 0
        n = 0
        for courses, grades in student.grades:
            for grade in grades:
                sum_grade += grade
                n += 1
                avg = (sum_grade / n)
            return avg

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.avg}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет лектора!')
            return
        return self.grades < other.grades

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
            # f'Средняя оценка за лекции: {sum(self.grades)/len(self.grades)}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)

    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return student

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


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
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']
ungry_reviewer = Reviewer('Sam', 'Gnus')
ungry_reviewer.courses_attached += ['Git', 'Math']
cool_reviewer.rate_stud(student1, 'Python', 10)
cool_reviewer.rate_stud(student1, 'Git', 10)
cool_reviewer.rate_stud(student1, 'Git', 10)
ungry_reviewer.rate_stud(student1, 'Git', 6)
ungry_reviewer.rate_stud(student1, 'Math', 7)
cool_reviewer.rate_stud(student2, 'Python', 8)
cool_reviewer.rate_stud(student2, 'Git', 9)
cool_reviewer.rate_stud(student2, 'Git', 8)
ungry_reviewer.rate_stud(student2, 'Git', 2)
ungry_reviewer.rate_stud(student2, 'Math', 3)
student1.rate_ment(lecturer1, 'Math', 10)
student1.rate_ment(lecturer1, 'Python', 10)
student2.rate_ment(lecturer1, 'Math', 8)
student2.rate_ment(lecturer1, 'Python', 9)
student1.rate_ment(lecturer2, 'Git', 10)
student1.rate_ment(lecturer2, 'Python', 10)
student2.rate_ment(lecturer2, 'Git', 8)
student2.rate_ment(lecturer2, 'Python', 9)
students_list = [student1.grades, student2.grades]
lecturers_list = [lecturer1.grades, lecturer2.grades]


# am_sum_grades = 0
# sum_grades_course = 0
# for students in students_list:
#     for courses, grades in students.items():
#         for course in courses:
#             for grade in grades:
#                 sum_grades_course += grade
#                 print(course)
#                 print(grade)
#             # print(sum_grades_course)
# print(am_sum_grades)

def get_awg_course_grade(students):
    sum_grade = 0
    for student in students:
        sum_grade += student['course']
    return sum_grade


# print(student1)
# print(student1.get_avg_course_grade(self.grades))
print(students_list)
# print(len(students_list[-1]))
# print(lecturer1)
# print(lecturers_list)
print(student1.get_avg_course_grade(student1))
