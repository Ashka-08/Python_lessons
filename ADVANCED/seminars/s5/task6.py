# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# Для вывода результата используйте «принт» без перехода на новую строку.

# v1
# gen = (f'{j} x {i} = {i*j}\t' if j % 5
#         else f'{j} x {i} = {i*j}\n' 
#         for i in range(2, 11) for j in range(2, 6))
# print(*gen)
# gen = (f'{j} x {i} = {i*j}\t' if j % 9
#         else f'{j} x {i} = {i*j}\n' 
#         for i in range(2, 11) for j in range(6, 10))
# print(*gen)

# v2
# def tabl_gen():
#     for i in range(2,11):
#         str = ''
#         for j in range(2,6):
#             str += f'{j} x {i} = {i*j}\t'
#             if not j % 5:
#                 str += '\n'
#         yield str
#     for i in range(2,11):
#         str = ''
#         for j in range(6,10):
#             str += f'{j} x {i} = {i*j}\t'
#             if not j % 9:
#                 str += '\n'
#         yield str


# for _, str in enumerate(tabl_gen(), start=1):
#     print(str, end=' ')

# v3
print('\n\n'.join(
    ('\n'.join(['\t'.join(
    [f'{x} x {y: >2} = {x*y:>3}' for x in range(2 + 4*k, 6 + 4*k)])
    for y in range(2,11)]) for k in range(2))))