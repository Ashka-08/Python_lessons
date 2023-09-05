# Решение от преподавателя

## Задание 3

Создайте класс с базовым исключением и дочерние классы исключения:
* ошибка уровня,
* ошибка доступа.

## Задание 4

Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.

Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

## Задание 5

Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
* загрузка данных (функция из задания 4)
* вход в систему - требует указать имя и id пользователя. 

    *Для проверки наличия пользователя в множестве используйте магический метод     проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.*

* добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

## Задание 6

Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.

Передавайте необходимые данные из основного кода проекта.