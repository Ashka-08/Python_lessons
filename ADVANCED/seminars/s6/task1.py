# Вспомните какие модули вы уже проходили на курсе. 
# Создайте файл, в котором вы импортируете встроенные в модуль функции 
# под псевдонимами. (3-7 строк импорта).


import random as rnd
x = rnd.randint(0, 10)

from random import randint as rint
x = rint(0, 10)

from random import * 
x = randint(0, 10)

import math as mt

import decimal as dm

import array as ar

import json as js

print(js.__all__) 
#['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecodeError', 'JSONEncoder']


# import pandas as pd
# import numpy as np