# С клавиатуры вводятся две буквы (в одну строку через пробел) 
# Вывести на экран следующую строку: 
# "Коды <Буква 1> = <код буквы 1>, <Буква 2> = <код буквы 2>
# Sample Input:
# a z
# Sample Output:
# a = 97, z = 122

a,b=input().split()
print("Коды: "+a+" = "+str(ord(a))+", "+b+" = "+str(ord(b)))