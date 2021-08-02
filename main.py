class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grades_av()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
        return self.grades_av() < other.grades_av()

    def grades_av(self):
        res = sum(list(map(sum, list(self.grades.values())))) / sum(list(map(len, list(self.grades.values()))))
        return round(res, 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades_av()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
        return self.grades_av() < other.grades_av()

    def grades_av(self):
        res = sum(list(map(sum, list(self.grades.values())))) / sum(list(map(len, list(self.grades.values()))))
        return round(res, 1)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 < grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def grades_av_stud(students, course):
    total_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            total_grades.append(student.grades[course])
        else:
            print('Not a student!')
    res = sum(sum(total_grades, [])) / len(sum(total_grades, []))
    return round(res, 1)


def grades_av_lect(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            total_grades.append(lecturer.grades[course])
        else:
            print('Not a lecturer!')
    res = sum(sum(total_grades, [])) / len(sum(total_grades, []))
    return round(res, 1)


student_1 = Student('Username', 'Anonymous', 'Male')
student_1.finished_courses = ['Php']
student_1.courses_in_progress = ['Python', 'Java']
student_1.grades = {'Python': [3, 5, 7], 'Java': [10, 2, 4]}

student_2 = Student('Cool', 'Hackerman', 'Female')
student_2.finished_courses = ['Php']
student_2.courses_in_progress = ['Python', 'Java']
student_2.grades = {'Python': [10, 10, 9], 'Java': [10, 8, 10]}

lecturer_1 = Lecturer('Bill', 'Gates')
lecturer_1.courses_attached = ['Python', 'Java']
lecturer_1.grades = {'Python': [10, 8, 10], 'Java': [7, 9, 10]}

lecturer_2 = Lecturer('Jason', 'Statham')
lecturer_2.courses_attached = ['Python', 'Java']
lecturer_2.grades = {'Python': [1, 3, 2], 'Java': [10, 10, 4]}

reviewer_1 = Reviewer('Steve', 'Jobs')
reviewer_1.courses_attached = ['Python', 'Java']

reviewer_2 = Reviewer('R2', 'D2')
reviewer_2.courses_attached = ['Python', 'Java']


student_1.rate_lc(lecturer_1, 'Python', 8)
print(student_2)
print(student_1 > student_2)
print(student_1.grades_av())

print(lecturer_1)
print(lecturer_1 < lecturer_2)
print(lecturer_2.grades_av())

reviewer_1.rate_hw(student_1, 'Java', 7)
print(reviewer_2)
