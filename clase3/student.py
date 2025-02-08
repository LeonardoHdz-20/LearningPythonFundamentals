from clase2.lists import count


class Student:

    count = 0

    def __init__(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
        Student.count += 1

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Language: {self.language}, City: {self.city}'


    @staticmethod
    def get_total_students(self):
        return self.count

    @classmethod
    def get_total_students(cls):
        return cls.count

if __name__ == '__main__':
    estudiante = Student(name='Juan', age=21, language='Python', city='Math')
    print(Student.get_total_students())
    print(Student.get_total_students_class())
    estudiante.name = 'Josesito'
    print(estudiante)

    estudiante_2 = Student(name='Ana', age=21, language='Python', city='Math')
    print(Student.get_total_students())
    print()
