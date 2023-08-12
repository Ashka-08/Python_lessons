# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
# На примере банкомата
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class Bancomat:
    __MAX_LIMIT = 5_000_000
    __WEALTH_TAX = 0.9
    __COMMISSION = 1.5
    __MAX_COUNT = 3
    __COMMISSION_COUNT = 1.03
    __MAX_COMMISSION = 600
    __MIN_COMMISSION = 30

    def __init__(self):
        self.__total_cash = 0
        self.__counter = 0

    def menu(self):
        """Метод вывода меню"""
        print(f"Сумма на счете {self.__total_cash}")
        print("1 - пополнить")
        print("2 - снять")
        print("3 - выход")

    def money_in(self, money):
        """Метод внесения денег"""
        self.__total_cash += money
        self.__counter += 1
        self._check_account()

    def money_out(self, money):
        """Метод снятия денег"""
        self.__total_cash -= money
        self.__counter += 1
        self._check_account()

    def get_account_amount(self):
        """Метод получения общей суммы на счете"""
        return self.__total_cash

    def _check_account(self):
        """Метод начисления процентов за каждую 3 операцию"""
        if self.__total_cash > self.__MAX_LIMIT:
            self.__total_cash *= self.__WEALTH_TAX
            print('Списан налог на роскошь')
        if self.__counter == self.__MAX_COUNT:
            self.__total_cash *= self.__COMMISSION_COUNT
            self.__counter = 0
            print('Списана комиссия за 3-ю операцию')

    def work(self):
        """Метод работы банкомата"""
        while True:
            self.menu()
            choice = input("Введите номер операции: ")
            match choice:
                case "1":
                    add = int(input("Внесите сумму пополнения, кратную 50: "))
                    if add % 50 == 0:
                        self.money_in(add)
                    else:
                        print("Неверная сумма")

                case "2":
                    get = int(input("Введите сумму снятия, кратную 50: "))
                    if get % 50 == 0:
                        percent = get*self.__COMMISSION*0.01
                        if percent < self.__MIN_COMMISSION:
                            percent = self.__MIN_COMMISSION
                        if percent > self.__MAX_COMMISSION:
                            percent = self.__MAX_COMMISSION

                        if self.__total_cash < (get+percent):
                            print("Недостаточно средств")
                        else:
                            self.money_out(get+percent)
                    else:
                        print("Неверная сумма")

                case "3":
                    print('Выход')
                    quit()


bancomat = Bancomat()
bancomat.work()

