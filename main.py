#                           Home Task 4

# Task 1
# Модифицируйте первое домашнее задание (О заказе),
# добавив проверки в методы классов и обработку исключительных ситуаций. При попытке установить отрицательную или
# нулевую стоимость товара следует вызвать исключительную ситуацию, тип которой реализовать самостоятельно.


# Task 2
# Модифицируйте второе домашнее задание (Дисконт) добавив проверки в методы классов и обработку исключительных ситуаций.
# При попытке установить скидку не в пределах 0-100% - следует вызвать исключительную ситуацию,
# тип которой реализовать самостоятельно.


class StudentsLimitError(Exception):
    def __init__(self, max_students, message='Too many students'):
        self.max_students = max_students
        self.message = message
        super().__init__()

    def __str__(self):
        return f'Limit of students is {self.max_students}\n. {self.message}'


class Student:

    def __init__(self, name, date_of_birth, sex):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex

    def __str__(self):
        return f'{self.name}'


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.max_students = max_students
        self.__students = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError('Not a Student')
        if student in self.__students:
            raise ValueError('Student already in group')
        if len(self.__students) == self.max_students:
            raise StudentsLimitError(self.max_students)

        self.__students.append(student)
