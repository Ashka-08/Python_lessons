import model
import view

def button_click():
    info = ''
    ch = view.print_hello()
    if ch == 1:
        model.add_record(info)
    elif ch == 2:
        model.import_scv()
    elif ch == 3:
        model.import_txt()
    else:
        print('Ошибка, такого пункта меню нет')
