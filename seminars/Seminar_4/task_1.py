# Создать текстовый файл, записать в него построчно данные, которые вводит 
# пользователь. Окончанием ввода пусть служит пустая строка.

# with open ('file.txt','a') as data:
#     data.write(input()+"\n")

# s=input()
# with open('sample.txt', 'a') as data:
#     while (len(s)>0):
#         data.write(s+'\n')
# s=input()
# data.close

data = open('file.txt', 'a', encoding='UTF-8')
while True:
    string = input('Введите строку: ')
    if string == '':
        break
    data.write(string + '\n')
data.close()