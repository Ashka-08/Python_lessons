# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя 
# из того, что один любой символ (в том числе пробел) стоит
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
# На вход программе подается строка текста.
# Программа должна вывести стоимость строки.

# Тестовые данные

# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.

# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.

text_string = input('Введите текс: ')
symb_number = len(text_string)
coast = symb_number * 60
print(f'{coast // 100} руб. {coast % 100} коп.')

# a=input()
# b=(len(a)*60)//100
# c=(len(a)*60)-b*100
# print(b,"р.",c,"коп.")