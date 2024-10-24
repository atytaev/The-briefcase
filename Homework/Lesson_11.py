#1
# class Soda:
#     def __init__(self, taste=None):
#         self.taste = taste
#
#     def __str__(self):
#         result = self.taste
#         if result:
#             return f'У вас газировка со вкусом {self.taste}'
#         else:
#             return f'У вас обычная газировка'
#
# soda = Soda()
# print(soda)
# soda1 = Soda('Бука')
# print(soda1)
#2
# class Math():
#     def __init__(self):
#         pass
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# math=Math()
# operator = input('Выберите действие:')
# while operator != '0':
#     try:
#         if operator == '+':
#             print(f'Сумма: {math.add(int(input('Число 1:')),int(input('Число 2:')))}')
#         if operator == '-':
#             print(f'Разница: {math.sub(int(input('Число 1:')),int(input('Число 2:')))}')
#         if operator == '*':
#             print(f'Произведение: {math.mul(int(input('Число 1:')),int(input('Число 2:')))}')
#         if operator == '/':
#             print(f'Деление: {math.div(int(input('Число 1:')),int(input('Число 2:')))}')
#     except ZeroDivisionError:
#         print('Делить на 0 нельзя!')
#     except ValueError:
#         print('Вводите только числа!')
#
#     operator = input('Выберите действие: ')
# print('Программа завершена.')

#3
# class Car:
#     def __init__(self, color, car_type, year):
#         self.color = color
#         self.type = car_type
#         self.year = year
#         self.is_running = False
#
#     def go_car(self):
#         return 'Автомобиль заведен'
#
#
#     def stop_car(self):
#         return 'Автомобиль заглушен'
#
#
#     def set_year(self, year):
#         self.year = year
#         return self.year
#
#
#     def set_type(self, car_type):
#         self.type = car_type
#         return self.type
#
#     def set_color(self, color):
#         self.color = color
#         return self.color
#
# car = Car("Серого цвета", "BMW", 1997)
# print(car.go_car())
# print(car.set_type("BMW"))
# print(car.set_color("Серого цвета"))
# print(car.set_year(1997))
# print(car.stop_car())

#4
# class Sphere:
#     def __init__(self,radius=1,x=0,y=0,z=0):
#         self.radius=radius
#         self.x=x
#         self.y=y
#         self.z=z
#     def get_volume(self):
#         return 4/3*3.14*self.radius**3
#     def get_square(self):
#         return 4*3.14*self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_center(self):
#         return (self.y,self.x,self.z)
#     def set_center(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def set_radius(self,radius):
#         self.radius=radius
#         return self.radius
#     def is_point_inside(self,x,y,z):
#         if (x-self.x)**2+(y-self.y)**2+(z-self.z)**2<self.radius**2:
#             return True
#         else:
#             return False
# sphere=Sphere(2,1,1,1)
# print(sphere.get_volume())
# print(sphere.get_square())
# print(sphere.get_radius())
# print(sphere.get_center())
# print(sphere.is_point_inside(0,0,0))

#5
# class SuperStr(str):
#     def is_repeatance(self, text):
#         if len(self) % len(text) == 0:
#             return text * (len(self) // len(text)) == self
#         else:
#             return False
#
#     def is_palindrom(self):
#         s = self.lower()
#         return s == s[::-1]
#
# s = SuperStr("axaxax")
# s2 = SuperStr("axa")
# print(s.is_repeatance("ax"))
# print(s.is_repeatance("xa"))
# print(s.is_palindrom())
# print(s2.is_palindrom())


#8 task from lesson 9
import json
# import csv
#
#
# def json_to_csv(json_file, csv_file):
#     with open(json_file, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#     with open(csv_file, 'w', newline='', encoding='UTF-8') as w_file:
#         names = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
#         file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\n', fieldnames=names)
#         file_writer.writeheader()
#         for i in data:
#             file_writer.writerow(i)
#
#
# def read_json(json_file):
#     with open(json_file, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         for i in data:
#             print(i)
#
#
# def read_csv(csv_file):
#     with open(csv_file, 'r', encoding='UTF-8') as file:
#         reader = csv.reader(file)
#         for i in reader:
#             print(i)
#
#
# def add_to_json(json_file):
#     name = str(input('Введите имя сотрудника: '))
#     birthday = int(input('Введите дату рождения сотрудника: '))
#     height = int(input('Введите рост сотрудника: '))
#     weight = int(input('Введите вес сотрудника: '))
#     car = str(input('Введите true или false: '))
#     languages = str(input('Введите язык программирования: ')).split(',')
#
#     add_employee = {
#         'name': name,
#         'birthday': birthday,
#         'height': height,
#         'weight': weight,
#         'car': car,
#         'languages': languages
#     }
#     with open(json_file, 'r+', encoding='UTF-8') as file:
#         data = json.load(file)
#         data.append(add_employee)
#         file.seek(0)
#         json.dump(data, file, indent=4)
#
#
# def add_to_csv(csv_file):
#     name = str(input('Введите имя сотрудника: '))
#     birthday = int(input('Введите дату рождения сотрудника: '))
#     height = int(input('Введите рост сотрудника: '))
#     weight = int(input('Введите вес сотрудника: '))
#     car = str(input('Введите true или false: '))
#     languages = str(input('Введите язык программирования: ')).split(',')
#
#     add_employee = {'name': name, 'birthday': birthday, 'weight': weight, 'car': car, 'languages': languages}
#
#     with open(csv_file, 'a', encoding="UTF-8", newline='') as w_file:
#         names = ['name', 'birthday', 'weight', 'car', 'languages']
#         file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\n', fieldnames=names)
#
#         if w_file.tell() == 0:
#             file_writer.writeheader()
#
#         file_writer.writerow(add_employee)
#
#
# def read_info(json_file):
#     name=str(input())
#     with open(json_file,'r',encoding='UTF-8')as file:
#         data=json.load(file)
#     for person in data:
#         if person['name'] == name:
#             return person
#
# def filter_by_languages(json_file):
#     languages=str(input())
#     lang=[]
#     with open(json_file,'r',encoding='UTF-8')as file:
#         data=json.load(file)
#     for person in data:
#         if languages['languages']:
#             lang.append(person)
#     return lang
#
# def filter_by_year(json_file):
#     year =str(input())
#     total_height=0
#     a=0
#     with open(json_file,'r',encoding='UTF-8') as file:
#         data=json.load(file)
#     for person in data:
#         if int(person['birthday'].split('.')[-1]<int(year)):
#             total_height+=person['height']
#             a+=1
#     return total_height/a
#
#
# while True:
#     print('Меню:')
#     print('1. Прочитать данные и преобразовать в JSON')
#     print('2. Сохранить данные в CSV')
#     print('3. Добавить нового сотрудника в JSON')
#     print('4. Добавить нового сотрудника в CSV')
#     print('5. Прочитать информацию о сотруднике по имени')
#     print('6. Фильтрация по году рождения')
#     print('7. Фильтрация по языку программирования')
#     print('8. Выход')
#
#     choice = input('Выберите действие: ')
#
#     if choice == "1":
#         read_json('employees.json')
#
#     elif choice == "2":
#         read_csv('output.csv')
#
#     elif choice == "3":
#         add_to_json('employees.json')
#
#     elif choice == "4":
#         add_to_csv('output.csv')
#
#     elif choice == "5":
#         print(read_info('employees.json'))
#
#     elif choice == "6":
#         print(filter_by_year('employees.json'))
#
#     elif choice == "7":
#         print(filter_by_languages('employees.json'))
#
#     else:
#         break