# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению 
# Решки. Напишите программу, которая подсчитывает наибольшее количество подряд 
# выпавших Решек.
# На вход программе подается строка текста, состоящая из букв русского алфавита 
# "О" и "Р".
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.

# Тестовые данные
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

""" 1 Вариант """
# text_input = str(input("введите текст: "))
# max_RESULT = 0
# reshka_in_raw = 0
# for i in range(text_input.__len__()):
#     if text_input[i] == 'Р':
#         reshka_in_raw = reshka_in_raw+1
#         if reshka_in_raw>max_RESULT:
#             max_RESULT = reshka_in_raw
#     else:
#         reshka_in_raw = 0
# print(max_RESULT)

text = input("Input: ")
max = 0
c = 0
for i in range(text.__len__()):
    if text[i] == 'Р':
        c += 1
        if c > max:
            max = c
    else:
        c = 0
print(max)

""" 2 Вариант """
# str = str(input("введите текст: "))
# listRes = str.split('О')
# print(listRes)
# max = len(listRes[0])
# for i in listRes:
#     if len(i) > max:
#         max = len(i)
# print(max)

""" 3 Вариант """
# s=input()
# t=0
# while "Р"*(t+1) in s:
#     t+=1
# if t!=0:
#     print(t)
# else:
#     print(0)