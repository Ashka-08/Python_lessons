# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

# a = ( "a", 'b', '2', '3' ,'c')
# b = "".join(" " if el.isdigit() else el for el in a).split()
# c = "".join(el if el.isdigit() else " " for el in a).split()
# print(b)
# print(c)
# ответ:
# ['ab', 'c']
# ['23']

# a = ( "a", 'b', '2', '3' ,'c')
# b = []
# c = []
# for i in a:
#     if i.isdigit():
#         b.append(i)
#     else:
#         c.append(i)
# print(b)
# print(c)
# Ответ
# ['2', '3']
# ['a', 'b', 'c']

a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')

b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)