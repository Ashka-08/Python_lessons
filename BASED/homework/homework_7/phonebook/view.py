def import_data(data, sep=None):
    with open('file_1.txt', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")

def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Категория".center(30))
        print("-"*130)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20))
    else:
        print("Справочник пуст!")