class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
                f'\nСредняя оценка за домашние задания: {self.avg_rate()} '
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} '
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.avg_rate_course() < other.avg_rate_course()

    def __le__(self, other):
        return self.avg_rate_course() <= other.avg_rate_course()

    def __eq__(self, other):
        return self.avg_rate_course() == other.avg_rate_course()

    def __gt__(self, other):
        return self.avg_rate_course() > other.avg_rate_course()

    def __ge__(self, other):
        return self.avg_rate_course() >= other.avg_rate_course()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.avg_rate()}')

    def __lt__(self, other):
        return self.avg_rate_course() < other.avg_rate_course()

    def __le__(self, other):
        return self.avg_rate_course() <= other.avg_rate_course()

    def __eq__(self, other):
        return self.avg_rate_course() == other.avg_rate_course()

    def __gt__(self, other):
        return self.avg_rate_course() > other.avg_rate_course()

    def __ge__(self, other):
        return self.avg_rate_course() >= other.avg_rate_course()

def average_student_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0

def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grades / total_lecturers if total_lecturers > 0 else 0

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

#Студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Username', 'Unknown', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

#Эксперты
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer1 = Reviewer('Yak', 'James')
cool_reviewer.courses_attached += ['Python']

#Лекторы
cool_lectorer = Lecturer('Some', 'Lecturer')
cool_lectorer1 = Lecturer('Some1', 'Unknown1')
cool_lectorer.courses_attached += ['Python']

#эксперты выставляют оценки
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 9)

#ученик выставляет оценки преподавателю
best_student.rate_lecturer(cool_lectorer, 'Python', 10)
best_student.rate_lecturer(cool_lectorer, 'Python', 9)
best_student.rate_lecturer(cool_lectorer, 'Python', 8)

print(best_student)