# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# находим степени
def rank(st):
    if 'x^' in st:
        i = st.find('^')
        num = int(st[i+1:])
    elif ('x' in st) and ('^' not in st):
        num = 1
    else:
        num = -1
    return num

# находим коэффициенты
def koeff(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбираем на коэффициенты и степени
def analysis(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if rank(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1               # степень
    ii = l-1            # индекс
    while ii >= 0:
        if rank(st[ii]) != -1 and rank(st[ii]) == i:
            lst.append(koeff(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1        
    return lst

# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    temp = ''
    if len(lst) < 1:
        temp = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                temp += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    temp += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                temp += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    temp += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                temp += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                temp += ' = 0'
    return temp

# находим в файлах оба многочлена
with open('task_5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('task_5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен\n {st1}")
print(f"Второй многочлен\n {st2}")

# складываем многочлены
lst1 = analysis(st1)
lst2 = analysis(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])

# записываем результат
st3 = create_str(lst_new)
print(f"Сумма многочленов равна\n [{st3}]")
# with open('task_5_3.txt', 'w') as data:
#         data.write(st3)