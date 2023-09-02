# Логирование

import logging

logging.info('Немного информации')
logging.error('Поймали ошибку')
print('\n')

# Базовые регистраторы

import logging
logging.basicConfig(level=logging.NOTSET)
logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом всё')
print('\n')
"""
DEBUG:root:Очень подробная отладочная информация. Заменяем множество "принтов"
INFO:root:Немного информации о работе кода
WARNING:root:Внимание! Надвигается буря!
ERROR:root:Поймали ошибку. Дальше только неизвестность
CRITICAL:root:На этом всё
"""


# работать с регистраторами напрямую запрещено

import logging
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')
print('\n')


# ситуация с несколькими файлами

import logging
from other import log_all
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
print('\n')

"""
WARNING:Основной файл проекта:Внимание! Используем вызов функции из другого модуля
WARNING:other:Внимание! Надвигается буря!
ERROR:other:Поймали ошибку. Дальше только неизвестность
CRITICAL:other:На этом всё
"""

# Подробнее о basicConfig

import logging
from other import log_all

logging.basicConfig(filename='ADVANCED\lessons\l15\project.log', filemode='w',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
print('\n')


# Формат сохранения события “{“ 

import logging
from other import log_all

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('__main__')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
print('\n')


# Задание

import logging
logging.basicConfig(
    filename="log/log.log",
    encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.WARNING
    )
