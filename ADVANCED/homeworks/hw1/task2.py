# Напишите код, который запрашивает число и сообщает является ли оно простым 
# или составным. Используйте правило для проверки: 
# «Число является простым, если делится нацело только на единицу и на себя». 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    n = input('Введите положительное число не больше 100 тысяч: ')
    if n.isdigit():
        num = int(n)
        if num == 0:
            print('На 0 делить нельзя')
            continue
        if num < 0 or num > 100000:
            print('Ошибка, попробуйте еще')
            continue
        
        count = 0
        for i in range(2, num // 2+1):
            if (num % i == 0):
                count += 1
        if (count <= 0):
            print("Число простое")
        else:
            print("Число не является простым")
        break
    
    else: 
        print('Ошибка, введено не целое число')
        continue