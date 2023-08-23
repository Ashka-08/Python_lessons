# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


class Factorial:

    def __init__(self, start, stop = None, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        if stop is None:
            self.stop = start
            self.start = 1
        self.value = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            self.value *= self.start
            self.start += self.step
            return self.value
        raise StopIteration


f1 = Factorial(5)
print(*f1)

f2 = Factorial(1, 7)
print(*f2)

f3 = Factorial(start=1, stop=8, step=2)
print(*f3)