import model
import view

def button_click():
    info = []
    ch = view.print_hello()
    if ch == 1:
        model.add_record(info)
        model.write_base(info)
        view.print_add(info)
        button_click()
    elif ch == 2:
        model.import_scv()
        view.success()
    elif ch == 3:
        model.import_txt()
        view.success()
    elif ch == 4:
        print('End')
    else:
        print('Ошибка, такого пункта меню нет')
