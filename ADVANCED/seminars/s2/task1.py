# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

num = 15
flag = True
string = 'String'
fl = 2.15
print(type(num), type(flag), type(string), type(fl), end="\n")
# <class 'int'> <class 'bool'> <class 'str'> <class 'float'>
lst = [1, 2]
kor = (1, 2)
st = {1, 2}
dic = \
    {
    1 : 'one',
    2 : 'two'
    }
print(type(lst), type(kor), type(st), type(dic))
# <class 'list'> <class 'tuple'> <class 'set'> <class 'dict'>
