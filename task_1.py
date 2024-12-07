# У вас есть абстракция учитель, вам надо написать класс
# согласно этой абстракции характеристики класса:
# Поля (атрибуты) класса class Teacher:
# имя (name) в примере Иван Петров;
# образование (education) в примере БГПУ;
# опыт работы (experience) в примере 4 года;
# Все атрибуты необходимо сделать защищенными.
# Для данных атрибутов необходимо написать геттеры (для всех)
# а для атрибута опыт работы (experience) также необходим еще и
# сеттер.
# Методы класса Teacher.
# get_teacher_data возвращает информацию об учителе
# результат вызова метода:
# add_mark в качестве аргументов принимает имя студента и
# его оценку, результат вызова метода:
# remove_mark в качестве аргументов принимает имя
# студента и его оценку, результат вызова метода:
# give_a_consultation в качестве аргумента принимает, класс
# в котором учатся ученики, результат вызова метода:

class Teacher:
    def __init__(self,name,education,xp):
        self.__name = name
        self.__education = education
        self.__xp = xp

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def set_xp(self,value):
        self.__xp = value

    def get_teacher_data(self):
        return print(f"{self.__name}, образование {self.__education}, опыт работы {self.__xp} года")

    def add_mark(self,student_name,student_mark):
        return print(f'{self.__name} поставил оценку {student_mark} студенту {student_name}')

    def remove_mark(self,student_name,student_mark):
        return print(f'{self.__name} удалил оценку {student_mark} студенту {student_name}')

    def give_a_consultation(self,student_class):
        return print(f'{self.__name} провел консультацию в классе {student_class}')

teacher = Teacher("Иван Петров","БГПУ","4")

teacher.get_teacher_data()
teacher.add_mark('Петр Борисов',"5")
teacher.remove_mark('Даниил Васильев',"3")
teacher.give_a_consultation("9Б")