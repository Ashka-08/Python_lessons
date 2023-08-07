# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import pickle
import json

def json_to_pickle():
    for file in os.listdir():
        if file.endswith('.json'):
            with (
                open(file, 'r') as file_in,
                open(f'{file[:-5]}.pickle', 'wb') as file_out
                ):
                pickle.dump((json.load(file_in)), file_out)


json_to_pickle()