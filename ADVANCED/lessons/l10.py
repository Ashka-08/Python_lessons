"""Классы"""


class Person:
    max_up = 3 # Атрибут класса

p1 = Person() # Экземпляр класса
print(p1.max_up)

print(Person.max_up) # Обращение к атрибуту класса через точечную нотацию

p2 = Person()
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
p1.max_up = 12 # локальная область видимости экземпляра класса
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 42
print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

# Динамическая структура класса

Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
p1.health = 100 # объявление локальной переменной внутри р1
# print(f'{Person.health = }, {p1.health = }, {p2.health = }') 
# AttributeError: type object 'Person' has no attribute 'health'
# print(f'{p1.health = }, {p2.health = }') 
# AttributeError: 'Person' object has no attribute 'health'
print(f'{p1.health = }')


# Возможность динамически изменять класс - как аналог работы со словарями dict.
class Person:
    pass

p1 = Person()
p1.level = 1
p1.health = 100
dict_p1 = {}
dict_p1['level'] = 1
dict_p1['health'] = 100
print(f'{p1.health = }')
print(f'{dict_p1["health"] = }')

# Конструктор экземпляра магический метод __init__()

class Person:
    max_up = 3

    def __init__(self):
        self.level = 1  # Это атрибут экземпляра
        self.health = 100

p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health = }') 
# AttributeError: type object 'Person' has no attribute 'level'
Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

# Передача аргументов в экземпляр

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')

# Методы класса

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.level = }, {p2.level = }, {p3.level = }')
p3.level_up()
p1.level_up()
p3.level_up()
print(f'{p1.level = }, {p2.level = }, {p3.level = }')

# При желании можно передавать в метод аргументы

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')

# Задание

class User:
    count = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')
u1.count.append(42)
u1.count.append(73)
u2.counter = 256
u2.count.append(u2.counter)
u2.count.append(u1.count[-1])
print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# u1.name = 'One', u1.phone = '123-45-67', u1.count = [42, 73, 256, 256]
print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
# u2.name = 'NoOne', u2.phone = '76-54-321', u2.count = [42, 73, 256, 256]


"""Инкапсуляция"""

# Одно подчёркивание в начале - protected — защищённый доступ

class Person:
    max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

p1 = Person('Сильвана', 'Эльф', 120)
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу', speed=60)
print(f'{p1._max_level = }')
print(f'{p2._speed = }')
p2._speed = 150
print(f'{p2._speed = }')
p3.level_up()
print(f'{p3.level = }')
p3.level = 80
p3.level_up()
print(f'{p3.level = }')


# Два подчёркивания в начале - private — приватный доступ

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')
p1.up = 1
print(f'{p1.up = }')
for _ in range(5):
    p1.add_up()
    print(f'{p1.up = }')
# print(p1.__max_up) # AttributeError: 'Person' object has no
# attribute '__max_up'
# print(Person.__max_up) # AttributeError: type object 'Person'
# has no attribute '__max_up'


# Задание

class User:

    def __init__(self, name, phone, password):
        self.__name__ = name # нельзя перепределять магические переменные
        self._phone = phone
        self.__password = password

u1 = User('One', '123-45-67', 'qwerty')
print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password =}')
# нельзя обращаться к защищенным переменным вне класса и к приватным тем более 


"""Наследование"""

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
    
    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)
    
class Hero(Person): # дочерний класс
        
    def __init__(self, power, *args, **kwargs):
        self.power = power # добавить герою свойство
        super().__init__(*args, **kwargs) # метод инициализации родительского класса

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)

p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
print(f'{p1.name = }, {p1.up = }, {p1.power = }')


# Множественное наследование

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
    
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
    
    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

class Address:
    
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'

class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'

class Hero(Person, Address, Weapon):

    def __init__(self, power, name=None, race=None, speed=None,
        country=None, city=None, street=None,
        left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)

p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
country='Эльфляндия', street='Ночного эльфа',
left_hand='Стрела')
print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')


# MRO — method resolution order переводится как “порядок разрешения методов”

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'

class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'

class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'

class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()

class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()

class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()

class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()
        print(*Z.mro(), sep='\n')

"""
Разберём результат работы mro с нашим классом Z.
● В первую очередь отрабатывает инициализация самого класса.
● Далее начинаем двигаться слева направо по списку родительских классов:
X1, X2
● Следующим будет класс B. Почему он, а не X3? Класс B является
родительским только для класса X2. Так мы не нарушаем порядок слева
направо и старшинство.
● Следующим инициализируется X3, последний из родительских классов у Z.
● Далее идёт инициализация класса A. Он родитель для X1 и X3. Следовательно
его инициализация была невозможна раньше дочерних классов.
● Классы С и D инициализируются последними, они правее A, B и С в списке
родительских классов у “иксов”.
● Класс object всегда инициализируется в последнюю очередь.
Поиск аргументов и методов в экземпляре класса Z будет происходить в порядке,
представленном методом mro.

"""

z = Z()
print(f'{z.data_b = }')
# print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a'

"""
Вызов метода __init__ остановился на классе B. Мы не дописали ему вызов super,
считая что он и так не имеет наследников. В результате аргумент data_a не был
создан в экземпляре класса z. 
"""

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Текст')
        print(self.data_b)


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'

class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'

class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'

class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()

class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()

class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()

class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()
        print(*Z.mro(), sep='\n')

z = Z()
z.say() # B
print()


# Задание
class A:
    name = 'A'

    def call(self):
        print(f'I am {self.name}')

class B:
    name = 'B'

    def call(self):
        print(f'I am {self.name}')

class C:
    name = 'C'

    def call(self):
        print(f'I am {self.name}')

class D(C, A):
    pass
class E(D, B):
    pass

e = E()
e.call() #I am C


"""Полиморфизм"""

path_1 = '/home/user'
path_2 = '/my_project/workdir'
# result = path_1 / path_2 # TypeError: unsupported operand type(s) for /: 'str' and 'str'


class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)
        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)

path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}') 
# result = '/home/user/my_project/workdir', <class '__main__.DivStr'>
print(f'{result / "text" = }') # result / "text" = '/home/user/my_project/workdir/text'
print(f'{result / 42 = }') # result / 42 = '/home/user/my_project/workdir/42'
print(f'{result * 3 = }')
# result * 3 = '/home/user/my_project/workdir/home/user/my_project/workdir/home/user/my_project/workdir'

