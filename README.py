class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self < avg_grade_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __lt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self < avg_grade_other


class Reviewer(Mentor):
    def grade_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nУ лекторов:"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

another_student = Student('Another', 'Student', 'your_gender')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Some', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

another_reviewer = Reviewer('Another', 'Reviewer')
another_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(another_student, 'Python', 8)
cool_reviewer.rate_hw(another_student, 'Python', 9)

best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
another_student.rate_lecture(cool_lecturer, 'Python', 10)
another_student.rate_lecture(another_lecturer, 'Python', 9)

print(cool_lecturer)
print(another_lecturer)
print(best_student)
print(another_student)
print(cool_reviewer)
print(another_reviewer)

def calculate_avg_hw_grade(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    if count > 0:
        return total_grade / count
    else:
        return 0

avg_hw_grade = calculate_avg_hw_grade([best_student, another_student], 'Python')
print(f"Средняя оценка за домашние задания по курсу Python: {avg_hw_grade:.1f}")

def calculate_avg_lecture_grade(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count > 0:
        return total_grade / count
    else:
        return 0

avg_lecture_grade = calculate_avg_lecture_grade([cool_lecturer, another_lecturer], 'Python')
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture_grade:.1f}")

if cool_lecturer < another_lecturer:
    print("Средняя оценка за лекции у cool_lecturer меньше")
else:
    print("Средняя оценка за лекции у another_lecturer меньше")

if best_student < another_student:
    print("Средняя оценка за домашние задания у best_student меньше")
else:
    print("Средняя оценка за домашние задания у another_student меньше")
