# class Product:
#     def __init__(self, name:str, store:str, price: float):
#         self.__name = name
#         self.__store = store
#         self.__price = price
#
#
#     def get_name(self)->str:
#         return self.__name
#     def get_store(self)->str:
#         return self.__store
#     def get_price(self)->float:
#         return float(self.__price)
#     def __add__(self, other):
#         if isinstance(other, Product):
#             return self.__price+other.__price
#         elif isinstance(other, (float, int)):
#             return self.__price +other
#         else:
#             raise TypeError (f'unsupported operand type(s) for +: "Product" and "{type(other)}"')
#     def __str__(self):
#         return f"{self.__name} ({self.__store}) - {self.__price} руб."
# class Sklad:
#     def __init__(self):
#         self.__products = []
#
#     def summa_price(self)->float:
#         summary = 0
#         for p in self.__products:
#             summary = p + summary
#         return summary
#     def add_product(self, product):
#         self.__products.append(product)
#
#     def find_product_by_index(self, index):
#         return self.__products[index]
#
#     def find_product_by_name(self, name):
#         for product in self.__products:
#             if product.get_name() == name:
#                 return product
#         return None
#
#     def sort_by_name(self):
#         self.__products.sort(key=lambda x: x.get_name())
#     def sort_by_store(self):
#         self.__products.sort(key=lambda x: x.get_store())
#     def sort_by_price(self):
#         self.__products.sort(key=lambda x: x.get_price())
#
#
#     def __str__(self):
#         output = ""
#         for product in self.__products:
#             output += str(product) + "\n"
#         return output
#
#     def __add__(self, other):
#         result = Sklad()
#         for product in self.__products:
#             result.add_product(product)
#         for product in other.__products:
#             result.add_product(product)
#         return result
#
# product1 = Product("Яблоки", "i-store", 50)
# product2 = Product("Молоко", "Магазин 2", 80)
# product3 = Product("Хлеб", "Магазин 3", 30)
#
# sklad = Sklad()
# sklad.add_product(product1)
# sklad.add_product(product2)
# sklad.add_product(product3)
# print(sklad)
# print(sklad.find_product_by_index(2))
# print(sklad.find_product_by_name("Яблоки"), '\n')
#
# sklad.sort_by_name()
# print(f"Сортировка по названию наименованию: \n{sklad}")
#
# sklad.sort_by_store()
# print(f"Сортировка по названию магазину: \n{sklad}")
#
# sklad.sort_by_price()
# print(f"Сортировка по цене: \n{sklad}")
#
# new_sklad = sklad + sklad
#
# print(f'Cложение двух складов: {new_sklad.summa_price()}')

#
# class BeeElephant:
#     def __init__(self, bee_part, elephant_part):
#         self.bee_part = bee_part
#         self.elephant_part = elephant_part
#     def fly(self):
#         return self.bee_part >= self.elephant_part
#     def trumpet(self):
#         if self.elephant_part >= self.bee_part:
#             return 'tu-tu-doo-doo'
#         else:
#             return 'wzzzz'
#     def eat(self, meal, value):
#         if meal == 'nectar':
#             self.elephant_part = max(0, self.elephant_part - value)
#             self.bee_part = min(100, self.bee_part + value)
#         elif meal == 'grass':
#             self.bee_part = max(0, self.bee_part - value)
#             self.elephant_part = min(100, self.elephant_part + value)
#     def get_parts(self):
#         return [self.bee_part, self.elephant_part]
#
# beeelephant = BeeElephant(3,2)
# print(beeelephant.fly())
# print(beeelephant.trumpet())
# beeelephant.eat('nectar', 1)
# print(beeelephant.get_parts())
#
# be = BeeElephant(13, 87)
# print(be.fly())
# print(be.trumpet())
# be.eat('nectar', 90)
# print(be.trumpet())
# print(be.get_parts())

# class Bus:
#     def __init__(self, speed, max_places, max_speed):
#         self.speed = speed
#         self.max_places = max_places
#         self.max_speed = max_speed
#         self.surnames = []
#         self.has_empty_seats = True
#         self.seats = {i: None for i in range(1, max_places + 1)}
#
#     def board (self, *surnames):
#         for surname in surnames:
#             if len(self.surnames) < self.max_places:
#                 self.surnames.append(surname)
#                 for seat, name in self.seats.items():
#                     if name is None:
#                         self.seats[seat] = surname
#                         break
#                 print(f'{surname} сел в автобус')
#             else:
#                 print('Автобус переполнен')
#         self.has_empty_seats = len(self.surnames) < self.max_places
#
#     def exit (self, *surnames):
#         for surname in surnames:
#             if surname in self.surnames:
#                 self.surnames.remove(surname)
#                 for seat, name in self.seats.items():
#                     if name == surname:
#                         self.seats[seat] = None
#                         break
#                 print(f'{surname} вышел с автобуса')
#         self.has_empty_seats = len(self.surnames) < self.max_places
#
#     def increase_speed(self, speed_incrase):
#         self.speed = min(self.speed + speed_incrase,self.max_speed)
#
#     def decrease_speed(self, speed_decrase):
#         self.speed = max(self.speed + speed_decrase, 0)
#
#     def __contains__(self, surname):
#         return surname in self.surnames
#     def __iadd__(self, surname):
#         self.board(surname)
#         return self
#     def __isub__(self, surname):
#         self.exit(surname)
#         return self
#
# bus = Bus(speed=50, max_places=50, max_speed=90)
# bus.board('Alice', 'Bob', 'David', 'Max')
#
# print(bus.surnames)
# print(bus.has_empty_seats)
#
# bus -= 'Bob'
# bus += 'Mafrodi'
# bus += 'Al Capone'
# print(bus.seats)
# print(bus.surnames)
#
# bus.increase_speed(50)
# bus.decrease_speed(25)
# print(bus.speed)



