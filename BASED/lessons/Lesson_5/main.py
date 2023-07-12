# python -m pip install --upgrade pip
# pip install isOdd
# pip freeze просмотреть библиотеки
# pip freeze > requirements.txt. сохранить версии библиоте в файле


# создание виртуального окружения
# python3 -m venv venv  
# venv\Scripts\activate
# deactivate
# pip install -r requirements.txt 

# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(2)) 

# import time #встроенный таймер
# from progress.bar import Bar

# bar = Bar('Processing', max=5)
# for i in range(5):
#     # Do some work
#     time.sleep(1) # задержка в 1 сек
#     bar.next()
# bar.finish()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))


# # matplotlib библиотека графиков
# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

list = [1, 2, 3, 2, 7]
plt.plot(list)

plt.show()