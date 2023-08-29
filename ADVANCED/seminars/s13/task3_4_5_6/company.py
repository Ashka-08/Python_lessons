import json
import os
import random

from faker import Faker

from employee import Employee
from errors import AccessError, LevelError, UniqueID

class Company:

    def __init__(self, name) -> None:
        self.name = name
        if os.path.exists(f'ADVANCED\seminars\s13\\task3_4_5_6\{self.name}.json'):
            with open(f'ADVANCED\seminars\s13\\task3_4_5_6\{self.name}.json', 'r', encoding='UTF-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = self.create_employee(self.name, 10)
        self.employees = [Employee(e_name, e_lvl, e_id)
            for e_lvl, person in employees_list.items()
            for e_id, e_name in person.items()]
    
    def login(self, name: str, e_id: str):
        """Метод входа в систему - требует указать имя и id пользователя"""
        for employee in self.employees:
            if employee.name == name and employee.employee_id == e_id:
                return employee
        raise AccessError(Employee(name, 0, e_id))
    
    def hiring(self, me: Employee, new_name: str, new_id: str, new_lvl: int):
        """Метод найма служащего"""

        if me:
            if me.lvl_access > new_lvl:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, new_lvl, new_id))
                    self.__save()
                else:
                    raise UniqueID(new_id)
            else:
                raise LevelError(me, Employee(new_name, new_lvl, new_id))
        else:
            raise AccessError(me)
        

    def __save(self):
        """Метод сохранения после найма служащего"""
        employees_list = {}
        for employee in self.employees:
            if employee.lvl_access in employees_list:
                employees_list[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_list[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'ADVANCED\seminars\s13\\task3_4_5_6\{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees_list, file, indent=3, ensure_ascii=False)

    def create_employee(company: str, count: int):
        """Создание рандомного словаря с ключами с уровнями доступа
        и значениями в виде словаря с ID и ФИО
        и сохранение в файл формата json"""
        employees = {}
        list_id = []
        for _ in range(count):
            name = Faker(locale='ru_RU')
            name = name.name()
            while True:
                employee_id = str(random.randint(1, 999999)).zfill(6)
                if employee_id not in list_id:
                    list_id.append(employee_id)
                    break
            lvl_access = int(employee_id) % 7 + 1
            if lvl_access in employees:
                employees[lvl_access][employee_id] = name
            else:
                employees[lvl_access] = {employee_id: name}
        with open(f'ADVANCED\seminars\s13\\task3_4_5_6\{company}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees, file, indent=3, ensure_ascii=False)
        return employees

