class EmployeeName:
    """Дескриптор для имени при создании служащего"""

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)
    
    def __set__(self, instance, value: str):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f'Имя может состоять только из букв: {value}')
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f'Имена должны быть с большой буквы: {value}')
        setattr(instance, self.parameter_name, value)


class EmployeeID:
    """Дескриптор для ID при создании служащего"""

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)
    
    def __set__(self, instance, value: str):
        if not len(value) == 6:
            raise ValueError(f'ID должен быть шестизначным: {value}')
        if not value.isdigit():
            raise ValueError(f'ID должен содержать только цифры: {value}')
        setattr(instance, self.parameter_name, value)


class Employee:
    """Класс служащего с проверками и дескрипторами"""
    
    name = EmployeeName()
    employee_id = EmployeeID()

    def __init__(self, name: str, lvl_access: int, employee_id: str) -> None:
        self.name = name
        self.employee_id = employee_id
        if 0 < int(lvl_access) < 8:
            self.lvl_access = int(lvl_access)
        else:
            raise ValueError(f'Уровень доступа должен быть в диапазоне [0, 7]: {lvl_access}')

    def __str__(self) -> str:
        return f'{self.name} ({self.employee_id}) | Доступ: {self.lvl_access}'
    
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.employee_id == other.employee_id

