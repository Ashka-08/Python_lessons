# Напишите программу, которая использует модуль logging 
# для вывода сообщения об ошибке в файл. 
# Например отлавливаем ошибку деления на ноль.


import logging


logger = logging.getLogger('__main__')

FORMAT = '{asctime}, {levelname}, {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.ERROR, 
                    filename='ADVANCED\seminars\log1.log', filemode='a')

x, y = map(int, input('Введите два целых числа через пробел: ').split())
try:
    print((x / y))
    logger.info('Ok')
except ZeroDivisionError as e:
    print(e)
    logger.error(e)


# logging.basicConfig(level=logging.ERROR, filename='ADVANCED\seminars\log1.log', 
#                     filemode='a', format='%(asctime)s, %(levelname)s, %(message)s')

# x, y = map(int, input('Введите два целых числа через пробел: ').split())
# try:
#     print((x / y))
#     logging.info('Ok')
# except:
#     logging.error('ZeroDivisionZero')