FEE = 0.015
INTEREST = 0.03
TAX = 0.1

balance = 0
menu = '1 - пополнить, 2 - снять, 3 - выход: '
run = True
counter = 0

while run:
    if balance >=5_000_000:
        balance -= TAX*balance
    if counter == 3:
        counter = 0
        balance += INTEREST*balance
    print(f'Баланс {balance}')
    
    match input(menu):
        case '1':
            num = int(input('Введите сумму пополнения, кратную 50: '))
            if num % 50 != 0:
                print('Сумма должна быть кратна 50')
                continue
            balance += num
            counter += 1
        case '2':
            num = int(input('Введите сумму снятия, кратную 50: '))
            if num % 50 != 0:
                print('Сумма должна быть кратна 50')
                continue
            num = num + 30 if num * FEE <= 30 else num + 600 if num * FEE >= 600 else num * FEE + num
            if num > balance:
                print('Сумма превышает баланс')
                continue
            balance += num
            counter += 1
        case '3':
            run = False
        case _:
            print('ошибка ввода')
        