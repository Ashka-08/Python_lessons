from employee import Employee

class UserBasicException(Exception):
    """Базовый класс ошибок"""

    def __init__(self, message: str) -> None:
        self.message = message
    
    def __str__(self) -> str:
        return f'{self.message}'


class LevelError(UserBasicException):
    """Ошибка уровня доступа при создании нового служащего"""

    def __init__(self, me, new) -> None:
        super(LevelError, self).__init__(f'Ошибка доступа! '
            f'Служащий ({me.name}, доступ: {me.lvl_access}) '
            f'не имеет права создавать служащего ({new.name}, доступ: {new.lvl_access}) '
            f'выше собственного уровня доступа')


class AccessError(UserBasicException):
    """Ошибка доступа в случе отсутствия служащего в базе"""

    def __init__(self, me: Employee) -> None:
        super(AccessError, self).__init__(f'Ошибка доступа! '
            f'Служащий {me.name} ({me.employee_id}) не найден в базе')


class UniqueID(UserBasicException):
    """Ошибка неуникального ID при создании нового служащего"""

    def __init__(self, new_id: str) -> None:
        super(UniqueID, self).__init__(f'Ошибка доступа! '
            f'Служащий с таким ID ({new_id}) уже существует')


