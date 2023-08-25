from error import UserUserNotMultipleSumError, UserIntSumError

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
                    add = input("Внесите сумму пополнения, кратную 50: ")
                    try:
                        add = int(add)
                    except UserIntSumError(add) as e:
                        print(e)
                    else:
                        if add % 50 == 0:
                            self.money_in(add)
                        else:
                            raise UserUserNotMultipleSumError(add)

                case "2":
                    get = input("Введите сумму снятия, кратную 50: ")
                    try:
                        get = int(get)
                    except UserIntSumError(add) as e:
                        print(e)
                    else:
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
                            raise UserUserNotMultipleSumError(get)

                case "3":
                    print('Выход')
                    quit()


bancomat = Bancomat()
bancomat.work()