# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода
# проекта.

class UserException(Exception):
    pass

class UserLevelError(UserException):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Ошибка уровня! {self.value}'

class UserPermissionError(UserException):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Ошибка доступа! {self.value}'