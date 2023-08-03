# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


from random import randint, sample, shuffle

def gen_name():
    vowel = 'аеиоуэюя'
    consonant = 'бвгджзклмнпрстфхцчшщ'
    a = randint(4,7)
    v = randint(1, a-2)
    s = sample(vowel, v) + sample(consonant, a - v)
    shuffle(s)
    print(res := ''.join(s).title())
    return res

with open('s7_task2.txt', 'a', encoding='utf-8') as f:
    for _ in range(6):
        f.writelines(gen_name() + '\n')