"""
Задача 38:
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и
удаления данных
"""

def add_info(filename): #добавление данных в файл
    with open(filename, "r", encoding="utf-8") as data:
        phonedata_file = data.read()
    with open(filename, "a", encoding="utf-8") as data:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{fio} {phone_number}\n")
        print(f"Добавлена запись: {fio} | {phone_number}\n")

def show_info(filename): #вывод на экран
    print("ФИО  Телефон\n")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

def change_info(filename): #корректировка данных
    print("ФИО  Телефон\n")
    with open(filename, "r", encoding='utf-8') as data:
        phone_data = data.read()
    print(phone_data)
    print("")
    row_number_to_delete = int(input("Введите номер строки для редактирования: ")) - 1
    phone_data_rows = phone_data.split("\n")
    change_phone_data_rows = phone_data_rows[row_number_to_delete]
    new_data = change_phone_data_rows.split("  ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    if len(fio) == 0:
        fio = new_data[1]
    if len(phone) == 0:
        phone = new_data[2]
    changed_row = f"{fio}  {phone}"
    phone_data_rows[row_number_to_delete] = changed_row
    print(f"Запись - {change_phone_data_rows} изменена на - {changed_row}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(phone_data_rows))

def delete_info(filename): #удаление информации
    print("ФИО  Телефон\n")
    with open(filename, "r", encoding="utf-8") as data:
        phone_data = data.read()
        print(phone_data)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    phone_data_rows = phone_data.split("\n")
    delete_phone_data_rows = phone_data_rows[index_delete_data]
    phone_data_rows.pop(index_delete_data)
    print(f"Удалена запись: {delete_phone_data_rows}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(phone_data_rows))

def main(): #основной код
    action = 0
    file_phonedata = "phonedata.txt"
    with open(file_phonedata, "a", encoding="utf-8") as file:
         file.write("") #файл создастся если его нет

    while action != 5:
        print("Выберите действие: 1 - вывод инфо на экран; 2 - запись данных в файл; 3 - изменение данных; "
              "4 - удаление записей; 5 - выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_info(file_phonedata)
            break
        elif action == 2:
            add_info(file_phonedata)
            break
        elif action == 3:
            change_info(file_phonedata)
            break
        elif action == 4:
            delete_info(file_phonedata)
            break
        else:
            action = 5

main()