from company import Company

nike = Company('NIKE')
# print(*nike.employees, sep='\n')

me = nike.login('Горбунова Ольга Евгеньевна', '350747')
nike.hiring(me, 'Андерей Кривой', '123458', 4)

print(*nike.employees, sep='\n')