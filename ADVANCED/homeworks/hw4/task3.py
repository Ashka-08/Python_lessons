# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

def addition():
    global total_cash
    global count
    global history
    add = int(input("внесите сумму кратную 50: "))
    if add % 50 == 0:
        total_cash += add
        count += 1
        history.append(['add', add])
    else:
        print("неверная сумма")


def withdrawal():
    global total_cash
    global count
    global history
    take = int(input("введите сумму снятия кратную 50: "))
    if take % 50 == 0:
        percent = take*1.5*0.01
        if percent < 30 :
            percent = 30
        if percent > 600:
            percent = 600

        if total_cash < (take+percent):
            print("недостаточно средств")
        else:
            total_cash -= (take+percent)
            count += 1
            history.append(['withdrawal', take, percent])
    else:
        print("неверная сумма")

total_cash = 0
count = 0
history = []
while True:

    if total_cash > 5_000_000:
        total_cash *= 0.9

    print("сумма на счете ", total_cash)
    print("История операций", history)
    print("1 - пополнить")
    print("2 - снять")
    print("0 - выйти")

    action = input("введите номер операции: ")

    match action:
        case "1":
            addition()
            history
        case "2":
            withdrawal()

        case "0":
            quit()

    if count == 3:
        total_cash *= 1.03
        count = 0