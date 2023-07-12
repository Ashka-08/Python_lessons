import view
import model

def button_click():
    view.hello_message()
    data_base = model.read_database()
    menu = view.show_menu()
    
    if menu == 0:
        # добавление человека
        new = view.input_person(data_base)
        data_base = model.add_to_data_base(new, data_base)
        c = view.save_message()
        if c == 1:
            model.save_database(data_base)
            view.success_message()
        else:
            view.error_message()

    elif menu == 1:
        # удаление сотрудника по id
        model.del_employee(data_base, view.input_id_to_del())
        view.success_message()
        ch = view.save_message()
        if ch == 1:
            data_base = model.id_count(data_base) # востановление очередности id
            model.save_database(data_base)
        else:
            view.error_message()

    elif menu == 2:
        # редактирование
        view.change_employee(data_base)
        ch = int(input('Продолжить редактирование? 0 - нет, 1 - да: '))
        if ch == 1:
            data_base = view.change_employee(data_base)
        else:
            ch2 = view.save_message()
            if ch2 == 1:
                data_base = model.id_count(data_base) # востановление очередности id
                model.save_database(data_base)
                view.success_message()
            else:
                view.error_message()

    elif menu == 3:
        # поиск сотрудника по фамилии
        view.print_data(model.search_employee(view.input_last_name(), data_base))

    elif menu == 4:
        # поиск по должности
        view.print_data(model.search_position(view.input_position(), data_base))

    elif menu == 5:
        # поиск по зп
        model.search_salary(view.input_min_salary(), view.input_max_salary(), data_base)

    elif menu == 6:
        # Импорт в json
        model.import_json(data_base)
        view.success_message()

    elif menu == 7:
        # импорт в csv
        model.import_csv(data_base)
        view.success_message()

    elif menu == 8:
        # экспорт из json
        data_base = model.export_json(data_base)
        model.save_database(data_base)
        view.success_message()

    elif menu == 9:
        # экспорт из csv
        new_base = model.export_csv(data_base)
        model.save_database(new_base)

    elif menu == 10:
        # показать весь список
        view.print_data(data_base)

    else: 
        print('\nПрограмма закрыта\n')